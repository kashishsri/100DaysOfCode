# Dictionary in Python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
    "Loop" : "The action of doing something repeatedly.", 
}

# Nesting in Dictionaries
capitals = {
    "Uttar Pradesh" : "Lucknow",
    "Madhya Pradesh" : "Bhopal",
    "Goa" : "Panaji"
}
# Nesting a list in dict

travel_log = {
    "Uttar Pradesh" : ["Lucknow", "Kanpur", "Mangarh"],
    "Madhya Pradesh" : ["Maihar", "Satna"]
}

# Nesting a dict in dict

travel_log_per_visit = {
    "Uttar Pradesh" : {"Lucknow" : 5 , "Kanpur" : 3, "Mangarh" : 1},
    "Madhya Pradesh" : {"cities_visited" : ["Maihar", "Satna"], "total_visits" : 5}
}
# print(travel_log_per_visit)

# for key in travel_log_per_visit:
#     print(key)
#     print(travel_log_per_visit[key])

# Nesting dict in list
travel_log = [
    {
        "state": "Uttar Pradesh", 
        "cities_visited" : ["Lucknow", "Kanpur", "Mangarh"], 
        "total_visites" : 10
    },
    {
        "state": "Madhya Pradesh", 
        "cities_visited" : ["Maihar", "Satna"], 
        "total_visits" : 5
    },
]