# Variables in Python

first_name = "Asabeneh"
last_name = "Yetayeh"
country = "Finland"
city = "Helsinki"
age = 250
is_married = True
skills = ["HTML", "CSS", "JS", "React", "Python"]
person_info = {
    "firstname": "Asabeneh",
    "lastname": "Yetayeh",
    "country": "Finland",
    "city": "Helsinki",
}

# Printing the values stored in the variables

print("First name:", first_name)
print("First name length:", len(first_name))
print("Last name: ", last_name)
print("Last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Person information: ", person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = (
    "Asabeneh",
    "Yetayeh",
    "Helsink",
    250,
    True,
)

print(first_name, last_name, country, age, is_married)
print("First name:", first_name)
print("Last name: ", last_name)
print("Country: ", country)
print("Age: ", age)
print("Married: ", is_married)
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
