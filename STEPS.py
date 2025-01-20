from datetime import datetime

def get_shortest_name(name1, name2):
    return name1 if len(name1) < len(name2) else name2

def greet_user():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    
    shortest_name = get_shortest_name(first_name, last_name)
    
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    print(f"{greeting}, {shortest_name}!")

if __name__ == "__main__":
    greet_user()