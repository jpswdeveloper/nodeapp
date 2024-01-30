FROM node:21-alpine

WORKDIR /react_app

COPY ./package.json .

COPY  . .

RUN npm install

EXPOSE 3000

CMD [ "npm","start" ]
