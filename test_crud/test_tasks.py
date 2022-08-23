import http
from urllib import response
import urllib3

testInput = [{"id": 1, "task": "Pipeline Setup"}]
baseURL = "http://127.0.0.1:5000/"
http = urllib3.PoolManager()
def test_get_tasks():
    response = http.request('GET', f'{baseURL}tasks/')
    assert response.status == 200

def test_add_tasks():
    response = http.request("POST", f"{baseURL}add_new_tasks", {"id": 1, "task": "Pipeline Setup"})
    if response.status == 200:
        data = response.data
        if "id" in data and "task" in data:
            return True

def test_update_fields():
    response = http.request("PUT", f"{baseURL}update_task_by_id", {"id": 1, "task": "Pipeline Setup-1"})
    if response.status == 200:
        data = response.data
        if "id" in data and "task" in data:
            return True

def test_update_field_id():
    response = http.request("PUT", f"{baseURL}update_task_by_id", {"id": 1, "task": "Pipeline Setup-2"})
    if response.status == 200:
        data = response.data
        if "id" in data and "task" in data:
            try:
                id = int(id)
                return True
            except:
                raise Exception

def test_negative_testing():
    response = http.request("PUT", f"{baseURL}update_task_by_id", {"id": 1, "task": "Pipeline Setup"})
    if response.status == 200:
        data = response.data
        if "id" in data and "data" in data:
            try:
                id = int(id)
                return False
            except:
                raise Exception

def test_delete():
    response = http.request("DELETE", f"{baseURL}delete_task_by_id/1")
    assert response.status == 200
