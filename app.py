from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import gunicorn

app = Flask(__name__, template_folder="templates")
app.debug = True


@app.route('/')
def hello_world():
    response = requests.get('https://rifmu.ru/'+"кот")
    contents_html = response.content

    soup = BeautifulSoup(contents_html, 'lxml')
    text_arr = []

    for child in soup.ul.recursiveChildGenerator():

        if child.name == 'a':

            text_arr.append(child.text)

    return {"data": text_arr}
