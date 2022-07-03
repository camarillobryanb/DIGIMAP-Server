from flask import Flask

urls = ("/favicon.ico", "dummy")

app = Flask(__name__)

@app.route('/')
@app.route('/api', methods=['GET'])
def server():
    return {
        "tutorial": "Flask React Heroku "
    }

if __name__ == '__main__':
    app.run()