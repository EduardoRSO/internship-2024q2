# Use the official AWS Lambda Python 3.10 image as the base image
FROM public.ecr.aws/lambda/python:3.10

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the CMD to your main function (assumed to be main.py)
CMD ["main.handler"]
