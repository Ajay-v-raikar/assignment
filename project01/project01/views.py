from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello welcome to project-1</h1>")