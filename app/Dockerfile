FROM python:3.6
RUN apt-get update
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py", "0.0.0.0:5000"]
