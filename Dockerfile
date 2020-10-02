FROM python:3.8.5
ENV FLASK_ENV=development
ENV FLASK_APP=main.app:init_app
ENV FLASK_NAME='Personal Data Integration'
ENV ENV_FOR_DYNACONF="DEVELOPMENT"
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mv .env-example .env
RUN flask db init && flask db migrate && flask db upgrade
RUN flask run