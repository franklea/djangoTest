from django.shortcuts import render
from models import User,Test,WebPage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def data(request):
    if request.method == 'GET':
        print "---------- A Get Request --------"
        if 'name' in request.GET and 'age' in request.GET:
            print 'name: ' + request.GET['name'].encode('utf-8')
            print 'age: ' + request.GET['age'].encode('utf-8')
            print 'val:' + request.GET['val'].encode('utf-8')
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
        if 'name' in request.POST and 'age' in request.POST:
            print 'name : ' + request.POST['name']
            print 'age : '  + request.POST['age']
            print 'val : ' + request.POST['val']

            # save to db
            #item = Test(user=request.POST['user'],content=request.POST['content'])
            #item.save()

            #context = {}
            #context['result'] = request.POST['name'] + '\n' + request.POST['age']
            #context['dbrst'] = "date save succeed! "
            #return render(request,'data.html',context)
            response = JsonResponse({'response': 'Thank you ! Have a good day! '})
            return response
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

