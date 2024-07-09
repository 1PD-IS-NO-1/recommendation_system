from flask import Flask, request, render_template, redirect, url_for
import pickle

app = Flask(__name__)

# Load your data and similarity matrix
new_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [new_df.iloc[i[0]].title for i in movie_list]
    return recommended_movies

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend_movie():
    movie_name = request.args.get('movie')
    recommendations = recommend(movie_name)
    return render_template('recommendations.html', movie=movie_name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)


