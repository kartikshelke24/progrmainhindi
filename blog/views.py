
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages

from blog.models import BlogComment, BlogPost

# Create your views here.
def blogHome(request):
    allPost = BlogPost.objects.all()
    context = {'allPost' : allPost}
    return render(request, 'blog/blogHome.html',context)
  
    
def blogPost(request,slug):
    post = BlogPost.objects.get(postSlug=slug)
    postComment = BlogComment.objects.filter(post=post,parent=None)
    commentReply = BlogComment.objects.filter(post=post).exclude(parent=None)
    context = {'post' : post,'postComment':postComment,'commentReply':commentReply}
    return render(request, 'blog/blogPost.html',context)


def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('commentText')
        user=request.user
        postSno =request.POST.get('postSno')
        parentSno =request.POST.get('parentSno')
        post= BlogPost.objects.get(sno=postSno)
        if parentSno=="":
            comment=BlogComment(commentText= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(commentText= comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    
    return redirect(f"/blog/{post.postSlug}")
    




