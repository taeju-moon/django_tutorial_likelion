from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, CommentForm, IdPostForm, IdCommentForm
from .models import Post, IdPost

def home(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "index.html", {"posts":posts})

def postcreate(request):
    if request.method == "POST" or request.method=="FILES":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
        return render(request, "post_form.html", {"form":form})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, "detail.html", {"post":post, "comment_form":comment_form})

#save comment
def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect("detail", post_id)



###############################################


def idHome(request):
    posts = IdPost.objects.all().order_by("-date")
    return render(request, "id_index.html", {"posts":posts})

def idPostcreate(request):
    if request.method == "POST" or request.method=="FILES":
        form = IdPostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.writer = request.user
            unfinished.save()
            return redirect("idHome")
    else:
        form = IdPostForm()
        return render(request, "id_post_form.html", {"form":form})

def idDetail(request, post_id):
    post = get_object_or_404(IdPost, pk=post_id)
    comment_form = IdCommentForm()
    return render(request, "id_detail.html", {"post":post, "comment_form":comment_form})

#save comment
def new_idComment(request, post_id):
    filled_form = IdCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(IdPost, pk=post_id)
        finished_form.save()
    return redirect("idDetail", post_id)