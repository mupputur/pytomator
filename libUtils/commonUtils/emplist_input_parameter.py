import json
from test_data.setup_path import Paths

def get_test_data(test_fun):
    path = Paths.setting("employee_list_testdata.json")
    print(path)
    with open(path, 'r') as f:
        resp = json.load(f)
        return resp.get(test_fun)

