FROM node:8.11.2-alpine as builder

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install -g @angular/cli@7.3.9

# add app
COPY . /app

# start app in development
# CMD ng serve --host 0.0.0.0

# Produciton Build
RUN cd /app && npm run build

FROM nginx:alpine

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From 'builder' copy website to default nginx public folder
COPY --from=builder /app/dist/demo /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]