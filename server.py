from flask import Flask, render_template
import random as rm
from datetime import datetime
import requests

GENDER_API_ENDPOINT = "https://api.genderize.io"
AGE_API_ENDPOINT = "https://api.agify.io"

app =Flask(__name__)


@app.route('/')
def home():
    random_number= rm.randint(1,10)
    curr_year = datetime.today().year
    my_name = "Jashan Aneja"
    return render_template("index.html", num = random_number ,current_year =curr_year , name = my_name)

@app.route('/guess/<name>/')
def guess(name):
    params = {
    "name" : name
    }
    response = requests.get(GENDER_API_ENDPOINT ,params= params)
    response2 = requests.get(AGE_API_ENDPOINT ,params = params)

    data = response.json()
    name2 = data["name"]
    gender =data["gender"]

    data2 = response2.json()
    age = data2["age"]
    return render_template("index2.html" ,name = name2 , age = age , gender = gender)



if __name__ == "__main__":
    app.run(debug=True)