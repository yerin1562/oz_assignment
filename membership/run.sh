#!/bin/bash

# 1. install git, python 3.12
sudo yum update -y
sudo yum install -y git python3.12 

# python version
python3.12 --version

# 2. git clone
REPO_URL="https://github.com/Samiiz/djtest.git" # 내거 넣어라 
echo "Cloning repository..."
git clone $REPO_URL
REPO_NAME=$(basename "$REPO_URL" .git)
cd $REPO_NAME

# 3. virtual environment setting
echo "Creating and activating Python virtual environment..."
python3.12 -m venv .venv
source .venv/bin/activate

# 4. install pkages
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping package installation."
fi

# 5. Django initialization
if [ -f "manage.py" ]; then
    echo "Running Django migrations and server setup..."

    # db migration
    python manage.py makemigrations
    python manage.py migrate

    # create super user
    echo "Creating superuser..."
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', '1234')" | python manage.py shell

    # django runserver
    python manage.py runserver 0.0.0.0:8000
else
    echo "manage.py not found. Please check your Django project structure."
fi

# 6. complate
echo "Django development server is running"
