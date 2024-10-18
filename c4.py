def most_active(bio_data):
    #Check to see if author was active
    most_active_author = None
    max_active_years = 0

    for author, birth, death in bio_data:
        active_years = death - birth
        
        if active_years > max_active_years:
            max_active_years = active_years
            most_active_author = author

    return most_active_author

#Author data
bio_data = [
    ('Alice', 1901, 1950),
    ('Bob',   1920, 1960),
    ('Carol', 1908, 1945),
    ('Dave',  1951, 1960)
]

#Get the result
result = most_active(bio_data)
print(f"The most active author is: {result}")
