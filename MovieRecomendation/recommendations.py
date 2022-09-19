import requests
#class recon
class Recommendations():
   def __init__(self, movies_list, similarity, movies):
       self.movies_list = movies_list
       self.similarity = similarity
       self.movies = movies

   def fetch_poster(self, movie_id):
      self.response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
      data = self.response.json()
      return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

   def fetch_homepage(self, movie_id):
      self.response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
      data = self.response.json()
      return data['homepage']

   def fetch_overview(self, movie_id):
      self.response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
      data = self.response.json()
      return data['overview']

   def recommend(self, movie):
      movie_index = self.movies[self.movies['title'] == movie].index[0]
      distances = self.similarity[movie_index]
      movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:11]

      recommend_list = []
      recommend_posters = []
      recommend_homepage = []
      recommend_overview = []

      for i in movies_list:
         movie_id = self.movies.iloc[i[0]].movie_id
         recommend_list.append(self.movies.iloc[i[0]].title)
         # fetch poster from API
         recommend_posters.append(self.fetch_poster(movie_id))
         recommend_homepage.append(self.fetch_homepage(movie_id))
         recommend_overview.append(self.fetch_overview(movie_id))
      return recommend_list, recommend_posters, recommend_homepage, recommend_overview
   
   # TODO: NEED TO IMPROVE CODE
   def fetch_data(self, movie):
      movie_index = self.movies[self.movies['title'] == movie].index[0]
      distances = self.similarity[movie_index]
      movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:21]

      recommend_list = []
      recommend_posters = []
      recommend_homepage = []
      recommend_overview = []

      for i in movies_list:
         movie_id = self.movies.iloc[i[0]].movie_id
         recommend_list.append(self.movies.iloc[i[0]].title)
         # fetch poster from API
         recommend_posters.append(self.fetch_poster(movie_id))
         recommend_homepage.append(self.fetch_homepage(movie_id))
         recommend_overview.append(self.fetch_overview(movie_id))
      return recommend_list, recommend_posters, recommend_homepage, recommend_overview
