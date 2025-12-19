Secure Flask Application Deployment on AWS EC2

Overview
This project demonstrates the deployment of a Flask web application on AWS EC2 with a focus on secure backend practices and cloud deployment fundamentals. The application implements secure password handling and follows basic security best practices commonly used in production-ready systems.

--------------------------------------------------

Features
- Flask-based web application
- Secure user authentication using bcrypt password hashing
- Deployment on AWS EC2 (Linux)
- SSH-based server access using key authentication
- AWS Security Groups configured for restricted network access
- Clean and structured backend design

--------------------------------------------------

Tech Stack
- Programming Language: Python
- Framework: Flask
- Authentication Security: Flask-Bcrypt
- Cloud Platform: AWS EC2
- Operating System: Linux (Ubuntu)
- Tools: Git, GitHub, SSH

--------------------------------------------------

Project Structure

flask-aws-ec2/
- app.py
- requirements.txt
- README.md

--------------------------------------------------

How to Run Locally

Step 1: Clone the repository
git clone https://github.com/vigneshsai52/flask-aws-ec2.git
cd flask-aws-ec2

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Run the application
python app.py

Application runs at:
http://127.0.0.1:5000

--------------------------------------------------

Deployment on AWS EC2 (High-Level)
- Created an EC2 instance using Linux OS
- Configured inbound rules in Security Groups (SSH and application port)
- Connected to the server using SSH and PEM key
- Deployed and executed the Flask application on the EC2 instance
- Verified access using the public IP address

--------------------------------------------------

Security Practices
- Passwords are securely hashed using bcrypt
- SSH access secured with key-based authentication
- Network access restricted using AWS Security Groups
- Sensitive information not hardcoded in source code

--------------------------------------------------

Learning Outcomes
- Gained hands-on experience with AWS EC2
- Learned basic cloud deployment workflow
- Understood secure authentication handling
- Improved knowledge of Linux-based server environments
- Practiced deploying backend applications to the cloud

--------------------------------------------------

Author
Vignesh Sai
Software Engineering Student | Cloud & Security Enthusiast
GitHub: https://github.com/vigneshsai52
LinkedIn: https://www.linkedin.com/in/u-vignesh-sai-107336244
