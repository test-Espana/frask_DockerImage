FROM python:3.10.6
WORKDIR /code/app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt . 
COPY app .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# COPY . .
# CMD ["flask", "run"]