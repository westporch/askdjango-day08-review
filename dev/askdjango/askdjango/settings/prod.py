from .common import *

import pymysql
pymysql.install_as_MySQLdb()

INSTALLED_APPS += ['storages']

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'USER': os.environ.get('DATABASE_USER'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
    },
}

STATICFILES_STORAGE = 'askdjango.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'askdjango.storages.MediaS3Boto3Storage'

'''AWS 설정
1. 쉘 환경 변수 등록
~/.zshrc에 아래 내용을 추가한다.
export AWS_ACCESS_KEY_ID=값 입력
export AWS_SECRET_ACCESS_KEY=값 입력
export AWS_STORAGE_BUCKET_NAME=값 입력
export AWS_S3_REGION_NAME=값 입력
2. 적용
source ~/.zshrc 실행
3. python3 콘솔에서 적용한 환경 변수 확인
python3 콘솔 실행후 아래 명령 입력
import os
print(os.environ)
'''
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']