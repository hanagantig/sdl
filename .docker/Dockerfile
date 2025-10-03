FROM python:3.6.9-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN \
 apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl && \
 apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install --upgrade pip setuptools && \
 python3 -m pip install setuptools==45 && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
# python3 -m pip install psycopg2 && \
 apk --purge del .build-deps && \
 apk add terminus-font && \
 apk add --no-cache wkhtmltopdf && \
 fc-cache -fv


#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

# copy projecd
COPY . /usr/src/app/

#CMD ./manage.py runserver

#RUN ./manage.py loaddata db.json
