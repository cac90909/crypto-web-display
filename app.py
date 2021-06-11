from flask import Flask, render_template
import setup

app = Flask(__name__)

@app.route('/price')
def index():
    updated_prices = setup.get_prices()
    time = setup.get_time()
    return render_template('index.html', dict_prices = updated_prices, time=time, title='My portfolio')
    
if __name__ == '__main__':
    app.run(debug=True)