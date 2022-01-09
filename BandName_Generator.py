print("Welcome to the shop where you can create customise bands for your favourite pets!")
user_name = input("Enter the name of the user:\n")
pet_name = input("Enter the name of the favourite pet of the user:\n")
user_city = input("Enter the city in which user grew up in:\n")
band_name = pet_name+"~"+user_city
print(f"Band name for the {user_name} is -",band_name)

#Method 2 using functions
# def greeting():
#     print("Welcome to the shop where you can create customise bands for your favourite pets!")

# def band_name(u_name,pet,city):
#     band = pet+"~"+city
#     print(f"Band name for the {u_name} is -",band)

# welcome_message = greeting()
# band_name_creation= band_name("Parth","Bruno","Mumbai")