FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD app /code/
RUN python manage.py collectstatic -c --noinput
EXPOSE 8000
CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","SMCLauncher.gunicorn_wsgi"]
