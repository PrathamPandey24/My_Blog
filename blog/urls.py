from django.urls import path
from . import views


#link for functions in views for moving through starting page-->all blog-->single blog



urlpatterns=[
    path("", views.StartingPageView.as_view(), name="starting-page"),                                            
    path("posts",views.AllPostsView.as_view() , name="posts-page"),
    path("posts/<slug:slug>/",views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later"),
 ] 