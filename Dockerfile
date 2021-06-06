FROM python:3.9-alpine

RUN apk add curl

ENV  FLASK_APP="autodesk.app"
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# RUN pip3 install -e ./autodesk


COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]