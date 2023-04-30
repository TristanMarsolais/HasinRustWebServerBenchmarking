# This is the instruction to spin up the docker test environement : 

# Run this command in the current directory to build the custom image. 
$ docker build -t rusttestenv .

# Run this command in the current directory to start the container. 
$ docker run -it --rm -d -p 8083:8083 --name rust rusttestenv

# Go to http://localhost:8083/small.html to access the small web page.
# Go to http://localhost:8083/large.html to access the large web page.