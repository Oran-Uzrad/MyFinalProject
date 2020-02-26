"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MyFinalProject import app
from flask import request

import pandas as pd

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from MyFinalProject.Models.Forms import ExpandForm
from MyFinalProject.Models.Forms import CollapseForm



from os import path
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'The first argument to the field'


@app.route('/')
@app.route('/home')
def home():

    print("Home")

    """Renders the home page."""
    
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():

    print("Contact")

    """Renders the contact page."""

    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():

    print("About")

    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/data')
def data():

    print("Data")

    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='My data page.',
        img_trump = '/static/imgs/obama.jpg',
        img_obama = '/static/imgs/obama.jpg',
        img_bush = '/static/imgs/bush.jpg',
        img_clinton = '/static/imgs/clinton.jpg'
    )

@app.route('/project_resources')
def project_resources():

    print("Project Resources")

    """Renders the about page."""
    return render_template(
        'project_resources.html'
    )

@app.route('/hebrew_text')
def hebrew_text():
    """Renders the about page."""
    return render_template(
        'hebrew_text.html'
    )

@app.route('/data/trump' , methods = ['GET' , 'POST'])
def trump():

    print("Trump")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/trump.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'trump.html',
        title='Trump',
        year=datetime.now().year,
        message='My Trump page.',
        img_trump = '/static/imgs/trump.jpg',
        img_obama = '/static/imgs/trump.jpg',
        img_bush = '/static/imgs/trump.jpg',
        img_clinton = '/static/imgs/trump.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/tracking_changes')
def tracking_changes():

    print("Tracking Changes")

    """Renders the about page."""
    return render_template(
        'tracking_changes.html',
        title='Tracking changes to the site',
        year=datetime.now().year,
        message=''
    )
