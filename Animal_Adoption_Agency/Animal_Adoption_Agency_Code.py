
# Animal class that contains the animal's characteristics
class Animal:
    def __init__(self, name, species, breed, age, sex, neutered, temperement, health_concerns):
        self.name = "Name: " + name
        self.species = "Species: " + species
        self.breed = "Breed: " + breed
        self.age = "Age: " + age
        self.sex = "Sex: " + sex
        self.neutered = "Neutered: " + neutered
        self.temperment = "Temperment: " + temperement
        self.health_concerns = "Health Concerns: " + health_concerns

# Animals list:
animal_dictionary = {
    1 : Animal("Lilo", "Cat", "Siamese", "4", "female", "False", "Gentle", "Weak Right Leg"),
    2 : Animal("Spicy", "Cat", "Bombay", "6", "female", "True", "Quiet", "None"),
    3 : Animal("Pepper", "Cat", "Bombay", "6", "female", "True", "Shy", "None"),
    4 : Animal("Gulu", "Cat", "American Shorthair", "9", "male", "True", "Aggresively Loving", "None"),
    5 : Animal("Lili", "Cat", "Black-White & Grey Tabby", "10", "female", "True", "Shy", "Chunky"),
    6 : Animal("Eddy", "Cat", "Orange Tabby", "10", "male", "True", "Orange", "Gastroinestinal Cancer & Morbidly Underweight"),
    7 : Animal("Rose", "Cat", "Persian", "5", "female", "True", "Playful", "None"),
    8 : Animal("Huck", "Cat", "Orange Tabby", "3", "True", "Lazy", "Overweight", "None"),
    9 : Animal("Cherry", "Dog", "Pitbull", "7", "male", "True", "Playful", "None"),
    10 : Animal("Kippy", "Dog", "Pitbull", "8", "male", "False", "Playful", "None"),
    11 : Animal("SlyGuy", "Dog", "Golden Retriever", "3", "male", "True", "Shy", "None"),
    12 : Animal("Charlie", "Dog", "Golden Retriever", "5", "male", "True", "Playful", "None"),
}

print("Hello! Welcome to Loveable Animal Adoption Agency!")
Looking_for_pet = input("Are you here looking for a pet here today? ").strip().lower()
if Looking_for_pet == "yes" or Looking_for_pet == "y":
    species = input("Are you looking for a cat or dog? ").strip().lower()

    if species == "cat":
        print("Here are the cats at our Adoption Agency: ")
        for animal in animal_dictionary:
            if animal_dictionary[animal].species == "Species: Cat":
                print(animal_dictionary[animal].name)
                print(animal_dictionary[animal].species)
                print(animal_dictionary[animal].breed)
                print(animal_dictionary[animal].age)
                print(animal_dictionary[animal].sex)
                print(animal_dictionary[animal].neutered)
                print(animal_dictionary[animal].temperment)
                print(animal_dictionary[animal].health_concerns)
                print(" ")

    if species == "dog":
        print("Here are the dogs at our Adoption Agency: ")
        for animal in animal_dictionary:
            if animal_dictionary[animal].species == "Species: Dog":
                print(animal_dictionary[animal].name)
                print(animal_dictionary[animal].species)
                print(animal_dictionary[animal].breed)
                print(animal_dictionary[animal].age)
                print(animal_dictionary[animal].sex)
                print(animal_dictionary[animal].neutered)
                print(animal_dictionary[animal].temperment)
                print(animal_dictionary[animal].health_concerns)
                print(" ")
        
    will_adopt_pet = input("Which pet would you like to adopt? Please provide their name (Capital first letter): ")
    for animal in animal_dictionary:
        if "Name: " + will_adopt_pet == animal_dictionary[animal].name:
            name = animal_dictionary[animal].name.replace("Name: ", "")
            print(f"{name} is available for adoption!")
            print(f"You have successfully adopted {name}")
            break


else:
    print("Okay. We hope to see you again soon! Have a good day!")