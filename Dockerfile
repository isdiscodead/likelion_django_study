# 베이스 이미지 가져오기 -> Python 공식 이미지 ( dockerhub에 존재 )
FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/isdiscodead/likelion_django_study.git

WORKDIR /home/likelion_django_study/

# requirements에 있는 라이브러리들 모두 설치
RUN pip install -r requirements.txt

RUN pip install gunicorn

# 환경 변수 가져오기
RUN echo "SECRET_KEY=django-insecure-me&5g=_kl*c1okm22^&(=j02)i6&2tuhpu!au8%oi3b3+fwoxz" > .env

# db 연동
RUN python manage.py migrate

# collect static files
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "almighty.wsgi", "--bind", "0.0.0.0:8000"]