FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

COPY requirements.txt /Resume/requirements.txt
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r /Resume/requirements.txt

COPY package.json /Resume/package.json
COPY package-lock.json /Resume/package-lock.json
COPY webpack.config.js /Resume/webpack.config.js
WORKDIR /Resume
RUN apk add --no-cache nodejs npm
RUN npm install

COPY . /Resume/
RUN ./node_modules/.bin/webpack
WORKDIR /
CMD uvicorn Resume.main:app --host 0.0.0.0
