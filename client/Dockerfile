FROM node:latest

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# add environment variables
ARG REACT_APP_ALBUMS_SERVICE_URL
ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
ENV REACT_APP_ALBUMS_SERVICE_URL $REACT_APP_ALBUMS_SERVICE_URL

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
CMD ["pushstate-server", "build"]
