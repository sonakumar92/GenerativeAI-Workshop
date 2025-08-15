# Example file for Advanced Python: Top Tools for Data Science
# Using the Faker library to generate text data


import faker


# Create Faker instance and set seed for reproducibility
fake = faker.Faker()


# Basic text generation - These methods generate fundamental text elements
print(fake.word())  # Generates a single random word, useful for testing or creating simple labels
print(fake.words(nb=3))  # Creates a list of random words, good for generating tags or keywords
print(fake.sentence(nb_words=6))  # Produces a grammatically correct sentence with specified word count
print(fake.sentences(nb=2))  # Generates multiple sentences, useful for creating short descriptions


# Paragraphs and longer text - For generating larger blocks of content
print(fake.paragraph(nb_sentences=3))  # Creates a coherent paragraph with specified number of sentences
print(fake.paragraphs(nb=2))  # Generates multiple paragraphs, good for article or blog post content
print(fake.text(max_nb_chars=200))  # Creates text with a specific character limit, useful for fields with size constraints


# Specialized text - Industry-specific and business-related content
print(fake.catch_phrase())  # Generates corporate-style slogans or taglines
print(fake.bs())  # Creates business speak phrases using common corporate buzzwords


# Internet-related text - Web-specific content
print(fake.user_name())  # Creates usernames suitable for online accounts
print(fake.domain_name())  # Produces realistic domain names for web addresses
print(fake.url())  # Creates complete URLs with proper structure
print(fake.password(length=12, special_chars=True))  # Generates secure passwords with specified requirements


# File-related - File system content
print(fake.file_name())  # Generates realistic file names with extensions
print(fake.file_path())  # Creates valid file paths for various operating systems
print(fake.mime_type())  # Produces standard MIME types for file identification


# Additional text generation examples
print(f"Random letter (any case): {fake.random_letter()}")
print(f"Random letters (specified length): {fake.random_letters(length=5)}")
print(f"Random lowercase letter: {fake.random_lowercase_letter()}")
print(f"Random uppercase letter: {fake.random_uppercase_letter()}")
