# access node image library from docker hub
# set your working directort
# Copy all contents 
# Run command to start node project
# Expose container port computer machine on || to access it locally

FROM node:21-alpine
WORKDIR  /app
#  copy package json .
COPY ./package.json .
RUN npm install 
# copy all files to working /app
COPY  . .
# Install packages
# Expose container port make it public to localmachine
EXPOSE 4000
# Run command
CMD ["npm","start"] 

