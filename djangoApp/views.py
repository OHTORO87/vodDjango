from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('헬로우!')

def create(request):
    return HttpResponse('크리에이트')

def read(request, id):
    return HttpResponse('아이디는?'+id)