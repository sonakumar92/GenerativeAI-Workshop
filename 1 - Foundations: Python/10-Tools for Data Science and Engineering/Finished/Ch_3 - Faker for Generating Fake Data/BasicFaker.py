# Example file for Advanced Python: Top Tools for Data Science
# Introduction to the Faker library


import faker


# create an instance of faker
fake = faker.Faker()


# generate basic fake generic data
print(fake.random_number())
print(fake.date())
print(fake.text())

# Generate some basic fake data about a person
print(fake.name())
print(fake.address())
print(fake.email())
print(fake.job())

# generate more granular fake data
print(fake.word())
print(fake.sentence())
print(fake.day_of_week())
print(fake.year())
