import pytest
import time
from libUtils.seleniumUtils.driver_manager import DriverManager
from webapps.orangeHRM.employeel_list_page import EmployeeListPage

@pytest.fixture
def setup():
    driver_manager = DriverManager()
    yield driver_manager
    driver_manager.close_session()

def test_search(setup):
    '''
     entering employee information and reseting
    1.  Launch the application & login with default credentials
    2.  Navigate to the Pim and then to employee list
    3.  Enter the first  name , emp id and supervisor name
    4. select the employee satus, job title
    6.  Click the reset button & check the text boxes are reset or not
    '''
    #setup.driver
    #driver_manger = DriverManager()
    add = EmployeeListPage(setup.driver)
    element=add.search("Linda Jane Anderson","102","John Smith")
    print(element)

