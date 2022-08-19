import streamlit as st
import pickle
import pandas as pd
from PIL import Image
from recommendations import Recommendations

# Load data
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
image = Image.open('assets/logo.png')
 
# Declare Class
recommendations = Recommendations(movies_list, similarity, movies)

# Config Streamlit
st.set_page_config(page_title='Movies Recommender', page_icon=image, layout="wide")
hide_menu_style = '''
   <style>
      #MainMenu {display: none; }
      footer {visibility: hidden;}
      .css-fk4es0 {display: none;}
      #stStatusWidget {display: none;}
      .css-r698ls {display: none;}
   </style>
'''
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Design Web
st.title('Movie Recommendations')

selected_movies = st.selectbox(
   'Which movie do you want to recommend?', movies['title'].values
)

def title_movie(names):
   return st.markdown(f'''
   <h4 style="font-family:Consolas; font-size:1.5rem;">{names}</h4>
   ''', unsafe_allow_html=True)

def link_movie(homepage):
   return st.markdown(f'''
   __[Link Movie]({homepage})__
   ''')

names_list, posters_list, homepage, overview = recommendations.fetch_data('Avatar')

# Handle button
if st.button('Recommend'):
   names, posters, homepage, overview = recommendations.recommend(selected_movies)
   
   for i in range(0, 10):
      col, col1, col2 = st.columns(3)
      if i < 1:
         with col:
            title_movie(names[i])
            st.image(posters[i])
            link_movie(homepage[i])
            st.markdown(f'''
            {overview[i]}
            ''')
         with col1:
            title_movie(names[i + 1])
            st.image(posters[i + 1])
            link_movie(homepage[i + 1])
            st.markdown(f'''
            {overview[i + 1]}
            ''')
         with col2:
            title_movie(names[i + 2])
            st.image(posters[i + 2])
            link_movie(homepage[i + 2])
            st.markdown(f'''
            {overview[i + 2]}
            ''')
      elif i >= 1 and i < 2:
         with col:
            title_movie(names[i + 3])
            st.image(posters[i + 3])
            link_movie(homepage[i + 3])
            st.markdown(f'''
            {overview[i + 3]}
            ''')
         with col1:
            title_movie(names[i + 4])
            st.image(posters[i + 4])
            link_movie(homepage[i + 4])
            st.markdown(f'''
            {overview[i + 4]}
            ''')
         with col2:
            title_movie(names[i + 5])
            st.image(posters[i + 5])
            link_movie(homepage[i + 5])
            st.markdown(f'''
            {overview[i + 5]}
            ''')
      elif i >= 2 and i < 3:
         with col:
            title_movie(names[i + 5])
            st.image(posters[i + 5])
            link_movie(homepage[i + 5])
            st.markdown(f'''
            {overview[i + 5]}
            ''')
         with col1:
            title_movie(names[i + 6])
            st.image(posters[i + 6])
            link_movie(homepage[i + 6])
            st.markdown(f'''
            {overview[i + 6]}
            ''')
         with col2:
            title_movie(names[i + 7])
            st.image(posters[i + 7])
            link_movie(homepage[i + 7])
            st.markdown(f'''
            {overview[i + 7]}
            ''')

else:
   for i in range(0, 10):
      col, col1, col2 = st.columns(3)
      if i < 1:
         with col:
            title_movie(names_list[i])
            st.image(posters_list[i])
            link_movie(homepage[i])
            st.markdown(f'''
            {overview[i]}
            ''')
         with col1:
            title_movie(names_list[i + 1])
            st.image(posters_list[i + 1])
            link_movie(homepage[i + 1])
            st.markdown(f'''
            {overview[i + 1]}
            ''')
         with col2:
            title_movie(names_list[i + 2])
            st.image(posters_list[i + 2])
            link_movie(homepage[i + 2])
            st.markdown(f'''
            {overview[i + 2]}
            ''')
      elif i >= 1 and i < 2:
         with col:
            title_movie(names_list[i + 3])
            st.image(posters_list[i + 3])
            link_movie(homepage[i + 3])
            st.markdown(f'''
            {overview[i + 3]}
            ''')
         with col1:
            title_movie(names_list[i + 4])
            st.image(posters_list[i + 4])
            link_movie(homepage[i + 4])
            st.markdown(f'''
            {overview[i + 4]}
            ''')
         with col2:
            title_movie(names_list[i + 5])
            st.image(posters_list[i + 5])
            link_movie(homepage[i + 5])
            st.markdown(f'''
            {overview[i + 5]}
            ''')
      elif i >= 2 and i < 3:
         with col:
            title_movie(names_list[i + 5])
            st.image(posters_list[i + 5])
            link_movie(homepage[i + 5])
            st.markdown(f'''
            {overview[i + 5]}
            ''')
         with col1:
            title_movie(names_list[i + 6])
            st.image(posters_list[i + 6])
            link_movie(homepage[i + 6])
            st.markdown(f'''
            {overview[i + 6]}
            ''')
         with col2:
            title_movie(names_list[i + 7])
            st.image(posters_list[i + 7])
            link_movie(homepage[i + 7])
            st.markdown(f'''
            {overview[i + 7]}
            ''')
      elif i >= 3 and i < 4:
         with col:
            title_movie(names_list[i + 8])
            st.image(posters_list[i + 8])
            link_movie(homepage[i + 8])
            st.markdown(f'''
            {overview[i + 8]}
            ''')
         with col1:
            title_movie(names_list[i + 9])
            st.image(posters_list[i + 9])
            link_movie(homepage[i + 9])
            st.markdown(f'''
            {overview[i + 9]}
            ''')
         with col2:
            title_movie(names_list[i + 10])
            st.image(posters_list[i + 10])
            link_movie(homepage[i + 10])
            st.markdown(f'''
            {overview[i + 10]}
            ''')


# Footer
st.markdown('''
   #### Created by __[Guanyu Zhou,Chunwang Yuan]
   <style>
      a {
         text-decoration: none;
         color: #4b6cff;
      }
   </style>
''', unsafe_allow_html=True)