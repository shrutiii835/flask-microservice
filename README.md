# 🚀 Flask Microservice

A simple Flask-based microservice with Docker and CI integration.

## ⚙️ Run

```bash
pip install -r requirements.txt
python app.py
```

## 🐳 Docker

```bash
docker build -t flask-microservice .
docker run -p 5000:5000 flask-microservice
```

## 🧪 Test

```bash
pytest
```
