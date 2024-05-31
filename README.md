# madhundle.com

## Development
```
. venv/bin/activate
[sudo] apt install python3-flask | pip install flask
[sudo] pip install flask_mail
export FLASK_APP=madhundle
export FLASK_ENV=development
flask run | python app.py
```

## Deployment
```
gcloud app deploy
```