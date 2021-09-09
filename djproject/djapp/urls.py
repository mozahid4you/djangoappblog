from django.urls import path
from . views import HomeList,Blogdetail,Addpost,Updatepost,Deletepost

urlpatterns = [

    path('',HomeList.as_view(),name='home'),
    path('detail/<int:pk>',Blogdetail.as_view(),name='detail'),
    path('addpost/',Addpost.as_view(),name='addpost'),
    path('update/<int:pk>',Updatepost.as_view(),name='update'),
    path('delete/<int:pk>',Deletepost.as_view(),name='delete'),

]
