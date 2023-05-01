# Use the official Node.js image as the base
FROM node:14

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the source code
COPY . .

# Expose the port the app runs on
EXPOSE 8084

# Start the app
CMD ["node", "server.js"]
