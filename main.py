print("Welcome to the Favourite Teachers Program")

#create empty list and input for user's four favourite teachers to be added to list

teachers = []
fav = input("\nWho is your favourite teacher: ").title()
teachers.append(fav)
fav = input("Who is your second favourite teacher: ").title()
teachers.append(fav)
fav = input("Who is your third favourite teacher: ").title()
teachers.append(fav)
fav = input("Who is your fourth favourite teacher: ").title()
teachers.append(fav)

#print list in ranked order, alpha order and reverse alpha order. Print top 2 teachers, bottom 2, least favourite and total number on list

print("\nYour favourite teachers ranked are: " + str(teachers))
print("Your favourite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favourite teachers  in reverse alphabetical order are: " + str(sorted(teachers,reverse=True)))

print("\nYour top two teachers are: " + str(teachers[0:2]))
print("Your next two favourites are: " + str(teachers[2:4]))
print("Your least favourite teacher is: " + teachers[-1])
print("You have " + str(len(teachers)) + " teachers in your list")

#add new favourite teacher to list
fav = input("\nYou have a new favourite teacher. What is their name: ").title()
teachers.insert(0,fav)

#lists printed as above
print("\nYour favourite teachers ranked are: " + str(teachers))
print("Your favourite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favourite teachers  in reverse alphabetical order are: " + str(sorted(teachers,reverse=True)))

print("\nYour top two teachers are: " + str(teachers[0:2]))
print("Your next two favourites are: " + str(teachers[2:4]))
print("Your least favourite teacher is: " + teachers[-1])
print("You have " + str(len(teachers)) + " teachers in your list")

#ask user to remove teacher

oldfav = input("\nYou've decided you don't like a teacher anymore. What teacher do you want to remove from your list: ").title()
teachers.remove(oldfav)

#lists printed as above
print("\nYour favourite teachers ranked are: " + str(teachers))
print("Your favourite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favourite teachers  in reverse alphabetical order are: " + str(sorted(teachers,reverse=True)))

print("\nYour top two teachers are: " + str(teachers[0:2]))
print("Your next two favourites are: " + str(teachers[2:4]))
print("Your least favourite teacher is: " + teachers[-1])
print("You have " + str(len(teachers)) + " teachers in your list")