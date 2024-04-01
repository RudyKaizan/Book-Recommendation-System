from flask import Flask,render_template,request
import pickle

popular_books = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
sim_score = pickle.load(open('sim_score.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))



app = Flask(__name__,template_folder = 'templates', static_folder = 'static')
@app.route('/')
def index():
    return render_template('index.html',book_name = list(popular_books['Book-Title'].values),
                                        author = list(popular_books['Book-Author'].values),
                                        image = list(popular_books['Image-URL-M'].values),
                                        votes = list(popular_books['Num-ratings'].values),
                                        rating = list(popular_books['Avg-ratings'].values),)

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    return str(user_input)

if __name__ == '__main__':
    app.run(debug=True)