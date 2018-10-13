from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve
PEOPLE = {
        "Farrell": {
            "fname": "Doug",
            "lname": "Farrell",
            "timestamp": get_timestamp()
        },
        "Brockman": {
            "fname": "Kent",
            "lname": "Brockman",
            "timestamp": get_timestamp()
        },
        "James": {
            "fname": "Lebron",
            "lname": "James",
            "timestamp": get_timestamp()
        },
}
# create handler for read (GET CRUD operation) peopl
def read():
    """
    This function responds to a GET request for /api/people with a complete list of people

    :return:        sorted list of people
    """
    # create the list of people from data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
