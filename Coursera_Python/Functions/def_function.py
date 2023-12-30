def greeting(name):
    print("Welcome, " + name)

greeting("Jessica")

def greeting(name, department):
    print("Welcome, " + name)
    print(" You are part of the " + department) 

greeting("Jessica", "Software development team")

print(type("Welcome")) 

def area_triangle(base, height):
     return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("the sum of both area is : " + str(sum))

def convert_seconds(seconds):
     hours = seconds // 3600
     minutes = (seconds - hours * 3600) // 60

def lucky_number(name): 
    number = len(name) * 9
    print("Hello" + name + " . Your lucky number is" + str(number)) 

    lucky_number("Kay")
    lucky_number("Cameron")


def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)

# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))

# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in millimeters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in millimeters is " + str(convert_volume(2)*2))
# Alternative calculation:
# print("The volume in millimeters is " + str(convert_volume(4))

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return convert_distance

# Do not indent any of the following lines of code as they are 
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = str(1.6) (my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
print("The round-trip in kilometers is " + str(my_trip_km*2))
