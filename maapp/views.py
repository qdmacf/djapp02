from django.shortcuts import render

# Create your views here.
def home(request):
    import request
    import json
    api_request = request.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request,'home.html',{"api":api})


