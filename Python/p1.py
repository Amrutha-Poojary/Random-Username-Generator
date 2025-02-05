import random
import string

def load_word_lists():
    adjectives = ["Happy", "Cool", "Brave", "Clever", "Swift", "Fierce", "Loyal", "Mighty", "Witty", "Bold"]
    nouns = ["Dragon", "Tiger", "Falcon", "Wolf", "Panther", "Eagle", "Shark", "Phoenix", "Lion", "Hawk"]
    return adjectives, nouns

def generate_username(include_numbers=True, include_special=False, length=8):
    adjectives, nouns = load_word_lists()
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special:
        special_chars = "!@#$%^&*"
        username += random.choice(special_chars)
    
    return username[:length]

def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"{len(usernames)} usernames saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    include_special = input("Include special characters? (y/n): ").strip().lower() == "y"
    length = int(input("Maximum username length (default 8, enter 0 to ignore): ") or 8)
    
    usernames = [generate_username(include_numbers, include_special, length) for _ in range(num_usernames)]
    
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    save_choice = input("Do you want to save the usernames to a file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_usernames(usernames)
    
    print("Thank you for using the Random Username Generator!")

if __name__ == "__main__":
    main()
