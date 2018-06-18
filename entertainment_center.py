import fresh_tomatoes
import media


toy_story = media.Movie("Toy story", "A story of a boy and his toys that come to life", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on a alien planet", "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

shawshank = media.Movie("Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "https://en.wikipedia.org/wiki/The_Shawshank_Redemption#/media/File:ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

no_country = media.Movie("No Country For Old Men", "Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash near the Rio Grande.", "https://en.wikipedia.org/wiki/No_Country_for_Old_Men_(film)#/media/File:No_Country_for_Old_Men_poster.jpg", "https://www.youtube.com/watch?v=38A__WT3-o0")

up_in_the_air = media.Movie("Up in the Air", "Ryan Bingham enjoys living out of a suitcase for his job, travelling around the country firing people, but finds that lifestyle threatened by the presence of a potential love interest, and a new hire.", "https://en.wikipedia.org/wiki/Up_in_the_Air_(2009_film)#/media/File:Up_in_the_Air_Poster.jpg", "https://www.youtube.com/watch?v=rTL1FmvVCuA")

minority_report = media.Movie("Minority Report", "In a future where a special police unit is able to arrest murderers before they commit their crimes, an officer from that unit is himself accused of a future murder.", "https://en.wikipedia.org/wiki/Minority_Report_(film)#/media/File:Minority_Report_Poster.jpg", "https://www.youtube.com/watch?v=lG7DGMgfOb8")

###lists - "https://docs.python.org/2/tutorial/introduction.html#lists"
movies = [toy_story, avatar, shawshank, no_country, up_in_the_air, minority_report]

#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

#print(avatar.storyline)
#avatar.show_trailer()
#shawshank.show_trailer()
#print(shawshank.storyline)
print(media.Movie.__doc__)

print(media.Movie.__name__)

print(media.Movie.__module__)





