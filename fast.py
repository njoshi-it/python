def get_full_name(first_name: str, last_name: str): #type hint 
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))



