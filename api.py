from abc import ABCMeta, abstractmethod
import requests

class API_consumer(metaclass=ABCMeta):
   @abstractmethod
   def extract(self, id):
       pass

class API_Pokemon(API_consumer):
   def __init__(self):
       self.__URL = 'https://pokeapi.co/api/v2/pokemon/'
   @property
   def URL(self):
       return self.__URL
   def extract(self, id):
       URL = self.URL + str(id)
       try:
           response = requests.get(URL)
           response.raise_for_status()
           data = response.json()
           return (data.get('id'), data.get('name'))
       except requests.exceptions.RequestException as e:
           print(f'Erro ao acessar API Pokemon: {e}')
           return None //aqui fazemos o consumo de api pokemon

class API_Rick_Morty(API_consumer):
   def __init__(self):
       self.__URL = 'https://rickandmortyapi.com/api/character/'
   @property
   def URL(self):
       return self.__URL
   def extract(self, id):
       URL = self.URL + str(id)
       try:
           response = requests.get(URL)
           response.raise_for_status()
           data = response.json()
           return (data.get('id'), data.get('name'), data.get('species'))
       except requests.exceptions.RequestException as e:
           print(f'Erro ao acessar API Rick and Morty: {e}')
           return None  // aqui fazemos o consumo de api rick and morty

class API_Star_Wars(API_consumer):
   def __init__(self):
       self.__URL = 'https://swapi.dev/api/people/'
   @property
   def URL(self):
       return self.__URL
   def extract(self, id):
       URL = self.URL + str(id)
       try:
           response = requests.get(URL)
           response.raise_for_status()
           data = response.json()
           return (data.get('name'), data.get('films'))
       except requests.exceptions.RequestException as e:
           print(f'Erro ao acessar API Star Wars: {e}')
           return None // aqui fazemos o consumo de api de star wars

class API_Ice_and_Fire(API_consumer):
   def __init__(self):
       self.__URL = 'https://anapioficeandfire.com/api/characters/'
   @property
   def URL(self):
       return self.__URL
   def extract(self, id):
       URL = self.URL + str(id)
       try:
           response = requests.get(URL)
           response.raise_for_status()
           data = response.json()
           return (data.get('name'), data.get('tvSeries'))
       except requests.exceptions.RequestException as e:
           print(f'Erro ao acessar API Crônicas de Gelo e Fogo: {e}')
           return None
