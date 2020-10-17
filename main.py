from flask import Flask, render_template


app = Flask('flasksample')
app.config.from_object('config')

@app.route('/', methods=['GET'])
def flasksample_root():
    return render_template('index.html')


