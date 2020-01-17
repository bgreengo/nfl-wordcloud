from sportsreference.nfl.roster import Roster
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import random

#Create empty list to store players names
players = []

# Pull down 49ers roster from sportsrefence API - Reference: https://sportsreference.readthedocs.io/en/latest/nfl.html
niners = Roster('SFO')

#Loop through players and parse for their last names and add to the list
for player in niners.players:
    if player.name != None:
        full_names = player.name
        last_names = full_names.split()[1]
        players.append(last_names)

#Add the picture 
logo = np.array(Image.open("niners.png"))

#Shuffle players names so the wordcloud uses other names beside alphabetically
random.shuffle(players)

#Create wordcloud
wordcloud = WordCloud(width=2000, height=2000, background_color= "red", relative_scaling=1, colormap="YlOrRd_r", #mask=logo, 
                        min_font_size = 10).generate(str(players))

#Plot the wordcloud
plt.figure(figsize = (8,8))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()