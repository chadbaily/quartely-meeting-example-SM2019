pip install --upgrade -r requirements.txt && python manage.py makemigrations modelsExample && python manage.py migrate modelsExample && python manage.py makemigrations && python manage.py migrate && mod_wsgi-express start-server --working-directory ./ --reload-on-changes ./models/wsgi.py