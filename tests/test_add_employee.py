import pytest
import time
from libUtils.seleniumUtils.driver_manager import DriverManager
from webapps.orangeHRM.add_employee_page import AddEmployeePage

@pytest.fixture
def setup():
    driver_manager = DriverManager()
    yield driver_manager
    driver_manager.close_session()
    
def test_add_employee_without_login_details(setup):
    '''
     Adding new employee with default employee ID
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add emplyee details
    4.  Enter the first  name & last name
    6.  Click the save button & check the emplyee was successfully created or not in the employee list
    '''
    #setup.driver
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_out_login_details("Veena","karahalli","nanjundappa")
    assert element.text == 'Personal Details'

def test_add_employee_with_out_login_details_cus_empid(setup):
    '''
    1.  Launch the application & login_details
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
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_out_login_details_cus_empid("Vishal","sushi","rayappa","1278")
    assert element.text == 'Personal Details'


def test_add_employee_with_login_details(setup):
    '''
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add employee details
    4.  Enter the first  name & last name
    6.  Enable the Craete Login Details button
    7.   User the firstname as the username and create a password
    8.  click the status as enabled and clcik save button
    9.  Check the employee details in employee list
    10. Logout the application and re-login with the  new emplyee login details
    '''
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_login_details("Vinod","sushila","changalarayappa","Vinod10","Avnt@2022","Avnt@2022")
    assert element.text == 'Personal Details'

def test_add_existing_employee_with_out_login_details_diff_empid(setup):
    '''
    1.  Launch the application & login_details
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
    add = AddEmployeePage(setup.driver)
    element= add.add_existing_employee_with_out_login_details_diff_empid("Vishal","sushi","rayappa","12278")
    assert element.text == 'Personal Details'

def test_add_existing_employee_with_out_login_details_same_empid(setup):
    '''
    1.  Launch the application & login_details
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
    add = AddEmployeePage(setup.driver)
    element= add.add_existing_employee_with_out_login_details_same_empid("Vishal","sushi","rayappa","1278")
    assert element.text == 'Personal Details'

def test_add_employee_with_out_login_details_blank_fields(setup):
    '''
    1.  Launch the application & login_details
    2.  Navigate to the PIM
    3.  Click add button  to add employee details
    4.  Enter the first  name & last name
    5.  click the status as enabled and click save button
    6.  Check the employee details in employee list
    7. Logout the application and re-login with the  new employee login details
    '''
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_out_login_details_blank_fields(" ","kolar"," ")
    assert element.text == 'Required'

def test_add_employee_with_login_details_exist_username(setup):
    '''
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add employee details
    4.  Enter the first  name & last name
    6.  Enable the Craete Login Details button
    7.   User the firstname as the username and create a password
    8.  click the status as enabled and clcik save button
    9.  Check the employee details in employee list
    10. Logout the application and re-login with the  new emplyee login details
    '''
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_login_details_exist_username("Vikram","ram","rm","Vinod10","ramrM.123","ramrM.123")
    assert element.text == 'Personal Details'

def test_add_employee_with_login_details_diff_pwd_confpwd(setup):
    '''
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add employee details
    4.  Enter the first  name & last name
    6.  Enable the Craete Login Details button
    7.   User the firstname as the username and create a password
    8.  click the status as enabled and clcik save button
    9.  Check the employee details in employee list
    10. Logout the application and re-login with the  new emplyee login details
    '''
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_login_details_diff_pwd_confpwd("praveen","giri","kn","praveen10","pravin@22","pravin.22")
    assert element.text == 'Personal Details'

def test_add_employee_with_login_details_wrong_pwd_credential(setup):
    '''
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add employee details
    4.  Enter the first  name & last name
    6.  Enable the Craete Login Details button
    7.   User the firstname as the username and create a password
    8.  click the status as enabled and clcik save button
    9.  Check the employee details in employee list
    10. Logout the application and re-login with the  new emplyee login details
    '''
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_login_details_wrong_pwd_credential("srihari","venkat","av","srihari10","sriha","sriha")
    assert element.text == 'Personal Details'

def test_add_employee_without_login_details_01(setup):
    '''
     Adding new employee with default employee ID
    1.  Launch the application & login with default credentials
    2.  Navigate to the PIM
    3.  Click add button  to add emplyee details
    4.  Enter the first  name & last name
    6.  Click the save button & check the emplyee was successfully created or not in the employee list
    '''
    #setup.driver
    #driver_manger = DriverManager()
    add = AddEmployeePage(setup.driver)
    element= add.add_employee_with_out_login_details_01("Veena","karahalli","nanjundappa")
    assert element.text == 'Personal Details'