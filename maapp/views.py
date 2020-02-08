from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request,'home.html',{"api":api})

def user(request):
    if request.method == 'POST':
        import requests
        import json

        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/"+user)
        username = json.loads(user_request.content)

        return render(request, 'user.html', {'username':username})
    else:
        notfound ="请在搜索框里输入你要查询的用户。。。"
        return render(request, 'user.html', {'notfound':notfound})















