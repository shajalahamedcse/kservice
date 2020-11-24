FROM python:3.6.1-alpine
WORKDIR /project
ADD requirements.txt /project
RUN pip install -r requirements.txt
ADD ./src /project

EXPOSE 5000
CMD ["python","app.py"]