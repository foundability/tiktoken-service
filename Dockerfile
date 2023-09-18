FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app files to the container
COPY src/app.py ./src/

# Install the required dependencies
RUN pip install flask tiktoken

# Set the Flask app environment variable
ENV FLASK_APP=src/app.py

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "src/app.py"]
