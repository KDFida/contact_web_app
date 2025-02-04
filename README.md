# Contact Manager

A basic Django-based contact management application.

## Prerequisites

- Python version 3 (min)
- pip
- (Optional) Virtual environment tool (e.g., `venv`)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kdfida/contact_web_app.git
   cd contact_web_app

2. **Set Up a Virtual Environment**
    - On macOS/Linux:
        ```bash 
        python3 -m venv env
        source env/bin/activate
    
    - On Windows:
        ```bash 
        python -m venv env
        env\Scripts\activate

3. **Install Dependecies**
    To install dependencies, run: 
    ```bash
    pip install -r requirements.txt

4. **Apply Database Migrations**
    ```bash 
    python manage.py migrate

5. **Running the Application Locally**
    Start the Django development server:
    ```bash 
    python manage.py runserver


## Deploying to Production
Before deploying, make sure to update Django settings:
    - Set DEBUG = False
    - Configure ALLOWED_HOSTS with your production domain(s)
    - Set up proper static files handling (e.g., using WhiteNoise or serving via a CDN)

You can also deploy this project to cloud platforms like AWS, GCP, Heroku, or Azure. For example, to deploy on AWS Elastic Beanstalk:
    - Install the AWS EB CLI.
    - Run eb init in your project root to configure your application.
    - Create an environment with eb create.
    - Deploy with eb deploy.