FROM python:3.9

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt --no-cache-dir

COPY . /code/

ENV FLASK_CONFIG development
# ENV FLASK_APP wsgi.py

# Development environment configuration
ENV FLASK_APP run.py
ENV FLASK_ENV development
CMD flask run --host=0.0.0.0
 