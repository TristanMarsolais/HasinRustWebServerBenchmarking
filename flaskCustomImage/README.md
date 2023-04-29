# This is the instruction to spin up the docker test environement : 

# Run this command in the current directory to build the custom image. 
$ docker build -t flasktestenv .

# Run this command in the current directory to start the container. 
$ docker run -it --rm -d -p 8081:8081 --name flask flasktestenv

# Go to http://localhost:8081/small/ to access the small web page.
# Go to http://localhost:8081/large/ to access the large web page.