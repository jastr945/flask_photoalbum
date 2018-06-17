FROM node:latest as builder

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# add environment variables
ARG REACT_APP_REDIRECT_URI
ARG REACT_APP_CLIENT_ID
ENV REACT_APP_REDIRECT_URI $REACT_APP_REDIRECT_URI
ENV REACT_APP_CLIENT_ID $REACT_APP_CLIENT_ID

# install and cache app dependencies
ADD package.json /usr/src/app/package.json
RUN npm install --silent
RUN npm install pushstate-server -g --silent
RUN npm install axios --save
RUN npm install react-timestamp
RUN npm install --save-dev url-loader file-loader
RUN npm install --save @researchgate/react-intersection-observer
RUN npm install --save react-bootstrap
RUN npm i react-loading
RUN npm install react-google-login

# add app
ADD . /usr/src/app

# build react app
RUN npm run build

# start app
FROM nginx
COPY --from=builder /usr/src/app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
