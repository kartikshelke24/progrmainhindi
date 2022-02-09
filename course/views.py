
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from course.models import Course, Playlist, CourseComment

# Create your views here.
def allCourse(request):
    allCourse = Course.objects.all()

    context = {'allCourse' : allCourse}
    return render(request, 'course/allCourse.html', context)
    # return HttpResponse("Hey")
    
def playlist(request, slug):
    playlist = Playlist.objects.get(slug=slug)
    courseTitle = Playlist.objects.get(slug=slug).courseTitle
    allPlaylist = Playlist.objects.filter(courseTitle=courseTitle)
    courseComment = CourseComment.objects.filter(post=playlist,parent=None)
    courseCommentReply = CourseComment.objects.filter(post=playlist).exclude(parent=None)
    # allPlaylist = Playlist.objects.all()
    context = {'playlist' : playlist,
                'allPlaylist' : allPlaylist,
                'courseComment' : courseComment,
                'courseCommentReply' : courseCommentReply}
    return render(request, 'course/playlist.html', context)
    # return HttpResponse("Hey")

    


def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('commentText')
        user=request.user
        postSno =request.POST.get('postSno')
        parentSno =request.POST.get('parentSno')
        post= Playlist.objects.get(sno=postSno)
        if parentSno=="":
            comment=CourseComment(commentText= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully",extra_tags="simple_tag")
        else:
            parent= CourseComment.objects.get(sno=parentSno)
            comment=CourseComment(commentText= comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully",extra_tags="simple_tag")
    
    return redirect(f"/courses/{post.slug}")