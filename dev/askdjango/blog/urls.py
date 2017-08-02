from django.conf.urls import url	# 참고: https://github.com/django/django/blob/1.11.3/django/conf/urls/__init__.py#L77-L85
from . import views
from . import views_cbv

''' 1. r'^$'에서 r에 대한 설명

r은 정규표현식이 아니다.
r은 Raw의 약자이다.

\n --> 1글자
\d --> 2글자(\, d) ==> \\d로 사용해야 한다.

\ 를 적게 사용하는 방법으로 r을 사용하면 된다.

'\\d'는 r'\d'와 같은 표현이다.
r을 써주면 escaping을 해준다.
'''

''' 2. urlpatterns에 대한 설명

urls.py 파일에는 항상 urlpatterns 리스트(순서가 있는 자료구조)가 있어야한다.
정의할 항목이 없다면 빈 리스트라도 만들어야 한다.

리스트는 순서가 있으므로 맨 위에서 부터 matching을 시작한다.
모든 url 정의가 유니크할 필요는 없다.
매칭되는 url이 없다면 404 not found 메시지가 발생한다.
'''

# 1개의 view에 여러 개의 url을 정의해도 된다.
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'), # ^$는 아무것도 없는 정규표현식을 의미함, r은 Raw의 약자이다, URL 리버스는 name을 통해 뷰함수를 찾아가는 것이다.
    url(r'^new/$', views.post_new, name='post_new'),
    #url(r'^new/$', views_cbv.post_new, name='post_new'), # blog/views_cbv.py 참고
	url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), # URL 패턴이 일치할 경우 pk에 저장된 값을 post_edit 뷰에 넘겨준다, <pk>와 post_edit 뷰에서 사용하는 인자 이름(pk)은 항상 같아야한다.
    #url(r'^(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'), # blog/views_cbv.py 참고
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
	url(r'^$', views.post_list2),	# FBV 정의 (템플릿을 통해 HTML 형식 응답하기)
    url(r'^$', views.post_list1),	# FBV 정의 (문자열로 HTML 형식 응답하기)
    url(r'^$', views.excel_download), # FBV: 엑셀 다운로드 응답하기
	url(r'^$', views.post_list3),	# FBV 정의 (JSON 형식 응답하기)
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),	# 인자가 3개일 경우
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),				# 인자가 2개일 경우
    url(r'^sum/(?P<x>\d+)/$', views.mysum),							# 인자가 1개일 경우
	url(r'^hello/(?P<korean_name>[ㄱ-힣]+)/(?P<age>[0-9]+)/$', views.greet_korean),
]
