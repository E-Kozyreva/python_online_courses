# Создайте класс BlogPost с атрибутами user_name, text, number_of_likes. Создайте два объекта этого класса. 
# После создания измените атрибут number_of_likes одного из объектов. Распечатайте атрибут number_of_likes каждого из объектов
from random import randint

class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


post_news = BlogPost('Honkai', 'Release of a new character', 0)
post_about_games = BlogPost('Hikki', "It's amazing", 0)

# Number of likes
post_news.number_of_likes = randint(0, 1000)
post_about_games.number_of_likes = randint(0, 1000)

print(post_news.number_of_likes)
print(post_about_games.number_of_likes)
