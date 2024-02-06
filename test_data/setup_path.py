import os

class Paths:

    @classmethod
    def setting(cls,filename):
        base = os.path.dirname(__file__)
        return os.path.join(base,filename)


if __name__=="__main__":

    full_path=(Paths.setting("add_employee_testdata.json"))
    fullpath=(Paths.setting("employee_list_testdata.json"))