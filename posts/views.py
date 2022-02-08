from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # if the method is Post
    if request.method == 'POST':
        form = PostForm(request.POST)

        # if the form is valid
        if form.is_valid():
            #yes, save
            form.save()

            # redirect to home
            return HttpResponseRedirect("/")

        else:
            # No, show error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit=20
    posts = Post.objects.all()[:20]

    # show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    # find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
