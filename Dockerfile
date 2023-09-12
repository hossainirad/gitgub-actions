FROM python:3.11-alpine

# set work directory
WORKDIR /code

# copy project
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk del build-deps

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /code/entrypoint.sh

# echo workin user
RUN echo "Current user: $(whoami)"
# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
