# This is the instruction to spin up the docker test environement : 

# Run this command in the current directory to build the custom image. 
$ docker build -t nodetestenv .

# Run this command in the current directory to start the container. 
$ docker run -it --rm -d -p 8084:8084 --name node nodetestenv

# Go to http://localhost:8084/small.html to access the small web page.
# Go to http://localhost:8084/large.html to access the large web page.