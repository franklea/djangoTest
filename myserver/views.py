from django.shortcuts import render
from models import User,Test,WebPage

# Create your views here

def index(request):
    return render(request, 'index.html')

def data(request):
    if request.method == 'GET':
        print "---------- A Get Request --------"
        if 'name' in request.GET and 'pwd' in request.GET:
            print 'name: ' + request.GET['name'].encode('utf-8')
            print 'pwd: ' + request.GET['pwd'].encode('utf-8')
            context = {}
            test_list = Test.objects.all()
            res = Test.objects.get(user='Tom')
            context['hint'] = res.content
            return render(request,'data.html',context)
        else:
            context = {}
            context['hint'] = 'Please enter your name and password!'
            return render(request,'data.html',context)

    elif request.method == 'POST':
        print "---------- A POST Request --------"
        if 'content' in request.POST and 'user' in request.POST:
            print 'user: ' + request.POST['user']
            print "content: " + request.POST['content']

            # save to db
            item = Test(user=request.POST['user'],content=request.POST['content'])
            item.save()

            context = {}
            context['result'] = request.POST['user'] + '\n' + request.POST['content']
            context['dbrst'] = "date save succeed! "
            return render(request,'data.html',context)
    return render(request, 'data.html')

def getpages(request):
    print "in get pages"
    return render(request,'getpages.html')

def showres(request):
    print "in showres"
    context={}
    if request.method == 'POST':
        device_id = request.POST['device_id']
        ip = request.POST['ip']
        url = request.POST['url']
        content = request.POST['content']
        if device_id and ip and url and content:
            # check if data is empty
            print "device_id: " + device_id
            print "ip address: " + ip
            print "url: " + url
            print "content: " + content
            item = WebPage(device_id=device_id, device_ip=ip, weburl=url, page_content=content)
            item.save()

            context['msg'] = "data save succeed ! "
        else :
            context['msg'] = "Please input all information ! "
        return render(request, 'result.html', context)
    return render(request,'result.html')

def test(request):
    return render(request,'test.html')

