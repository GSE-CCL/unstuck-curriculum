#Builds a Docker image to serve the Getting Unstuck site. 

FROM node:14 as builder

WORKDIR /build
COPY . /build

RUN npm install -g sass@1.35.1
RUN npm install --unsafe-perm

RUN make 

FROM python:3.9.6 as app

#install app dependencies
WORKDIR /app
COPY --from=builder /build/app /app

COPY requirements.txt /tmp
RUN  pip3 install -r /tmp/requirements.txt 

#set the default entry point
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "3", "wsgi:app"]
