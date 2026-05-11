from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Flask automatically converts dictionaries to JSON
    return {"message": "Hello, World!"}


@app.route("/<trest>")
def hello_trest(trest):
    # Flask automatically converts dictionaries to JSON
    return {"message": f"Hello, {trest}!"}


if __name__ == "__main__":
    print("Solomon is Here")
    app.run(debug=True, host="0.0.0.0")
