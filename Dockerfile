# Use nginx as the base image for serving static files
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy all static files to the nginx html directory
COPY . .

# Remove the default nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/

# Expose port 80
EXPOSE 80

# Start nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
