import random


generated_birthdays = []


def find_the_birthdays_with_most_frequency(generated_birthdaysx: list):
    frequent_birthdays = []
    for items in generated_birthdaysx:
        if generated_birthdaysx.count(items) > 1:
            frequent_birthdays.append(items)

    x1 = frequent_birthdays[0]
    for items in frequent_birthdays:
        if generated_birthdaysx.count(items) > generated_birthdaysx.count(x1):
            x1 = items
    print(f"In this simulation, multiple people have birthdays on {x1}. ({generated_birthdaysx.count(x1)} people)")
    return x1


def birthday_generator():
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec")

    birthday_months = []
    birthday_dates = []

    number_of_birthdays_to_be_generated = input("How many birthdays shall i generate? (Max 100) \n>")

    for i in range(0, int(number_of_birthdays_to_be_generated)):
        birthday_months.append(random.choice(months))
        birthday_dates.append(random.randint(1, 31))

    for i in range(0, int(number_of_birthdays_to_be_generated)):
        birth_x = str(birthday_months[i]) + " " + str(birthday_dates[i])
        generated_birthdays.append(birth_x)

    print(f"Here are {number_of_birthdays_to_be_generated} birthdays: \n")

    for birthdays in generated_birthdays:
        print(birthdays + ",", end=" ")
    print("\n")

    x1 = find_the_birthdays_with_most_frequency(generated_birthdays)

    yes = input(f"""Generating {number_of_birthdays_to_be_generated} random birthdays 100,000 times... 
    Enter Yes to begin...""")

    if yes == "Yes":
        print("Let\'s run another 100,000 simulations.")

        number_of_birthdays_found = 0
        number_of_simulations = 0
        new_simulation_generated_random_birthdays = []

        birthday_months2 = []
        birthday_dates2 = []

        while number_of_simulations < 100001:
            for i in range(0, int(number_of_birthdays_to_be_generated)):
                birthday_months2.append(random.choice(months))
                birthday_dates2.append(random.randint(1, 31))

            for i in range(0, int(number_of_birthdays_to_be_generated)):
                birth_x2 = str(birthday_months2[i]) + " " + str(birthday_dates2[i])
                new_simulation_generated_random_birthdays.append(birth_x2)

            for items in new_simulation_generated_random_birthdays:
                if items == x1:
                    number_of_birthdays_found += 1
            number_of_simulations += 1

        print("100,000 simulations run.")
        print(f"Out of 100,000 simulations of {number_of_birthdays_to_be_generated} people, there was a matching "
              f"birthday in that group {number_of_birthdays_found} times.")

        probability = (int(number_of_birthdays_found)/100000)*100
        print(f'This means that {number_of_birthdays_to_be_generated} people have a {probability} % chance of '
              f'having a matching birthday in their group. That\'s probably more than you would think!')
    else:
        exit(0)


birthday_generator()
