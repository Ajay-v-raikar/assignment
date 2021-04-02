from django.http import HttpResponse
import os

file_path=os.path.abspath(__file__)
dir_path=os.path.dirname(file_path)
print(dir_path)
def home(request):
    file_addr=os.path.join(dir_path,"sample.html")
    file = open(file_addr,'r')
    data=file.read()
    return HttpResponse(data)