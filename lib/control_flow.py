#!/usr/bin/env python3

def admin_login(username, password):
    if (username.lower() == "admin" or username.upper() == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

# Examples
print(admin_login("sudo", "12345"))
# Output: "Access denied"

print(admin_login("admin", "12345"))
# Output: "Access granted"

print(admin_login("ADMIN", "12345"))
# Output: "Access granted"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

# Examples
print(hows_the_weather(33))
# Output: "It's brisk out there!"

print(hows_the_weather(55))
# Output: "It's a little chilly out there!"

print(hows_the_weather(90))
# Output: "It's too dang hot out there!"

print(hows_the_weather(70))
# Output: "It's perfect out there!"

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

# Examples
print(fizzbuzz(0))
# Output: "FizzBuzz"

