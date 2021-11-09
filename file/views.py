from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse,JsonResponse
import boto3
from secret import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_STORAGE_BUCKET_NAME
from datetime import datetime
from file.models import Data,Category
import os
from icon_info import ICON_CONFIG
from django.utils.safestring import SafeString

def index(request):
    template = loader.get_template('file/index.html')
    context = {'data':Data.objects.all(),'category':Category.objects.all()}
    return HttpResponse(template.render(context, request))
# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = request.POST
        
        if len(request.FILES) != 0:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                )
            curr_dt = datetime.now()
            timestamp = int(round(curr_dt.timestamp()))    
            file = request.FILES['file']
            
            extension = os.path.splitext(file.name)[1]
            s3_client.upload_fileobj(
                file,
                AWS_STORAGE_BUCKET_NAME,
                str(timestamp)+extension,
                ExtraArgs={
                    "ContentType": file.content_type,
                }
            )
            
            
            data = Data(title=form['title'],content=form['desc'],category=form['category'],file=str(timestamp),extension=extension[1:])
            data.save()
            return redirect('/file/')
        else:
            return JsonResponse({'message':'file_none'})
            
def category(request,category):
    template = loader.get_template('file/repo.html')
    
    context = {'data':Data.objects.filter(category=category),'icon':ICON_CONFIG}
    return HttpResponse(template.render(context, request))
    
def info(request,id):
    template = loader.get_template('file/info.html')
    data=Data.objects.get(id=id)
    #icon = json.loads(ICON_CONFIG)
    context = {'data':data,'icon':ICON_CONFIG[data.extension]}
    return HttpResponse(template.render(context, request))