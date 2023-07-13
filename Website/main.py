from flask import Flask , url_for , render_template
from Assets.Coffee import Coffees
from Assets.Tea import tea
from Assets.Juice import Juice
app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template('index.html',Coffees=Coffees)

@app.route('/tea')
def TeaPage():
    return render_template('tea_modal.html',tea=tea)

@app.route('/juice')
def JuicePage():
    return render_template('juice_modal.html',Juice=Juice)

with app.test_request_context():
    print(url_for('HomePage'))
    print(url_for('TeaPage'))
    print(url_for('JuicePage'))

if __name__ == '__main__':
    # flask --app Website/main.py run --debug
    app.run(debug=True)