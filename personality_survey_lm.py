print("What's your favorite sport?")
sport = input().lower()

if sport == "dance":
    print("That's my favorite too!")
elif sport == "field hockey":
    print("I do that for my school!")
elif sport == "golf":
    print("I also play that all the time!")
else:
    print(sport + " sounds fun!")

print("What's your favorite TV show?")
tvshow = input().title()

if tvshow == "How I Met Your Mother":
    print("I LOVE that show!")
elif tvshow == "Gilmore Girls":
    print("That is such a good show!!")
elif tvshow == "Friends":
    print("That one's also amazing!")
else:
    print("I haven't seen " + tvshow + " yet.")

print("What's your favorite book?")
book = input().title()

if "Harry Potter" in book:
    print("One of my favorite books ever!")
elif book == "I Am Malala":
    print("I also love that book!")
else:
    print(book + " is not one of my favorites, but I'm glad you like it!")

myrestaurants = ["Meli Melo", "Sundown Saloon", "Bartaco"]

print("Where do you like to eat?")
restaurant = input().lower()

if restaurant in myrestaurant:
    print("Mine too!")
else:
    print("I've never been there, but it sounds good!")

myfood = ["nutella crepe", "chicken nuggets", "tacos"]

print("What food do you like to eat there?")
food = input().lower

if food in myfood:
    print("I LOVE that too!")
else:
    print("Oooh, that sounds good. I've never tried that.")

    
