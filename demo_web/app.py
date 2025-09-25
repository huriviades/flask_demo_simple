from flask import Flask, render_template

app = Flask(__name__)

stores = [{"name": "New Store", "items": [{"name": "my item", "price": 14.49}]}]

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
