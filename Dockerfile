FROM python:3.12

COPY . .
WORKDIR .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]