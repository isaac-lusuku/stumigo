bind = '127.0.0.1:8000'  # The IP address and port for your local server
workers = 2  # The number of worker processes to run Gunicorn
chdir = '"C:\Users\Administrator\Desktop\stumigo"'  # Replace with the actual path to your Django project
module = 'stumigo.wsgi:application'  # Replace 'your_project_name' with your Django project's name
