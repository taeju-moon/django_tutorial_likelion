from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

def home(request):
    #블로그 글들을 가져오기
    #posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date') #내림차순
    return render(request, "index.html", {"posts":posts})

#블로그 글 작성 html Form을 보여주는 함수
def new(request):
    return render(request, "new.html")

#블로그 글 저장하는 함수
def create(request):
    if (request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

#django form을 이용해서 입력값을 받는 함수
#GET요청(=입력값을 받을 수 있는 HTML을 갖다 줘)
#POST요청(=입력한 내용을 database에 저장)
#둘 다 처리 가능한 함수
def formcreate(request):
    if (request.method == 'POST'):
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        #HTML을 가져다 주기
        form = BlogForm()
    return render(request, "formcreate.html", {"form":form}) #찍어서 보내주고 싶은 내용을 세번째 인자에 딕셔너리 형태로 전달

#model form을 이용해 입력값을 받는 함수
def modelcreate(request):
    if (request.method == 'POST'  or request.method == 'FILES'): #FILES는 사진 데이터임
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #HTML을 가져다 주기
        form = BlogModelForm()
    return render(request, "formcreate.html", {"form":form})

def detail(request, blog_id):
    load_detail = get_object_or_404(Blog, pk=blog_id) #Blog객체 중 pk=blog_id인 객체 하나를 가져올 것임
    comment_form = CommentForm()
    return render(request, "detail.html", {"post":load_detail, "comment_form":comment_form})

def createcomment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) #아직 저장하지 마라
        finished_form.post = get_object_or_404(Blog, pk=blog_id) #어떤 블로그의 댓글인지
        finished_form.save()
    return redirect("detail", blog_id) #blog_id를 가진 detail페이지로 이동
    