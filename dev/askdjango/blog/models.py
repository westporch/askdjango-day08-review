from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.conf import settings

def min_length_10_validator(value):
    if len(value) < 10:
        raise ValidationError('제목을 10자 이상 입력해주세요.') # raise는 리턴이 아니다. 메시지를 던져주는 것이다.

class Post(models.Model):
    '''
    실습 순서

    1. 모델 정의
    필드가 변경(i.e. title -> name)되면 마이그레이션을 해줘야 한다. 단순히 함수만 추가되는 것은 마이그레이션을 안해도 된다.

    2. python3 manage.py makemigrations blog 실행
    * python3 manage.py makemigrations <app-name>
    * makemigrations 명령은 마이그레이션 파일(초안, 작업지시서)을 생성한다.
    * 모델 파일을 '마이그레이션 파일(작업 지시서)'로 생성한다.
    * DB에 적용하지 않은 작업 지시서는 삭제해도 된다.
    * 하지만 DB에 적용된 작업 지시서는 절대로 삭제하면 안된다.
    * 모델의 내용을 어떻게 DB 적용할지 정의한 것이다.
    * 아직 DB가 생성된 상태는 아니다.
    * title 필드의 이름을 다른 이름(title -> name)으로 변경했다면, 날리고 다시 만들거나 작업지시서에서 이름을 다시 변경(title -> name)한다.
    * 작업지시서가 제대로 만들어졌는지 확인이 필요하다.

    3. blog/migrations/0001_initial.py 파일(작업 지시서) 확인 
    view blog/migrations/0001_initial.py
    * 0001_initial.py 파일이 작업 지시서이다. 이 파일을 열어보면 내역을 확인할 수 있다.

    4. python3 manage.py sqlmigrate blog 0001_initial 명령으로 sql 확인
    * python3 manage.py sqlmigrate <app-name> <migration-name>
    * sql 수행 내역을 확인할 수 있다.
    * blog는 앱 이름을 의미한다.
    * 출력된 sql을 DB에서 그대로 실행해도 작동한다.	

    5. python3 manage.py migrate blog 명령으로 DB에 적용
    * python3 manage.py migrate <app-name> -> 특정 앱에 대해 마이그레이션을 수행함
    * python3 manage.py migrate -> 모든 앱에 대해 마이그레이션을 추가함
    * '마이그레이션 파일(작업 지시서)'을 데이터베이스로 생성한다.

    blog/migrations/에 아래와 같은 파일들이 있다고 가정.

    0001_initial.py
    0002_blahblah.py 
    0003_blahblah.py
-> 0004_blahblah.py
    0005_blahblah.py
    0006_blahblah.py
    0007_blahblah.py

    blahblah 항목은 장고가 적절히 판단해서 넣는다. 0005~0007은 DB에 미적용된 상태 (번호는 순차적으로 증가한다.)
    현재는 0004 위치에 있음.

    python3 manage.py migrate blog 명령을 실행하면 0001_initial.py ~ 004_blahblah.py를 순차적으로 실행한다.
    현재 위치는 0004임. 0004에서 특정 필드를 지움. 0003으로 간다. 0003으로 가면 데이터 스키마를 복구할 뿐이지 데이터를 복구해주지는 않는다. DB는 항상 보수적으로 관리해야 한다.

    python3 manage.py migrate blog 0003이라고 하면 0004만 취소됨.
    마지막 마이그레이션이 0003이 되라고 하는 명령.
    python3 manage.py migrate blog 0002라고 하면 0004, 0003이 취소됨
    python3 manage.py migrate blog zero라고 하면 모든 작업이 취소된다.
	
    6. python3 manage.py showmigrations blog 명령으로 마이그레이션 현황 확인
    * python3 manage.py showmigrations <app-name>
    * 엑스표시는 마이그레이션이 적용되었다는 것이다.

    7. sqlite 브라우저를 통해 DB 테이블 확인
    * sqlite 브라우저 다운 -> http://sqlitebrowser.org/
    '''

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, 
        validators=[min_length_10_validator],
        help_text='10자 이상 입력해주세요.')
    '''
    CharField는 길이 제한이 있는 문자열이다.
    DB는 길이 제한이 있는 문자열을 빠르게 잘 찾아낼 수 있다.
    '''
    photo = models.ImageField(upload_to='blog/post/%Y/%m/%d') # ImageField()는 이미지만 저장할 수 있다.
    content = models.TextField(help_text='본문 내용을 입력해주세요.') # TextField는 길이 제한이 없는 문자열이다.
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True는 글을 포스팅할 때 '생성 시각'을 django가 자동으로 저장한다.
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True는 글의 '갱신 시각'을 django가 자동으로 저장한다.

    class Meta: 
        ''' 모델에 메타데이터를 추가할 수 있다.
        참고: https://docs.djangoproject.com/en/1.11/ref/models/options/#ordering
        '''
        ordering = ['-id']	# 역순으로 정렬한다. (최신 포스트를 상단에 배치)

    def __str__(self):
        '''오버라이딩을 안하면 관리자 페이지(http://192.168.0.17:8888/admin/blog/post/)에서 POST항목이 Post object라고만 출력된다.
        포스트들의 제목을 출력하기 위해서 아래와 같이 설정한다.
        '''
        return self.title

    def get_absolute_url(self):
        ''' 특정 모델에 대한 detail 뷰를 작성할 경우 detail 뷰에 대한 url 설정(urls.py)을 하자마자 get_absolute_url 설정을 한다.
        redirect에 인스턴스만 지정하면 코드가 간결하고 가독성이 좋아진다. (views.py의 post_new 함수 참고)
        '''
        return reverse('blog:post_detail', args=[self.id])
