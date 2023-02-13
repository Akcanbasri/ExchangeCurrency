import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
user_rating = float(input("Enter Rating: "))


names = soup.find_all("td", {"class": "titleColumn"})
ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

for name, rating in zip(names, ratings):
    name = name.text
    rating = rating.text

    name = name.strip()
    name = name.replace("\n", "")

    rating = rating.strip()
    rating = rating.replace("\n", "")

    if float(rating) > user_rating:
        print("Name of film: {}  Rating of film {}".format(name, rating))