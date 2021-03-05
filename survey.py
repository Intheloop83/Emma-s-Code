# Create code to display an intro for the survey.
def intro():
    print("Thank you for taking this survey. You will be asked questions to determine how much we have in common. Hope you enjoy!")
intro()

# Create variable to tally points and have a special message revealed based on the score.
points = 0

# Create variable for user's name and to input information in the parenthesis.
name = input("Tell me your name. ")

# Create variable to input question.
# Use .lower to cover upper and lower case entries that the user may input.
# Create if/elif/else statements to print messages based on answers.
# Use .captalize to capitalize user input for movie, show, superpower and city variable names in else statements.

# Question 1

movie = input("What is your favorite gangster movie that has Al Pacino in it? ")
movie = movie.lower()
if movie == "scarface":
    print("Scarface is my favorite too. Its a classic!")
    points += 1
elif movie == "goodfellas":
    print("Nice. I like Goodfellas too but Scarface is my favorite.")
else:
    print(f"Great choice, but {movie.capitalize()} isnt my favorite. My favorite is Scarface.")

# Question 2

food = input("What is your favorite food? ")
food = food.lower()
if food == "seafood":
    print("I love seafood as well. Its my favorite. Yummy!")
    points += 1
elif food == "pizza":
    print("Mama Mia! Pass the Pizza! Cheesey pizza is delicious but I love seafood more!")
else:
    print(f"I see that you like {food}, but I love seafood. We may not have the same preference but we all have to eat!")

# Question 3

show = input("What is your favorite tv show? ")
show = show.lower()
if show == "martin":
    print("You so crazy! Martin is my fave too. #Throwback. He is hilarious!")
    points += 1
elif show == "friends":
    print("Friends is popular but I prefer Martin. I love a good laugh!")
else:
    print(f"You like {show.capitalize()}, but I love Martin. He cracks me up. Oldie but Goodie. LOL!!!")

# Question 4

subject = input("What was your favorite subject in school? Note: Gym is not an option! ")
subject = subject.lower()
if subject == "math":
    print("I was always good with numbers and I love a challenge. My favorite subject was math just like you. I shouldve been an accountant. :( ")
    points += 1
elif subject == "science":
    print("Lab coats and goggles= leave me alone! I was cool with science until it was time to dissect animals. Yuck!")
elif subject == "history":
    print("Too much to remember. I couldnt wait for history class to be over.")
elif subject == "gym":
    print("I said this wasnt an option! Lol!")
else:
    print(f"You liked {subject}, but my favorite was math. I like to solve problems.")

# Question 5

dog = input("What is your favorite breed of dog? ")
dog = dog.lower()
if dog == "pitbull" or dog == "pit bull":
    print("Thats what Im talking about. They're my faves as well. So many people think they're bad. Leave my pitbulls alone!")
    points += 1
elif dog == "german sheppard":
    print("Nice. German sheppards are good family dogs. I prefer pitbulls. Don't judge me.")
elif dog == "yorkie":
    print("Super cute but I need a bit of protection too. Im just saying! My fave would be pitbulls. Don't judge me.")
else:
    print(f"I see you like the {dog} breed, but my favorite dogs are pitbulls. Dont judge me. They're not as bad as people think they are. Love them!")

# Question 6

animal_insect = input("If you could be an animal or insect, which one would you be? ")
animal_insect = animal_insect.lower()
if animal_insect == "butterfly":
    print("Me too! I love butterflies. They're free, beautiful and change over time!")
    points += 1
elif animal_insect == "lion" or animal_insect == "tiger" or animal_insect == "bear":
    print("Roar! But Im not sared of lions or tigers or bears! ")
else:
    print(f"You chose {animal_insect}. Thats interesting. I'd be a butterfly. Free, beautiful and transformative!")

# Question 7

parent = input("Are you a parent? ")
parent = parent.lower()
if parent == "yes":
    print("I'm a proud mom! Children are blessings even though they drive us crazy at times.")
    points += 1
elif parent == "no":
    print("Thats cool. Maybe one day you will be.")
else:
    print(f"Thanks for sharing that with me.")

# Question 8

superpower = input("If you could have a superpower, what would it be? ")
superpower = superpower.lower()
if superpower == "heal" or superpower == "to heal" or superpower == "healing":
    print("Me too! Healing is so necessary.")
    points += 1
elif superpower == "x-ray vision" or superpower == "xray vision" or superpower == "xray" or superpower == "x-ray":
    print("I dont know if you chose this because you're naughty or want to be safe...Hmmmm!")
else:
    print(f"{superpower.capitalize()} is interesting. I would like the power to heal the world. We need help!!!")
    
# Question 9

button = input("Would you rather have a rewind button , pause button or fast forward button on your life? ")
button = button.lower()
if button == "pause button" or button == "pause":
    print("I'd choose a pause button too. This way I can have a moment to think before I make certain choices.")
    points += 1
elif button == "rewind button" or button == "rewind":
    print("We all feel like we'd like to do some things over. A rewind button wouldnt be bad but I'd choose the pause button.")
else:
    print(f"You chose {button}. Interesting choice.")

# Question 10

city = input("What's your favorite city? ")
city = city.lower()
if city == "new york" or city == "ny":
    print("I'm from New York. Its my fave too. Concrete jungle where dreams are made of. I love New York!")
    points += 1
elif city == "los angeles" or city == "la":
    print("I'm going , going , back , back to Cali, Cali! Hello Hollywood!")
else:
    print(f"{city.capitalize()} is your favorite city. Mine is New York. Concrete jungle where dreams are made of!")

# Survey Results
# Create if/elif atatements to reveal how much we have in common based on points.
if points < 5:
    print (f"{name}, it seems like we dont have much in common but thats okay.")
elif points == 0:
    print(f"{name}, it seems that we have nothing in common.")
elif points > 5:
    print(f"{name}, it appears that we have some things in common. Maybe we should be friends. :)")

# End of Survey Riddle
# Create a variable to tally the amount of guesses taken to get the correct answer.
# Use while loop and if/elif/else statements to give user options and instructions based on input and print messages based on user's answers.
# Use .upper to account for lower case and upper case entries.
guess = 0
while True == True:
    print("Heres a quick riddle to end the survey. What tastes better than it smells?")
    print("Type your guess, or type 'help1', 'help2', or 'I give up'")
    answer = input()
    guess += 1

    if "tongue" in answer:
        print("You got it smarty pants!")
        print ("It took you " + str(guess) +   " guess(es)")
        break
    elif answer == "help1":
        print("Its not food.")
    elif answer == "help2":
        print("Its a body part.")
    elif answer.upper() =="I GIVE UP":
        print ("The answer was a tongue. Now type tongue.")
    else:
        print("Try again")
        
# Create code to display an outro for the survey.
def outro():
    print(f"We have had the opportunity to find out a few things about each other. Whether we have things in common or not, I appreciate you taking this survey. Thanks a ton {name}. I hope you enjoyed it! :)")
outro()
