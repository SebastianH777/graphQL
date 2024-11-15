
def resolve_hello(obj, info):
    return "Hello, world!"

def resolve_greeting(obj, info, name):
    return f"Hello, {name}!"

people_db = {
    "1": {"id": "1", "name": "josue", "age": 3, "number": 999999999},
    "2": {"id": "2", "name": "jose", "age": 5, "number":0000},
    "3": {"id" : "3", "name": "sebitas" , "age": 18, "number": 936418180},
    "4": {"id" : "4", "name": "roli" , "age": 20, "number":20222},
}

def resolve_getPerson(obj, info, id):
    return people_db.get(id)
