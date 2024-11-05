from flask import Flask,render_template
app = Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Frontend Developer',
        'location':'Delhi, India',
        'salary':'Rs. 5,00,000'
    },
    {
        'id':2,
        'title':'Backend Developer',
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000'
    },
    {
        'id':3,
        'title':'Data Analyst',
        'location':'West Bengal, India',
        'salary':'Rs. 8,00,000'
    },
    {
        'id':4,
        'title':'Machine Learning Engineer',
        'location':'Bengaluru, India',
        'salary':'Rs. 9,00,000'
    },
]
@app.route('/')
def hello_world():
    return render_template("home.html",jobs=JOBS)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)