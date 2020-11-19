# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

RUN apt update
RUN apt install -y git python3-pip gunicorn3

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY app.py .

EXPOSE 8080

# command to run on container start
CMD ["python3", "app.py"]