from flask import Flask

from get_time import get_time

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return f"es ist aktuell {get_time(name='jonny ')}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
