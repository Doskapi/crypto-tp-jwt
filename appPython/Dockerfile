FROM python:2.7.12

# Create app directory
WORKDIR /code

# Geting the code from current directory
COPY . .

# Install app dependencies
RUN pip install -r requirements.txt

# Open 4000 port.
EXPOSE 4000

