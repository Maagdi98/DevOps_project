# Use the official Nginx image as the base
FROM nginx:latest

# Copy custom Nginx configuration file to the appropriate directory in the container
COPY nginx.conf /etc/nginx/nginx.conf

# Optionally, copy additional files if needed (e.g., SSL certificates, custom error pages)
# COPY ssl/cert.pem /etc/nginx/ssl/cert.pem
# COPY ssl/key.pem /etc/nginx/ssl/key.pem

# Expose the default HTTP port
EXPOSE 80
# Optionally, expose the HTTPS port if SSL is configured
# EXPOSE 443

# Start Nginx (Nginx runs as the main process by default in the official image)
