import pandas as pd
from flask import Flask, render_template, request
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['POST'])
def process_form():
    activity = request.form['activity']
    os.system(f"python get_activities.py {activity}")
    reward = pd.read_csv("data/rewards.csv", index_col=[0])
    
    
    return render_template('form.html',  tables=[reward.to_html(classes='data')], titles=reward.columns.values)



if __name__ == '__main__':
    app.run()
