import pytest
import time
from libUtils.seleniumUtils.driver_manager import DriverManager
from webapps.orangeHRM.employeel_list_page import EmployeeListPage

@pytest.fixture
def setup():
    driver_manager = DriverManager()
    yield driver_manager
    driver_manager.close_session()

def test_reset_button(setup):
    '''
     entering employee information and reseting
    1.  Launch the application & login with default credentials
    2.  Navigate to the Pim and then to employee list
    3.  Enter the first  name , emp id and supervisor name
    4.  Click the reset button & check the text boxes are reset or not
    '''
    #setup.driver
    #driver_manger = DriverManager()
    add = EmployeeListPage(setup.driver)
    element=add.reset_button("Linda Jane Anderson","102","John Smith")
    assert element.text == ''

