# 📝 Notes Management App

A simple and production-ready **Flask Notes Management Application** built with **Python, Flask, SQLite, Docker, and AWS EC2**. This project demonstrates containerization, cloud deployment, and CRUD operations while following DevOps best practices.

---

## 🚀 Live Demo

🌐 **Application:** http://15.206.178.54

> *(Update this URL if your EC2 public IP changes.)*

---

## 📌 Features

- ✅ Create Notes
- ✅ View Notes
- ✅ Search Notes
- ✅ Edit Notes
- ✅ Delete Notes
- ✅ Health Check Endpoint
- ✅ SQLite Database
- ✅ Dockerized Application
- ✅ AWS EC2 Deployment
- ✅ Gunicorn Production Server

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Language |
| Flask | Web Framework |
| Flask-SQLAlchemy | ORM |
| SQLite | Database |
| Gunicorn | Production WSGI Server |
| Docker | Containerization |
| AWS EC2 | Cloud Deployment |
| Ubuntu | Linux Server |
| Git | Version Control |
| GitHub | Source Code Management |

---

## 📂 Project Structure

```
notes-devops-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
│
├── templates/
│   ├── index.html
│   └── edit.html
│
├── static/
│   └── style.css
│
└── instance/
    └── notes.db
```

---

## ⚙️ Local Setup

### Clone Repository

```bash
git clone https://github.com/Abhinavsingh6557/notes-devops-app.git

cd notes-devops-app
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t notes-devops-app .
```

## Run Docker Container

```bash
docker run -d \
--name notes-app \
-p 80:5000 \
-v notes-data:/app/instance \
notes-devops-app
```

Verify:

```bash
docker ps
```

---

# ☁️ AWS EC2 Deployment

Deployment Steps:

- Launch Ubuntu EC2 Instance
- Configure Security Groups (Ports 22 & 80)
- Install Docker
- Clone GitHub Repository
- Build Docker Image
- Run Docker Container
- Verify Deployment

Application becomes available at:

```
http://<EC2-Public-IP>
```

---

# ❤️ Health Check

Endpoint

```
/health
```

Example

```json
{
    "status":"healthy"
}
```

---

# 📷 Screenshots

## Home Page

> Add screenshot here

```
images/home.png
```

## Add Note

> Add screenshot here

```
images/add-note.png
```

## Search Notes

> Add screenshot here

```
images/search.png
```

## AWS EC2 Deployment

> Add screenshot here

```
images/ec2.png
```

## Docker Container

> Add screenshot here

```
images/docker.png
```

---

# 📈 Future Improvements

- GitHub Actions CI/CD
- Docker Compose
- Nginx Reverse Proxy
- HTTPS using Let's Encrypt
- Docker Hub Image Publishing
- Kubernetes Deployment
- Prometheus & Grafana Monitoring
- Terraform Infrastructure as Code

---

# 👨‍💻 Author

**Abhinav Singh**

MCA Graduate | DevOps & Cloud Enthusiast

GitHub

https://github.com/Abhinavsingh6557

LinkedIn

https://www.linkedin.com/in/abhinav-singh-6557/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to continue building and sharing more DevOps and Cloud projects.

---

## 📄 License

This project is licensed under the MIT License.
