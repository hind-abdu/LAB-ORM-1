from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post

def show_post(request:HttpRequest):
    posts = Post.objects.all()
    return render(request, 'main_app/home.html', {'posts': posts})

def create_post_view(request: HttpRequest):

    if request.method == 'POST':
        new_post = Post(
            title = request.POST['title'],
            content = request.POST['content'],
            is_published = request.POST['is_published']
        )
        new_post.save()

    return render(request, 'main_app/create.html')

