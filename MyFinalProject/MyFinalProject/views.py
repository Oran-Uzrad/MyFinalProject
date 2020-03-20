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
from MyFinalProject.Models.Forms import SinglePresidentForm
from MyFinalProject.Models.Forms import AllOfTheAboveForm
from MyFinalProject.Models.plot_service_functions import plot_case_1
from MyFinalProject.Models.plot_service_functions import plot_to_img
from MyFinalProject.Models.general_service_functions import htmlspecialchars

from wtforms.fields.html5 import DateField , DateTimeField

from os import path
import io

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

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
        img_american_flag = '/static/imgs/american_flag.jpg',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():

    print("Contact")

    """Renders the contact page."""

    return render_template(
        'contact.html',
        year=datetime.now().year,
        img_tichonet = '/static/imgs/tichonet.png',
        img_oran = '/static/imgs/oran.jpg'
    )

@app.route('/about')
def about():

    print("About")

    """Renders the about page."""
    return render_template(
        'about.html',
        year=datetime.now().year,
        img_tichonet = '/static/imgs/tichonet.png'
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
        img_trump = '/static/imgs/trump.jpg',
        img_obama = '/static/imgs/obama.jpg',
        img_bush = '/static/imgs/bush.jpg',
        img_clinton = '/static/imgs/clinton.jpg'
    )

@app.route('/query' , methods = ['GET' , 'POST'])
def query():

    print("Query")

    form1 = SinglePresidentForm()
    chart = {}
    height_case_1 = "100"
    width_case_1 = "250"

    df_trump = pd.read_csv(path.join(path.dirname(__file__), 'static/data/trump.csv'))
    df_obama = pd.read_csv(path.join(path.dirname(__file__), 'static/data/obama.csv'))
    df_bush = pd.read_csv(path.join(path.dirname(__file__), 'static/data/bush.csv'))
    df_clinton = pd.read_csv(path.join(path.dirname(__file__), 'static/data/clinton.csv'))
    presidents_dict = {'trump' : df_trump , 'obama' : df_obama , 'bush' : df_bush , 'clinton' : df_clinton }

    if request.method == 'POST':
        president = form1.president.data 
        start_date = form1.start_date.data
        end_date = form1.end_date.data
        kind = form1.kind.data
        height_case_1 = "300"
        width_case_1 = "750"

        print(president)
        print(start_date)
        print(end_date)
        print(type(start_date))
        x = str(start_date)
        print(x)
        chart = plot_case_1(presidents_dict[president] , start_date , end_date , kind)

    
    return render_template(
        'query.html',
        img_trump = '/static/imgs/trump.jpg',
        img_obama = '/static/imgs/obama.jpg',
        img_bush = '/static/imgs/bush.jpg',
        img_clinton = '/static/imgs/clinton.jpg',
        img_under_construction = '/static/imgs/under_construction.png',
        form1 = form1,
        src_case_1 = chart,
        height_case_1 = height_case_1 ,
        width_case_1 = width_case_1 ,
        code_ex_1 = '/static/imgs/code_ex_1.PNG'
    )

