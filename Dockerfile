#FROM python:alpine
#
#WORKDIR /app
#COPY . /app
#
#RUN apt-get update -y && apt-get install -y \
#    python-pip python-dev build-essential && \
#    pip install -r requirements.txt
#
#ENTRYPOINT [ "python" ]
#
#EXPOSE 5000
#CMD [ "run.py" ]
FROM jfloff/alpine-python:3.6-onbuild

# for a flask server
EXPOSE 5000
CMD python run.py
