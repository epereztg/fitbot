import gc
import requests

for obj in gc.get_objects():
    print("Check if there is an open connection:", obj)
    if isinstance(obj, requests.Session):
        print("Found open session:", obj)
        obj.close()
