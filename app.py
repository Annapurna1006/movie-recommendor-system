import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    moviei = movies[movies['title'] == movie].index[0]
    distances = similarity[moviei]
    moviesl = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies = []
    for i in moviesl:
        moviei = [0]
        #fetch poster from API
        recomended_movies.append(movies.iloc[i[0]].title)
    return recomended_movies

moviesl = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(moviesl)
moviesl = moviesl['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
option = st.selectbox(
    "How would you like to be contacted?",
    (moviesl
))


if st.button("Recommend"):
   recommendations = recommend(option)
   for i in recommendations:
    st.write(i)
