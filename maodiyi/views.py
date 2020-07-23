from django.shortcuts import render
# Create your views here
from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType, Jobs
import rsa
import base64


def index(request):
    # import requests
    # import json
    # api_request = requests.get("https://api.github.com/users?since=0")
    # api = json.loads(api_request.content)
    args="Home page"
    return render(request,'index.html',{"args":args})

def guess(request):
    if request.method =='POST':

        trynum = request.POST['trynum']
        print(type(trynum))


        target=request.session.get("target","null")
        if target=="null":
            import random
            target = random.randint(0,100)
            request.session["target"]=target




        if trynum.isnumeric():
            num=int(trynum)
            if (num == target):
                result = "Yeah，猜中了！ 你的数是："+trynum+" "
                result+="可以继续猜下一个数字了："
                request.session.clear()
            elif (num <= target):
                result = "你猜的数 小 啦 你的数是："+trynum
            else:
                result = "你猜的数 大 啦 你的数是："+trynum
        else:
            result = "请输入有效数字"
        # result = result+"  target="+str(target)

        return render(request,'guess.html',{'result':result})
    else:
        notfound = "请在框里输入一个数字"
        return render(request, 'guess.html', {'notfound': notfound})


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_detail.html', context)

def getrsasign(data):
    with open('./maodiyi/bgedo_pri.pem', 'r') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
        

    ensign = rsa.sign(data.encode(), privkey, 'SHA-256')
    encodestr = base64.b64encode(ensign).decode()
    # 返回加密签名
    return (encodestr)

def bgsig(request):
    if request.method == 'POST':
        data = request.POST['data']
        result = getrsasign(data)
        return render(request,'bgsig.html',{'result':result})
    else:
        error = "有问题，请检查"
        return render(request, 'bgsig.html', {'error': error})

def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blogs_with_type.html', context)


def mathtest(request):
    import random
    tests = []
    i = 0
    while i < 10:
        x = random.randint(1, 9999)
        y = random.randint(1, 9999)
        tests.append(str(x) + " x " + str(y) + " =    ;")
        i = i + 1

    # tests2 = []
    i = 0
    while i < 10:
        x = random.randint(1, 999)
        y = random.randint(1, 999)
        b = divmod(x, y)
        if b[1] == 0 and b[0] > 1:
            tests.append(str(x) + " / " + str(y) + " =    ;")
            i = i + 1

    context = {}
    context['tests'] = tests
    return render_to_response('math.html', context)


def job_query(request):
    context = {}
    context['jobs'] = Jobs.objects.all()
    return render_to_response('job_list.html', context)
