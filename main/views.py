from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog
from django.utils import timezone 

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

def detail(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request,'main/detail.html',{'blog' : blog})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_blog =Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('detail',new_blog.id)