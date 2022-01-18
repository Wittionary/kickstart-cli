# kickstart-cli
Start pre-defined scripts and programs on your home infrastructure via CLI.

Get started by running the server locally with
```shell
# Windows
set FLASK_APP=app.py
flask run

# Linux
export FLASK_APP=app.py
flask run
```
or via docker
```shell
docker image build -t kickstart-server .
docker run kickstart-server
```

Setup the CLI with
```shell
# Windows
virtualenv venv
.\venv\Scripts\activate
pip install --editable .

# Linux
virtualenv venv
.\venv\bin\activate
pip install --editable .
```

Run your first command
```shell
ks ls
```