a = 6
a = a - 2
a = a * 2
a = a // 3
print(a)

#Q6
# List is mutable
numbers = [1, 2, 3]
numbers[1] = 20  # Changes second element to 20

# String is immutable
text = "abc"
# Trying to change the first character will give an error
text[0] = "d"  # This will cause a TypeError

#Q7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

random_numbers = ["XX" if x <= 50 else x for x in random_numbers]
random_numbers = [x for x in random_numbers if x == "XX"]

print(random_numbers)

#Q8
def valid_url(url):
    """
    Check if URL is valid or not

    :return:
    True if the URL is valid, False otherwise.
    """

    # Check if the URL starts with 'http://' or 'https://'. This is a must for any valid url
    if not url.startswith(("http://", "https://")):
        return False

    # Check if there is a dot in the URL which must come to have .com; .net; .org; etc.
    if "." not in url:
        return False

    # Check if there are spaces in the URL. You cannot have spaces in the URL so it makes it false if there is
    if " " in url:
        return False

    # If all basic checks pass, we consider the URL  valid
    return True


#Q9

def days(birthday):
    birth_year = int(birthday.split("-")[2])
    current_year = 2024
    years_since_birth = current_year - birth_year - 1
    total_days = 0
    for year in range(birth_year + 1, current_year):
        if year % 4 == 0:
            total_days += 366
        else:
            total_days += 365
    return total_days

birthday = "09-09-2004"
print("Days since birth:", days(birthday))



