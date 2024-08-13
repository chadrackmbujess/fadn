from django.urls import path
from publication import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.handleblog,name='blog'),
    #path('publication/<int:id_publication>',views.detail,name="detail"),
    path('video',views.video,name='video'),
    #path('profile',views.profile,name='profile'),
    #path('internshipdetails',views.internshipdetails,name='internshipdetails'),
    path('commentaire/<int:pk>/add-comment',views.add_comment,name='add-comment'),
    path('commentaire/<int:pk>/delete-comment',views.delete_comment,name='delete-comment'),
    path('comments',views.comment_list,name='comment_list'),

]
