# Order is attempting to optimize for cache hit
FROM python:3.10-alpine
LABEL maintainer="Witt Allen @wittionary"
ADD requirements.txt /
RUN pip install -r requirements.txt


ADD scripts.json /
ADD app.py /
RUN chmod 644 app.py

EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]