from django.shortcuts import render, redirect
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from typing import ContextManager
from .models import landing
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from googletrans import Translator

# import requests 

#한-영
import os
import sys
import urllib.request



# Create your views here.
def index(request):
    context={'a':'b'}
    return render(request, 'landing/index.html',context)

def inputtext(request):
    inputtext = request.POST.get('inputtext')

    inputtext.save()
    # print(inputtext)
    return redirect('landing/index.html')

def landing(request, textarea):
    # 한영
    # client_id, client_secret는 자신의 ID로 바꿔 주세요
    client_id = "nyNyf0syxDi_oOKpZs21"
    client_secret = "9QE7Z4eczb"
    encText = urllib.parse.quote(textarea)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    
 

    if(rescode==200):
        response_body = response.read()
        response_body = response_body.decode('utf-8')
        response_body = json.loads(response_body)
        response_body = response_body["message"]["result"]["translatedText"]
        print('='*10)
        print(response_body)
        context3 = response_body
    else:
        print("Error Code:" + rescode)


    #한-일
    encText = urllib.parse.quote(textarea)
    data = "source=ko&target=ja&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_body = response_body.decode('utf-8')
        response_body = json.loads(response_body)
        response_body = response_body["message"]["result"]["translatedText"]
        print('='*10)
        print(response_body)
        context4_1 = response_body
    else:
        print("Error Code:" + rescode)

    #일-영
    encText = urllib.parse.quote(context4_1)
    data = "source=ja&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_body = response_body.decode('utf-8')
        response_body = json.loads(response_body)
        response_body = response_body["message"]["result"]["translatedText"]
        print('='*10)
        print(response_body)
        context4 = response_body
    else:
        print("Error Code:" + rescode)



    print(textarea)
    print('안되는거같다')
    translator = Translator() 
    str1 = textarea 
    result1 = translator.translate(str1, dest='en')
    print(result1.text)
    str2 = textarea
    result2 = translator.translate(str2, dest='zh-CN')
    result3 = translator.translate(result2.text, dest='en')
    context1 = result1.text
    print(result1.text)
    context2 = result3.text 
 

    # ttranslator = Translator()
    # context1 = ttranslator.translate(textarea)
    contexta = ()
    contexta = [context1, context2, context3, context4] 
    
    return HttpResponse(json.dumps(contexta, ensure_ascii=False))
    