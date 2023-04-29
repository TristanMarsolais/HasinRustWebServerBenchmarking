# This is the instruction to spin up the docker test environement : 

# Run this command in the current directory to build the custom image. 
$ docker build -t nginxtestenv .

# Run this command in the current directory to start the container. 
$ docker run -it --rm -d -p 8080:8080 --name nginx nginxtestenv

# Go to http://localhost:8080/small/ to access the small web page.
# Go to http://localhost:8080/large/ to access the large web page.