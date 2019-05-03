import requests
from bs4 import BeautifulSoup
import os


class Rater:
    """ Takes a movie title and then search www.rottentomatoes.com for that
    movie's ratings.
    """
    def __init__(self, movie):
        self.movie = movie
        self.page = requests.get('https://www.rottentomatoes.com/m/' + self.movie)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def rating(self):
        """
        The information of the box containg the relevant information has been
        isolated (Tomatometer score, Viewers score, Description, etc).
        """
        movie_title = self.soup.find('h1', attrs={'class':'mop-ratings-wrap__title mop-ratings-wrap__title--top'}).get_text()
        critique = self.soup.find('p', attrs={'class':'mop-ratings-wrap__text mop-ratings-wrap__text--concensus'}).get_text()
        tomato_score = self.soup.find('h1', attrs={'class':'mop-ratings-wrap__score'}).get_text(strip=True)
        tomato_reviews = self.soup.find('small', attrs={'class': 'mop-ratings-wrap__text--small'}).get_text(strip=True)
        user_score = self.soup.find('span', attrs={'class':'mop-ratings-wrap__percentage mop-ratings-wrap__percentage--audience'}).get_text(' ',strip=True)
        user_reviews = self.soup.find('small', attrs={'class':'mop-ratings-wrap__text--small'}).find_next('small').get_text(strip=True)

        self.critique_formatter(critique, movie_title, tomato_score, tomato_reviews, user_score, user_reviews)

    def critique_formatter(self,critique, movie, t_score, t_reviews, user_score, user_reviews):
        crit_format = int(len(critique) / 3)
        print(movie)
        print()
        print('TOMATOMETER: ', t_score)
        print('Reviews Counted: ', t_reviews)
        print()
        print('AUDIENCE SCORE: ',user_score )
        print('User Ratings:', user_reviews)
        print()
        print('Critic consensus:')
        if len(critique) > 25:
            print(critique[:crit_format])
            print(critique[crit_format:(crit_format * 2) + 1:])
            print(critique[-crit_format-1:], end="\n")
        else:
            print(critique, end="\n")


def main():
    formatted_movie = ''
    movie = input('What movie would you like to search? ').lower()
    os.system('cls')
    print()
    for x in movie:
        if x != ' ':
            formatted_movie += x
        elif x == ' ':
            formatted_movie += '_'
    try:
        search = Rater(formatted_movie)
        print('--------------------------------------------------------------------------------')
        search.rating()
    except AttributeError:
        print("Sorry, I couldn't find that movie, please try again. ")
        print("\n")
    print('--------------------------------------------------------------------------------')
    print()


if __name__ == '__main__':
    while True:
        main()


