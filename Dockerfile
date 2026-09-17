FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu

EXPOSE 8080
CMD ["python3", "app.py"]
