def area_triangle(base, height):
     return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("the sum of both area is : " + str(sum))

def convert_seconds(seconds):
     hours = seconds // 3600
     minutes = (seconds - hours * 3600) // 60
     remaining_seconds = seconds - hours * 3600 - minutes * 60
     return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def greeting(name):
     print("Welcome, " + name)

greeting("Jessica")

result = greeting("Jessica")
print(result)