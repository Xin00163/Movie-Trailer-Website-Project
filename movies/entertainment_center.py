import fresh_tomatoes
import media

the_handmaiden = media.Movie("The Handmaiden",
                        "A woman is hired as a handmaiden to a Japanese heiress, but secretly she is involved in a plot to defraud her.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Handmaiden_film.png",
                        "https://www.youtube.com/watch?v=IkvHtfRAKNk")

fight_club = media.Movie("Fight Club",
                        "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

forrest_gump = media.Movie("Forrest Gump",
                        "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0")

mad_max = media.Movie("Mad Max",
                      "A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

gladiator = media.Movie("Gladiator",
                     "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                     "https://www.youtube.com/watch?v=IvTT29cavKo")

braveheart = media.Movie("Braveheart",
                        "When his secret bride is executed for assaulting an English soldier who tried to rape her, William Wallace begins a revolt against King Edward I of England.",
                        "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                        "https://www.youtube.com/watch?v=j53_WxqPZ7c")

movies = [the_handmaiden, fight_club, forrest_gump, mad_max, gladiator, braveheart]
fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
