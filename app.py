from flask import Flask

from app_kernel import create_app

# app = create_app()
app = Flask(__name__)




if __name__ == "__main__":
    print("Solomon is Here")
    app.run(debug=True, host="0.0.0.0")
