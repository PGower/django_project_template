FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
RUN mkdir /static
RUN mkdir /media
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD app /app/
RUN python manage.py collectstatic -c --noinput
EXPOSE 8000
CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","{{ project_name }}.gunicorn_wsgi"]
