import json
import time
from random import randint
from data import first_names, last_names, emails, streets, cities, countries


def get_random_user(id):

    return {
        "id" : id,
        "first_name": first_names[randint(0,4)],
        "last_name": last_names[randint(0,4)],
        "email": emails[randint(0,4)],
        "street": streets[randint(0,4)],
        "city": cities[randint(0,4)],
        "country": countries[randint(0,4)],
    }

def get_list_of_users():
    users = []
    for i in range(1000):
        users.append(get_random_user(i))
    return users

random_users_list = get_list_of_users()

random_users_list_json = json.dumps(random_users_list)
current_timestamp = time.time()
output_file_name = "output/random_users"+str(current_timestamp)+".json"
output_file = open(output_file_name, "w")
output_file.write(random_users_list_json)


print("random users were generated and saved in " + output_file_name)


