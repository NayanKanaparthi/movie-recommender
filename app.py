import streamlit as st
import pickle 
import requests
import os
# st.set_page_config(
#     page_title="Movie recommender",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     bg_color="#AEDFE7"  # Set your desired background color using a hex code
# )

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c0276ba29a6cf75accee65eec3844f9b".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommended(selected_movie):
    index = movies[movies['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies_names=[]
    recommended_movies_poster=[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies.iloc[i[0]].title)
    return recommended_movies_names, recommended_movies_poster



st.header("Movie Recommender")


movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

movies_list = movies['title'].values
movie_user_likes = st.selectbox('What kind of movie would you like to watch?',movies_list)

if st.button("Let's GO"):
    recommended_movies_names, recommended_movies_poster= recommended(movie_user_likes)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_names[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies_names[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_names[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_names[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies_names[4])
        st.image(recommended_movies_poster[4])



