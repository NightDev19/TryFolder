from flask import Flask , url_for,render_template,request

app = Flask(__name__)
Pokemons = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff", 
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]

@app.route('/')
def index():
    return render_template('pokemon.html', len = len(Pokemons) ,Pokemons = Pokemons)

@app.route('/hello',methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
def do_the_login():
    return "Login!"
def show_the_login_form():
    return 'No Login Form!'

@app.route('/HTML')
@app.route('/HTML/<name>')
def HTML(name=None):
    return render_template('index.html', name=name)

@app.route('/user/<username>')
def profile(username):
    return f"{username}\'s profile"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('profile',username ="Sherwin"))

if __name__ == "__main__":
    #flask --app Flask||<Folder Name>/main||<filename> run --debug {too run in loop}
    app.run()