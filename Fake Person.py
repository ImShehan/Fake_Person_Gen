import requests

# Define the API endpoint
url = "https://randomuser.me/api/?results=20"

# Make the API request
response = requests.get(url).json()

# Write the details to a text file
with open("person_details.txt", "w") as file:
    for i, person in enumerate(response['results']):
        file.write(f"Person {i + 1} -\n")
        file.write(f"  • Full name    - {person['name']['first']} {person['name']['last']}\n")
        file.write(f"  • Birth        - {person['dob']['date'][:10]}\n")
        file.write(f"  • Address      - {person['location']['street']['number']} {person['location']['street']['name']}, {person['location']['city']}, {person['location']['state']}, {person['location']['postcode']}\n")
        file.write(f"  • Phone Number - {person['cell']}\n")
        file.write(f"  • Email        - {person['email']}\n")
        file.write(f"  • Password     - {person['login']['password']}\n\n")

print("person_details.txt has been generated successfully.")
