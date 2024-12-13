from django.shortcuts import render ,get_object_or_404
from .models import Post

#function for the first starting page 
def starting_page(request):
    latest_posts= Post.objects.all().order_by("date")[:3]
    return render(request, "blog/index.html", {"posts":latest_posts})


#function for displaying all blogs after starting page
def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request ,"blog/all-posts.html", {"all_posts":all_posts})


#function for displaying the specific blog clicked on 
def post_details(request, slug):
    identified_post=get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post":identified_post,
        "post_tags":identified_post.tags.all()
    })

