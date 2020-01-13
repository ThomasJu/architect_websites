migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

server:
	python3 manage.py runserver

git:
	git add .
	git commit 
	git push