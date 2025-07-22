from flask import Flask, render_template, request
import requests
import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    breweries = []
    city = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f"{config.API_BASE_URL}?by_city={city.lower()}"
            response = requests.get(url)
            if response.ok:
                breweries = response.json()
    return render_template("index.html", breweries=breweries, city=city)

if __name__ == '__main__':
    app.run(debug=True)
