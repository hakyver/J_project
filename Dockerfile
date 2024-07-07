FROM python:3.12.3-bookworm
WORKDIR /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

ENTRYPOINT [ "gunicorn", "J_project.wsgi"]

#CMD [ "python3", "/home/david/aprendizaje/python/myvenv/mau4/J_project/manage.py", "runserver", "0.0.0.0:8000" ]
