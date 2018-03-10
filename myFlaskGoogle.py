from flask import Flask

from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_api import status
import config
from urllib.request import urlopen
import json


app = Flask(__name__)
config_object = config.DevelopmentConfig
app.config.from_object(config_object)


@app.route('/')
def main_page():
    #return render_template("index.html", title=app.config["APP_TITLE"], map_key=app.config["GOOGLE_MAP_KEY"])

    f = urlopen('http://api.wunderground.com/api/b27dbdfdaafdef52/geolookup/conditions/q/MN/Minneapolis.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    temp_f = parsed_json['current_observation']['temp_f']
    feelslike_f = parsed_json['current_observation']['feelslike_f']
    weather = parsed_json['current_observation']['weather']
    visibility_mi = parsed_json['current_observation']['visibility_mi']
    pressure_in = parsed_json['current_observation']['pressure_in']
    wind_dir = parsed_json['current_observation']['wind_dir']
    wind_string = parsed_json['current_observation']['wind_string']
    f.close()

    return render_template('index.html', title=app.config["APP_TITLE"], map_key=app.config["GOOGLE_MAP_KEY"],
                            temp_f=temp_f, feelslike_f=feelslike_f, weather=weather, visibility_mi=visibility_mi,
                            pressure_in=pressure_in, wind_dir=wind_dir, wind_string=wind_string)


if __name__ == '__main__':
    app.run(debug=True)
