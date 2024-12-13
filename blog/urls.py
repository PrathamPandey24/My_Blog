from django.urls import path
from . import views


#link for functions in views for moving through starting page-->all blog-->single blog



urlpatterns=[
    path("", views.starting_page, name="starting-page"),                                            
    path("posts",views.posts , name="posts-page"),
    path("posts/<slug:slug>",views.post_details, name="post-detail-page"),
]