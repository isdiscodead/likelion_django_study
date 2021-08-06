# 베이스 이미지 가져오기 -> Python 공식 이미지 ( dockerhub에 존재 )
FROM python:3.9.0

WORKDIR /home/

RUN echo "testing..."

RUN git clone https://github.com/isdiscodead/likelion_django_study.git

WORKDIR /home/likelion_django_study/

# requirements에 있는 라이브러리들 모두 설치
RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install psycopg2

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=almighty.settings.deploy && python manage.py migrate --settings=almighty.settings.deploy && gunicorn almighty.wsgi --env DJANGO_SETTINGS_MODULE=almighty.settings.deploy --bind 0.0.0.0:8000"]