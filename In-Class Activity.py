regular_price = float(input("Enter the regular price of the movie ticket:"))

age_discount = int(input("Enter your age (years):"))
height_discount = float(input("Enter your height (meters):"))
disability_discount = input("Do you qualify for a disability discount? (y/n):")

if age_discount <= 6:
    ticket_price = 0 * regular_price

elif height_discount <= 1.2:
    ticket_price = 0 * regular_price

elif disability_discount.lower() == "y":
    ticket_price = 0.5 * regular_price

else:
    ticket_price = regular_price

print("You should pay $", ticket_price, "for the movie ticket")