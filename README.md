# django_react_starter
Example app for React django starter

Go to react path and change something then run this command 
```bash
cd react_app/
npm run build
```
You can run django in local
```bash
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
If you want to open swagger use go to http://localhost:8000/swagger/ 
Api path here http://localhost:8000/api/v1/example/
Other all path goes to react app. You can set other path by using react router insite react_app/ application. if you need development you can set prefix url like http://localhost:8000/api/v1/example in react_app.
