from django.shortcuts import render
from .models import Blog

# Create your views here.

def showmain(request):
    blogs = Blog.objects.all()
    return render(request, 'main/mainpage.html',{"blogs":blogs})
  
def introduceMe(request): #소개 페이지 
    return render(request, 'main/introduce.html')

def photoMe(request): # 사진 
    return render(request, 'main/photo.html')
 
def profileMe(request): # 프로파일 !
    return render(request, 'main/profile.html')

def home(request):
    userName = request.GET['name']
    return render(request, 'main/home.html',{'userName':userName})
