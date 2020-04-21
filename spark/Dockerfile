# FROM bde2020/spark-python-template:2.4.5-hadoop2.7
# FROM python:3.8-slim-buster
# FROM openjdk <----------- new have not tried
FROM python:3.7-buster

WORKDIR /app

# RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
# RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
# RUN apt-get install software-properties-common
# RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update
RUN apt-get install -y default-jre
RUN apt-get install -y default-jdk
# RUN echo JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 >> /etc/environment
# RUN apt install openjdk-8-jdk
# RUN apt install openjdk-11-jdk
RUN pip install numpy scipy pandas matplotlib pyspark

COPY . /app

CMD sleep 86400
