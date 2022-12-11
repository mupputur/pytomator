import pytest
import time
from libUtils.seleniumUtils.driver_manager import DriverManager
from webapps.orangeHRM.add_employee_page import AddEmployeePage

@pytest.fixture
def setup():
    driver_manger = DriverManager()
    yield driver_manger
    driver_manger.close_session()
    
def test_add_employee_without_login_details(setup):
    '''
     Adding new employee with default employee ID
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add emplyee details
    4.  Enter the first  name & last name
    5.  Give the new employee ID
    6.  Click the save button & check the emplyee was successfully created or not in the employee list
    '''
    #setup.driver
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_out_login_details("sridevi","devi","anke")
    assert element.text == 'Personal Details'


def test_add_employee_with_login_details(driver_manger):
    '''
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add employee details
    4.  Enter the first  name & last name & employee ID
    6.  Enable the Craete Login Details button
    7.   User the firstname as the username and create a password
    8.  click the status as enabled and clcik save button
    9.  Check the employee details in employee list
    10. Logout the application and re-login with the  new emplyee login details
    '''
    #driver_manger = DriverManager()
    add = AddEmployeePage(driver_manger.driver)
    element= add.add_employee_with_login_details("vallika","valli","kolakaluri","prava","Valli@123","Valli@123")
    assert element.text == 'Personal Details'
