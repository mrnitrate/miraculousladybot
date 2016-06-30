import pytumblr
import psycopg2

client = pytumblr.TumblrRestClient( #https://api.tumblr.com/console
    '<EBA7cZNiWUKwuw7waQ12rf2YBUwmlHWh45VwgGhdjVXTwpWdJH>',
    '<PIFMt7nyx3bHoQY8ixbqEgrnx4orIfqNyhy5kWLRgbWrYg0iNt>',
    '<OC6bmFeYDHj61iqYZ0ZDWcFLI5EjCWbiICzTjEegBDoRh3UqaY>',
    '<LM27nLuW2BqiHBBgFSeznJ10koxaMoon1uYi1TI0KATdrUJMOD>',
)

conn = psycopg2.connect("dbname=fanfictions user=postgres")

blogName = "miraculousladybot"


#Connect to database
conn.autocommit = True
db = conn.cursor()



print "Loaded settings."
