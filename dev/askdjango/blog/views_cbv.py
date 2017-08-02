from django.views.generic import CreateView, UpdateView
from .models import Post
from .forms import PostForm

'''
클래스 기반 뷰는 재사용에 초점을 맞춘 것이다.
초보자의 경우에는 함수 기반 뷰를 사용하는 것이 좋다. 지금 CBV를 공부하는 것은 추천하지 않는다고 하심.
함수기반 뷰는 legacy가 아님. 처음부터 FBV를 쓰는 것을 권장하고 재사용성을 하고 싶다면 CBV를 적용해보라고 하심
'''

post_new = CreateView.as_view(model=Post, form_class=PostForm, success_url='/weblog/')

post_edit = UpdateView.as_view(model=Post, form_class=PostForm, success_url='/weblog/')