@app.route('/forms_demo' , methods = ['GET' , 'POST'])
def forms_demo():

    print("Forms Demo")

    form1 = AllOfTheAboveForm()
    

    if request.method == 'POST':
        s1 = form1.string_field_entry.data
        s2 = form1.text_area_field_entry.data
        s3 = form1.password_field_entry.data
        s4 = form1.date_field_entry.data
        s5 = form1.integer_field_entry.data
        s6 = form1.decimal_field_entry.data
        s7 = form1.boolean_field_entry.data
        s8 = form1.radio_field_entry.data
        s9 = form1.select_field_entry.data
        s10 = form1.select_field_multiple_entry.data

        t1 = str(type(s1))
        t2 = str(type(s2))
        t3 = str(type(s3))
        t4 = str(type(s4))
        t5 = str(type(s5))
        t6 = str(type(s6))
        t7 = str(type(s7))
        t8 = str(type(s8))
        t9 = str(type(s9))
        t10 = str(type(s10))
        
    else:
        s1 = 'GET Request'
        s2 = 'GET Request'
        s3 = 'GET Request'
        s4 = 'GET Request'
        s4 = 'GET Request'
        s5 = 'GET Request'
        s6 = 'GET Request'
        s7 = 'GET Request'
        s8 = 'GET Request'
        s9 = 'GET Request'
        s10 = 'GET Request'

        t1 = ''
        t2 = ''
        t3 = ''
        t4 = ''
        t5 = ''
        t6 = ''
        t7 = ''
        t8 = ''
        t9 = ''
        t10 = ''
      
        

    
    return render_template(
        'forms_demo.html',
        form1 = form1,
        
        s1 = s1 ,
        s2 = s2 ,
        s3 = s3 ,
        s4 = s4 ,
        s5 = s5 , 
        s6 = s6 ,
        s7 = s7 ,
        s8 = s8 , 
        s9 = s9 ,
        s10 = s10 , 

        t1 = t1 ,
        t2 = t2 ,
        t3 = t3 ,
        t4 = t4 ,
        t5 = t5 ,
        t6 = t6 ,
        t7 = t7 ,
        t8 = t8 ,
        t9 = t9 ,
        t10 = t10
    )

@app.route('/plot_demo' , methods = ['GET' , 'POST'])
def plot_demo():

    print("Plot Demo")

    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/time_series_2019-ncov-Confirmed.csv'))
    df = df.drop(['Lat' , 'Long' , 'Province/State'], 1)
    df = df.rename(columns={'Country/Region': 'Country'})
    df = df.groupby('Country').sum()
    df = df.loc[['Israel' , 'France' , 'Italy' , 'Spain' , 'United Kingdom']]
    df = df.transpose()
    df = df.reset_index()
    df = df.drop(['index'], 1)
    df = df.tail(30)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    df.plot(ax = ax , kind = 'line')
    chart = plot_to_img(fig)
    
    return render_template(
        'plot_demo.html',
        img_under_construction = '/static/imgs/under_construction.png',
        chart = chart ,
        height = "300" ,
        width = "750"
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
        message='Trump dataset page.',
        img_trump = '/static/imgs/trump.jpg',
        img_obama = '/static/imgs/trump.jpg',
        img_bush = '/static/imgs/trump.jpg',
        img_clinton = '/static/imgs/trump.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data/obama' , methods = ['GET' , 'POST'])
def obama():

    print("Obama")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/obama.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'obama.html',
        title='Obama',
        year=datetime.now().year,
        message='Obama dataset page.',
        img_trump = '/static/imgs/obama.jpg',
        img_obama = '/static/imgs/obama.jpg',
        img_bush = '/static/imgs/obama.jpg',
        img_clinton = '/static/imgs/obama.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data/bush' , methods = ['GET' , 'POST'])
def bush():

    print("Bush")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/bush.csv'), encoding = "utf-8")
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'bush.html',
        title='Bush',
        year=datetime.now().year,
        message='Bush dataset page.',
        img_trump = '/static/imgs/bush.jpg',
        img_obama = '/static/imgs/bush.jpg',
        img_bush = '/static/imgs/bush.jpg',
        img_clinton = '/static/imgs/bush.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data/clinton' , methods = ['GET' , 'POST'])
def clinton():

    print("Clinton")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/clinton.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'clinton.html',
        title='Clinton',
        year=datetime.now().year,
        message='Clinton dataset page.',
        img_trump = '/static/imgs/clinton.jpg',
        img_obama = '/static/imgs/clinton.jpg',
        img_bush = '/static/imgs/clinton.jpg',
        img_clinton = '/static/imgs/clinton.jpg',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/data/assignment_5130' , methods = ['GET' , 'POST'])
def assignment_5130():

    print("5130")

    return render_template(
        'assignment_5130.html',

    )

@app.route('/status')
def status():

    print("status")

    st = open(path.join(path.dirname(__file__), 'static/data/status.txt') , 'r' , encoding = 'utf-8').read()

    return render_template(
        'status.html'
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
