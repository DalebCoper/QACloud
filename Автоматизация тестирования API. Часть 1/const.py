import datetime
import pytz

# берем текущее время в зоне GMT +1 секунда (т.к. на исполнение теста тоже уходит время)
GMT = pytz.timezone("GMT")
dt = datetime.datetime.now(GMT) + datetime.timedelta(seconds=1)
headers = dt.strftime("%a, %d %b %Y %H:%M:%S %Z")

body = {"title": "foo", "body": "bar", "userId": 1}

URL = "https://jsonplaceholder.typicode.com"

get_valid_schema = {
    "type": "array",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "id", "title", "body"]
}

post_valid_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "id", "title", "body"]
}
