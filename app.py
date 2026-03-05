from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/adventure')
def adventure():
    return render_template('adventure.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

@app.route('/simulation')
def simulation():
    return render_template('simulation.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
