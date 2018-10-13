"""
The people module that supports all REST actions for the PEOPLE collection
"""

from flask import make_response, abort

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
def read_all():
    """
    This function responds to a GET request for /api/people with a complete list of people

    :return:        sorted list of people
    """
    # create the list of people from data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    """ 
    This function responds to a GET request for /api/people/{lname} with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # check fro person in people
    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
    return person

def create(person):
    """
    This function creates a new person in the people structure based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # check if person exists
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )

def update(lname, person):
    """
    This function updates an existing person in the people structure 

    :param lname:   last name of person to update in the people structure 
    :param person:  person to update
    :return:        updated person structure
    """
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]

    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

def delete(lname):
    """
    This function deletes an existing person in the people structure 

    :param lname:   last name of person to delete in the people structure
    :return:        200 on successful delete, 404 if not found
    """
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
        
