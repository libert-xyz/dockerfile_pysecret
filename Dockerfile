FROM python:3.8.0-alpine3.10

COPY . .
CMD ["python", "secret_pass.py"]
