# String manipulation
# str()

def print_greeting(name, age, is_birthday):
    result = "Hello " + name + ". "
    new_age = age
    if is_birthday:
        result += "It is your birthday today! Happy birthday! "
        new_age += 1
    result += "You are " + str(new_age) + " years old."
    return result
