# Use the official nginx image as the base image
FROM nginx

# Expose port 8080 internally 
EXPOSE 8080

# Remove the default nginx configuration file
RUN rm /etc/nginx/conf.d/*

# Copy the custom nginx configuration file to the container
COPY nginx.conf /etc/nginx/conf.d/

# Copy the first web page files to the container
COPY small/index.html /usr/share/nginx/html/small/
COPY large/index.html /usr/share/nginx/html/large/