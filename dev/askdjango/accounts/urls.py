from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views


'''url(r'^login/$', auth_views.login, name='login'),에 대한 설명
예를 들어 http://192.168.0.7:8080/accounts/login/ 접속시 프로파일 페이지로 이동한다.
장고 로그인 폼에서는 로그인 시 기본적으로 프로파일 페이지로 이동하게 끔 되어있다.
next를 이용하면 로그인 후 이동할 페이지를 지정할 수 있다.
예) http://127.0.0.1:8080/accounts/login/?next=/blog/
'''

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login',
        kwargs={
            'template_name': 'accounts/login.html', # 예) http://192.168.0.7:8080/accounts/login/
            'authentication_form': LoginForm,
        }),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
]