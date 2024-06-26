# Library management system

## How to run the code

First clone the repository.

```bash
git clone https://github.com/asifrahaman13/library-management.git
```

## Backend
Open the backend in a terminal.

```bash
cd backend/
```

Create virtual environment and install the dependencies.

```bash
virtualenv .venv
```

Activate the virtual environment

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Now change the .env.example to .env file enter the required data in the .env file.
```bash
mv .env.example .env
```

Run the backend in port 8000

```bash
uvicorn src.main:app --reload
```
# Want to run in docker?
In case you are facing any issue and want to run the application using docker.

First build the image

```bash
docker -t build backend:latest .
```

Next you can simply run the application.

```bash 
docker run -d -p  8000:8000 backend:latest
```


# Link to the documentation for the APIs:

https://docs.google.com/document/d/12-ozqYCtt2LpQUaTKo49m8-zx0tKBzRB5VM0c-0-TqY/edit?usp=sharing


# Testing

Simple Pytest scripts are written for sample unit and integration testing. Follows the official fast api documentation:
https://fastapi.tiangolo.com/tutorial/testing/

To test the application use the following script: 

```bash
python3 -m pytest
```
