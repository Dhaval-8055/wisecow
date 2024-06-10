# Use a base image that has Bash and netcat (nc) installed
FROM alpine:latest

# Install cowsay and fortune
RUN apk update && \
    apk add --no-cache bash coreutils cowsay fortune

# Set environment variables
ENV SRVPORT=4499 \
    RSPFILE=response

# Set working directory
WORKDIR /app

# Copy the script into the container
COPY wisecow.sh .

# Make the script executable
RUN chmod +x wisecow.sh

# Expose the port
EXPOSE $SRVPORT

# Run the script when the container starts
CMD ["./wisecow.sh"]
