# AskDjango Day8 오프라인 강의 복습

## 강의

날짜: 2017.07.30(일) 12:30 ~ 17:00

장소: [토즈 강남토즈타워점](http://map.naver.com/?mapmode=0&lng=3c377659a701511a2208c6b852917141&pinId=21660996&lat=e6207796f2b06b3f9e609f8d8d75c103&dlevel=11&enc=b64&pinType=site)

## 수업 내용

### Amazon S3 (Simple Storage Service)에 파일 저장

설정 몇 개만 바꾸시면, 업로드된 파일저장을 로컬디스크가 아닌 아마존 인프라에 안전하게 저장하실 수 있습니다.

### 페이스북/카카오/네이버 로그인

요즘 서비스 중에 페이스북/카카오/네이버 로그인을 지원하지 않는 서비스가 있나요? ㅎㅎ 없죠? 장고에서도 django-allauth 라이브러리를 통해 다른 OAuth Proider와 인증을 연동해봅시다.

### 서비스 배포

다 만들었으면, 이제 실제 서버에 올려봐야겠죠? 여러분의 서비스를 지인들과 공유할 시간입니다. :)


## 버전

python v3.5

virtualenv v15.1.0

### Python 라이브러리 버전

참고: [requirements.txt](https://github.com/westporch/askdjango-day08-review/blob/master/dev/askdjango/requirements.txt)

### 사용 방법

```
# git clone https://github.com/westporch/askdjango-day08-review.git
# cd askdjango-day08-review
# rm -rf myenv
# virtualenv --python=python3.5 myenv
# source askdjango-day08-review/myenv/bin/activate
(myenv) # pip3 install -r askdjango-day08-review/dev/askdjango/requirements.txt
```
