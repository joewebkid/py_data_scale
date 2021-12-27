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

@app.route('/p/<post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    dt = apiMongoConnect.req(method_name="findOne",method_type="POST",add_data={"filter": { "_id": { "$oid": post_id } }})
    dt_json = dt.json()
    content = dt_json['documents'][0]
    return render_template('page.html', data=content)
