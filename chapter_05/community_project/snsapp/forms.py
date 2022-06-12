from django import forms
from .models import Post, Comment, IdComment, IdPost

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        
        self.fields["title"].widget.attrs = {
            "class":"form-control",
            "placeholder":"글 제목을 입력하세요",
            "rows":20,
        }
        self.fields["body"].widget.attrs = {
            "class":"form-control",
            "placeholder":"글 제목을 입력하세요",
            "rows":20,
            "cols":100,
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields["comment"].widget.attrs = {
            "class":"form-control",
            "placeholder":"댓글을 입력하세요",
            "rows":10,
        }




class IdPostForm(forms.ModelForm):
    class Meta:
        model = IdPost
        fields = ["title", "body"]

    def __init__(self, *args, **kwargs):
        super(IdPostForm, self).__init__(*args, **kwargs)
        
        self.fields["title"].widget.attrs = {
            "class":"form-control",
            "placeholder":"글 제목을 입력하세요",
            "rows":20,
        }

        self.fields["body"].widget.attrs = {
            "class":"form-control",
            "placeholder":"글 제목을 입력하세요",
            "rows":20,
            "cols":100,
        }

class IdCommentForm(forms.ModelForm):
    class Meta:
        model = IdComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(IdCommentForm, self).__init__(*args, **kwargs)

        self.fields["comment"].widget.attrs = {
            "class":"form-control",
            "placeholder":"댓글을 입력하세요",
            "rows":10,
        }