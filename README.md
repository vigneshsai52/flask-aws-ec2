# 🚀 Secure Flask App on AWS EC2

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20S3-orange?logo=amazonaws)
![Security](https://img.shields.io/badge/Security-Bcrypt%20Auth-success)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight **Flask web application** deployed securely on **AWS EC2** with **bcrypt authentication** and **S3 integration** for optimized static content delivery.

---

## 📋 Project Overview

This project demonstrates building and deploying a **secure Flask application** on AWS EC2.  
It implements **Flask-Bcrypt** for password hashing to protect user data and mitigate risks like SQL injection and brute-force attacks.

### 🔑 Key Features
- Secure login & signup with **bcrypt** password hashing  
- Deployed on **AWS EC2 (Ubuntu/Linux)**  
- Static file optimization using **AWS S3**  
- **Security Groups** configured for restricted network access  
- Load time improved by **~15%** through S3 caching  

---

## 🧰 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Backend** | Python (Flask Framework) |
| **Authentication** | Flask-Bcrypt |
| **Cloud Platform** | AWS EC2, AWS S3 |
| **OS** | Linux (Ubuntu 22.04) |
| **Version Control** | Git & GitHub |

---

## 🏗️ Project Structure

flask-aws-ec2/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── static/ # (Optional) Static files from S3


---

## ⚙️ Setup & Run Locally

```bash
# Clone the repository
git clone https://github.com/vigneshsai52/flask-aws-ec2.git
cd flask-aws-ec2

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py

Then visit → http://localhost:5000
☁️ Deploying to AWS EC2
Step 1️⃣ — Launch EC2 Instance

Choose Ubuntu 22.04 LTS

Configure Security Groups:

Allow inbound 22 (SSH) and 5000 (Flask app)

Step 2️⃣ — Connect via SSH
ssh -i "your-key.pem" ubuntu@<EC2-Public-IP>

Step 3️⃣ — Set Up Environment
sudo apt update
sudo apt install python3-pip git -y
git clone https://github.com/vigneshsai52/flask-aws-ec2.git
cd flask-aws-ec2
pip3 install -r requirements.txt
python3 app.py

Step 4️⃣ — Access the App

Visit your browser at:
http://<EC2-Public-IP>:5000
