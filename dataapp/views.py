from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse,HttpResponse
from dataapp.models import Data
from django.core.paginator import Paginator
from lxml import etree
import requests
import random
import time



def logd(fun):
    def log(request):
        format = '%Y/%m/%d %H:%M:%S'
        value = time.localtime(int(time.time()))
        dt = time.strftime(format, value)
        print(request.META)
        url=request.get_raw_uri()
        ip=request.META['REMOTE_ADDR']
        url1 = 'http://ip.tool.chinaz.com/' + ip
        html = etree.HTML(requests.get(url=url1).text)
        p = html.xpath('//p[@class="WhwtdWrap bor-b1s col-gray03"]//text()')
        with open('log.fei.txt', 'a+', encoding='utf-8') as f:
            logs=str(dt+'\t\t'+'start at'+'\t\t'+url+'\t\t'+ip+'\t\t'+p[7]+'\n')
            f.write(logs)
            print(logs)
            return fun(request)
    return log



@logd
def home(request):
    a='hjjjarndv,.daslfad.f.a.dd1sads2f4daadddj,hdfmcncv,aldfakl'
    flag=request.GET.get('flag')
    key=request.GET.get('key')
    parentid=request.GET.get('parentid')
    if not key:
        key='1'
    if not flag:
        flag='1'
    uname=request.session.get('uname')
    if uname:
        result=render(request,'dataapp/main.html',{'flag':flag,'key':key,'parentid':parentid})
        string=random.sample(a,10)
        string=''.join(string)
        result.set_cookie('string',string)
        return result
    return redirect('userapp:login')



@logd
def menu(request):
    a='uiatja.aa{0oip98o5q34piav.,ml9OIEWRIUTOINl?P；qweipr53a75agfah2a04ga2d0WR'
    res=request.COOKIES.get('string')
    if res:
        meta=request.META
        print(meta['HTTP_REFERER'])
        print(request.META['REMOTE_ADDR'])
        number=request.GET.get('num')
        flag=request.GET.get('flag')

        if not number:
            number=1
        key=request.GET.get('key')
        parentid=request.GET.get('parentid')
        print(key,parentid)
        if  flag:
            if not key:
                url=reverse('dataapp:home')+'flag=2'+'&parentid='+parentid
                return redirect(url)
            url = reverse('dataapp:home') + 'flag=2' + '&parentid=' + parentid+'&key='+key
            return redirect(url)
        if parentid=='3':
            if key=='Python Web':
                data=Data.objects.filter(expect_city__icontains='北京',expect_zhiwei__icontains='互联网')
            elif key=='爬虫':
                data = Data.objects.filter(expect_city__icontains='北京', expect_zhiwei__icontains='教育')
            elif key=='大数据':
                data = Data.objects.filter(expect_city__icontains='北京', expect_zhiwei__icontains='汽车')
            elif key=='AI':
                data = Data.objects.filter(expect_city__icontains='北京', expect_zhiwei__icontains='其他')
            elif not key:
                data = Data.objects.filter(expect_city__icontains='北京')
        elif parentid=='4':
            if key=='Python Web':
                data=Data.objects.filter(expect_city__icontains='上海',expect_zhiwei__icontains='互联网')
            elif key=='爬虫':
                data = Data.objects.filter(expect_city__icontains='上海', expect_zhiwei__icontains='教育')
            elif key=='大数据':
                data = Data.objects.filter(expect_city__icontains='上海', expect_zhiwei__icontains='汽车')
            elif key=='AI':
                data = Data.objects.filter(expect_city__icontains='上海', expect_zhiwei__icontains='其他')
            elif not key:
                data = Data.objects.filter(expect_city__icontains='上海')
        elif parentid=='5':
            if key=='Python Web':
                data=Data.objects.filter(expect_city__icontains='广',expect_zhiwei__icontains='互联网')
            elif key=='爬虫':
                data = Data.objects.filter(expect_city__icontains='广', expect_zhiwei__icontains='教育')
            elif key=='大数据':
                data = Data.objects.filter(expect_city__icontains='广', expect_zhiwei__icontains='汽车')
            elif key=='AI':
                data = Data.objects.filter(expect_city__icontains='广', expect_zhiwei__icontains='其他')
            elif not key:
                data = Data.objects.filter(expect_city__icontains='广')
        elif parentid=='6':
            if key=='Python Web':
                data=Data.objects.filter(expect_city__icontains='深圳',expect_zhiwei__icontains='互联网')
            elif key=='爬虫':
                data = Data.objects.filter(expect_city__icontains='深圳', expect_zhiwei__icontains='教育')
            elif key=='大数据':
                data = Data.objects.filter(expect_city__icontains='深圳', expect_zhiwei__icontains='汽车')
            elif key=='AI':
                data = Data.objects.filter(expect_city__icontains='深圳', expect_zhiwei__icontains='其他')
            elif not key:
                data = Data.objects.filter(expect_city__icontains='深圳')
        pator = Paginator(data, 3)
        page = pator.page(number=int(number))
        result=render(request,'dataapp/menu.html',{'page':page,'key':key,'parentid':parentid})
        string = random.sample(a, 10)
        string = ''.join(string)
        result.set_cookie('string', string)
        return result
    return HttpResponse('欢迎火星来客')

def introduce(request):
    return render(request,'dataapp/introduce.html')
def ajax1(request):
    l=[]
    for i in ['北京', '上海', '广', '深圳']:
        res=Data.objects.filter(expect_city__icontains=i)
        l.append(len(list(res)))
    return HttpResponse(str(l))

def ajax2(request):
    l = []
    for i in ['北京', '上海', '广', '深圳']:
        res = Data.objects.filter(expect_city__icontains=i)
        age=Data.objects.filter(age__icontains='25',expect_city__icontains=i)
        l.append([len(list(res)),len(list(age)),random.randint(1,20),random.randint(1,20)])
    return HttpResponse(str(l))


def ajax3(request):
    l=[]
    for i in ['北京','上海','广州','深圳']:
        age=Data.objects.filter(expect_city__icontains=i).aggregate(mm=Avg('age'))
        l.append({'value':int(age['mm']),'name':i})
    return JsonResponse(l,safe=False)

def ajax4(request):
    with open('log.fei.txt','r',encoding='utf-8') as log:
        text=log.readlines()
        print(text)
        l=[]
        dic={}
        for data in text:
            key=data.split('\t\t')[-1].replace('\n','')
            if key=='本地计算机':
                key='河南'
            for j in dic:
                if key==j:
                    dic[key]['value']=dic[key]['value']+1
                    break
            else:
                dic[key]={'name':key,'value':1}
        for i in dic:
            l.append(dic[i])
        print(l)
        return JsonResponse(l,safe=False)
