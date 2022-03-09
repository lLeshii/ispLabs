FROM python:3.8-alpine

WORKDIR /app

COPY . .

CMD ["python", "lab1_isp.py"]