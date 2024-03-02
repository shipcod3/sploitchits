import re

def extract_emails(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content by line breaks
    lines = content.split('\n')

    # Define a regex pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to extract all email addresses from each line
    emails = [re.findall(email_pattern, line) for line in lines]

    # Flatten the list of lists into a single list
    flat_emails = [email for sublist in emails for email in sublist]

    return flat_emails

# Replace 'your_file.txt' with the path to your text file
file_path = 'file.txt'
result_emails = extract_emails(file_path)

# Print each extracted email on a separate line
for email in result_emails:
    print(email)
