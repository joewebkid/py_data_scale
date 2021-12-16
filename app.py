from flask import Flask, render_template
import gunicorn

from modules.api_func.mongo_api import apiMongoConnect

app = Flask(__name__, template_folder="templates")
app.debug = True


@app.route('/')
def hello_world():

    dt = apiMongoConnect.req()
    dt_json = dt.json()
    content = dt_json['documents']
    return render_template('base.html', data=content)