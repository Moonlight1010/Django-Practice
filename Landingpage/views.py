from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.all().order_by('-id')
    form = PostForm(request.POST)
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f'You have succesfully made a post')
            return redirect('index')
        else:
            form = PostForm()
    else:
        form = PostForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'Landingpage/home.html', context)

def about(request):
    height='6ft'
    return render(request, 'Landingpage/about.html', {'height':height})

def notification(request):
    return render(request, 'Landingpage/notification.html')

def read(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post,
    }
    return render(request, 'Landingpage/read.html', context)
def update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST, instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful')
            return redirect('read-page',id=post.id)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request, 'Landingpage/update.html', context)
    
def delete_view(request, id):
    post = Post.objects.get(id=id)
    post_title = post.title
    post.delete()
    messages.error(request, f'"{post_title}" has been sucessfully deleted!')
    return redirect('index')
