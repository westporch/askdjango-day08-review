from storages.backends.s3boto3 import S3Boto3Storage


class StaticS3Boto3Storage(S3Boto3Storage):
    '''StaticS3Boto3Storage 설명
    - python3 manage.py collectstatic 명령을 실행하면 AWS S3내 bucket/static 경로에 모든 static 파일 복사된다.
    - 모든 static 서빙 URL이 S3 bucket/static으로 지정
    '''
    location = 'static' # bucket 업로드 prefix 지정


class MediaS3Boto3Storage(S3Boto3Storage):
    '''MediaS3Boto3Storage 설명
    - 모든 파일 업로드가 bucket/media 경로에 저장된다.
    - 모든 media 서빙 URL이 S3 bucket/media로 지정
    - 기존 포스트에 올린 이미지 파일들은 DB에 경로만 저장되어 있다.
    - 이미지 파일을 다시 올리면 AWS S3로 업로드된다.
    '''
    location = 'media'  # bucket 업로드 prefix 지정