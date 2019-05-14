import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    grad = "Zagreb"

    unit = "metric"

    apikey = "" # OVDJE IDE API KLJUČ OD OPENWEATHER STRANICE !!!

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("index.html", data=data.json())


if __name__ == '__main__':
    app.run()
