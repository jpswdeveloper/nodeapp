# access node image library from docker hub
# set your working directort
# Copy all contents 
# Run command to start node project
# Expose container port computer machine on || to access it locally

FROM node:21-alpine
WORKDIR  /app
# copy all files to working /app
Copy . .
# Install packages
RUN npm install 
# Expose container port make it public to localmachine
Expose 4000
# Run command
CMD ['node','app/index.js']

