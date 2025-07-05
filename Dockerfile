FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN make install

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
