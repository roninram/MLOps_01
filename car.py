"""
Instructions:
        1.	Program Introduction:
        •	Display a welcome message:
"Welcome to the Car and Profile Generator!"
        2.	Collect User Input:
        •	Ask the user to enter the following details:
        •	    Name of the car owner
        •	    Car brand
        •	    Car model
        •	    Car type (e.g., sedan, SUV, sports car)
        •	    Car color
        •	    Favorite feature of the car
        3.	Perform Calculations:
        •	    Base Price Calculation:
            Start with a base price of $50,000.
        •	    Add $1,000 for each character in the car brand.
        •	    Add $2,000 for each character in the car type.
        •	Tax Calculation:
                Apply a 10% tax on the calculated price.
        •	Discount Calculation:
                Apply a discount of $100 for each character in the car color.
        •	Bonus Calculation:
                Add a bonus of $500 for each character in the description of the favorite feature.
        •	Final Price Calculation:
                Final Price = Base Price + Tax - Discount + Bonus

    4.	Display the Car Profile:
        •	        Print the profile with all the user’s details and calculated values in a structured format.

    5. Ensure the final price is displayed with two decimal places and comma separators (e.g., $52,000.00).


SOLUTION REQUIREMENTS:
DESIGN
CODE
TEST CASES



"""

print("Welcome to the Car and Profile Generator!")

# Collecting user input
owner_name = input("Enter your name: ")
car_brand = input("Enter the brand of your car: ")
car_model = input("Enter the model of your car: ")
car_type = input("Enter the type of your car (e.g., sedan, sports car, SUV): ")
car_color = input("Enter your car's color: ")
favorite_feature = input("What is your favorite feature of your car? ")

# Calculate the price based on car brand and car type
# The formula adds a base price of 50000, then adds:
#   1000 for each character in the car brand, and
#   2000 for each character in the car type.
price = 50000 + 1000 * len(car_brand) + 2000 * len(car_type)

tax = price * 0.10

# Calculation 3: Discount
# A discount is computed based on the length of the car color string.
discount = 100 * len(car_color)

# Calculation 4: Bonus
# A bonus value is added, based on the length of your favorite feature's description.
bonus = 500 * len(favorite_feature)


# Calculation 5: Final Price
# The final price adds the base price and tax, subtracts the discount, then adds the bonus.
final_price = price + tax - discount + bonus


# Displaying the profile in a structured layout
sep = "#" * 10
print(f"{sep*5:<100}")
# print("\n--------------------------------------------")
print("          Car and Personality Profile       ")
print(f"{sep*5:<100}")
# print("--------------------------------------------")
print("Name:             " + owner_name)
print("Car Brand:        " + car_brand)
print("Car Model:        " + car_model)
print("Car Type:         " + car_type)
print("Car Color:        " + car_color)
print("Favorite Feature: " + favorite_feature)

print(f"{sep*5:<100}")

print(f"Price Tag:        ${price:^,.2f}")
print(f"Tax (10%):        ${tax:^,.2f}")
print(f"Discount:         ${discount:^,.2f}")
print(f"Bonus:            ${bonus:^,.2f}")
print(f"Final Price:      ${final_price:^,.2f}")

print(f"{sep*5:<100}")
