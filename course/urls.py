from django.urls import path,include
# from froala_editor import views
from course import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('',views.allCourse,name='allCourse'),
    path('<str:slug>',views.playlist,name='playlist'),
    # path('froala_editor/',include('froala_editor.urls')),

]