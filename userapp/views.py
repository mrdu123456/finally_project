from django.shortcuts import render,HttpResponse,redirect
from userapp.models import User
from aliyunsdkcore import client
from aliyunsdkafs.request.v20180112 import AuthenticateSigRequest
from aliyunsdkcore.profile import region_provider
from lxml import etree
import random
def dong(re):
    global code
    t=re.GET.get('t')
    sid=re.GET.get('sid')
    sig=re.GET.get('sig')
    print(t)
    print(sid)
    print(sig)

    region_provider.add_endpoint('afs', 'cn-hangzhou', 'afs.aliyuncs.com')
    # YOUR ACCESS_KEY、YOUR ACCESS_SECRET请替换成您的阿里云accesskey id和secret
    clt = client.AcsClient('LTAIVqfIQBwKnALR', 'Nk5YkIqPO4Kp0nsMkEWkMu9e5BJOCc', 'cn-hangzhou')
    request = AuthenticateSigRequest.AuthenticateSigRequest()
    #必填参数：从前端获取，不可更改，android和ios只传这个参数即可
    request.set_SessionId(sid)
    #必填参数：从前端获取，不可更改
    request.set_Sig(sig)
    #必填参数：从前端获取，不可更改
    request.set_Token(t)
    #必填参数：从前端获取，不可更改
    request.set_Scene('nc_login')
    #必填参数：后端填写
    request.set_AppKey('FFFF0N00000000007F25')
    #必填参数：后端填写
    request.set_RemoteIp('192.168.116.1')
    result = clt.do_action(request)#返回code 100表示验签通过，900表示验签失败
    ht=etree.HTML(result)
    code=ht.xpath('//code/text()')[0]
    re.session['code']=code
    return HttpResponse('%s'%code)



def login(request):
    return render(request,'usrapp/login.html')


def loginlogic(request):
    uname=request.POST.get('userid')
    psd=request.POST.get('psw')
    res=User.objects.filter(uname=uname,pwd=psd)
    code=request.session.get('code')
    if res and code=='100':
        request.session['uname']=uname
        return redirect('dataapp:home')
    return redirect('userapp:login')

def ajax4(request):
    uname=request.GET.get('uname')
    res=User.objects.filter(uname=uname)
    if res:
        return HttpResponse('0')
    return HttpResponse('1')

def ajax5(request):
    uname=request.GET.get('uname')
    pwd=request.GET.get('pwd')
    res=User.objects.filter(uname=uname,pwd=pwd)
    print(res)
    if res:
        return HttpResponse('0')
    return HttpResponse('1')





def regist(request):
    return render(request,'usrapp/register.html')

def registlogic(request):
    uname=request.POST.get('userid')
    phone=request.POST.get('usrtel')
    email=request.POST.get('email')
    psw=request.POST.get('psw')
    res = User.objects.filter(phone=phone)
    res1 = User.objects.filter(email=email)
    if res or res1:
        return redirect('userapp:regist')
    else:
        User.objects.create(uname=uname,phone=phone,email=email,pwd=psw)
        request.session['uname']=uname
        return redirect('dataapp:home')



def ajax1(request):
    phone=request.GET.get('phone')
    res=User.objects.filter(phone=phone)
    if not res:
        return HttpResponse('2')
    else:
        return HttpResponse('1')

def ajax2(request):
    emm=request.GET.get('emm')
    res=User.objects.filter(email=emm)
    if not res:
        return HttpResponse('2')
    else:
        return HttpResponse('1')