# Use the official rust image as the base image
FROM rust

# Move to the app directory 
WORKDIR /usr/src/test_server

# Copy the app files to the container
COPY . .

# Activate nightly mode
RUN rustup install nightly

# Update the packages
RUN cargo update

# Compile the most optimized version of the app
RUN cargo install --path .

# Run the app
CMD ["test_server"]