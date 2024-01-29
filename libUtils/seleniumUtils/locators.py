

class LoginPageLocators:

    USERNAME_TB_NAME_LOC = ("username", "NAME")
    PASSWORD_TB_NAME_LOC = ("password", "NAME")
    LOGIN_BT_XPATH_LOC = ("//button[@type='submit']", "XPATH")

class AddEmployeePageLocators:
    FIRSTNAME_TB_XPATH_LOC = ("//input[@class='oxd-input oxd-input--active orangehrm-firstname']", "XPATH")
    MIDDLENAME_TB_XPATH_LOC = ("//input[@class='oxd-input oxd-input--active orangehrm-middlename']", "XPATH")
    LASTNAME_TB_XPATH_LOC = ("//input[@class='oxd-input oxd-input--active orangehrm-lastname']", "XPATH")
    SAVE_BT_XPATH_LOC = ("//button[@type='submit']", "XPATH")
    WAIT_BT_XPATH_LOC = "//h6[text()='Personal Details']"
    ENABLE_BT_XPATH_LOC=("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']","XPATH")
    USERNAME_TB_XPATH_LOC=("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input","XPATH")
    PASSWORD_TB_XPATH_LOC=("//input[@type='password']","XPATH")
    CONFIRM_PASSWORD_TB_XPATH_LOC=("(//input[@type='password'])[2]","XPATH")
    ADD_EMPLOYEE_TB_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-item'])[2]","XPATH")
    EMPLOYEE_ID_TB_XPATH_LOC=("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input","XPATH")
    ERROR_MESSAGE_LOC=("//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']","XPATH")

class PIMPAGELocators:

    CONFIGURATION_BT_XPATH_LOC=("//span[@class='oxd-topbar-body-nav-tab-item']", "XPATH")
    EMP_LIST_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-item']", "XPATH")
    ADD_EMP_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-item'])[2]", "XPATH")
    REPORT_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-item'])[3]", "XPATH")

    OPT_FIELD_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-link']","XPATH")
    CUSTOM_FIELD_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-link'])[2]","XPATH")
    DATA_IMPORT_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-link'])[3]","XPATH")
    REPORTING_METHODS_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-link'])[4]","XPATH")
    TERMINATIONAL_REASONS_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-link'])[5]","XPATH")


class HomePageLocators:
    PIM_PAGE_BT_XPATH_LOC=("//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a", "XPATH")
    ADMIN_PAGE_BT_XPATH_LOC=("//a[@href='/web/index.php/admin/viewAdminModule']", "XPATH")
    TIME_PAGE_BT_XPATH_LOC=("(//a[@class='oxd-main-menu-item'])[4]", "XPATH")
    RECRUITMENT_PAGE_BT_XPATH_LOC=("(//a[@class='oxd-main-menu-item'])[5]", "XPATH")
    PERFORMANCE_PAGE_BT_XPATH_LOC=("(//a[@class='oxd-main-menu-item'])[7]", "XPATH")
    LEAVE_PAGE_BT_XPATH_LOC=("//a[@href= '/web/index.php/leave/viewLeaveModule']", "XPATH")
    MYINFO_PAGE_BT_XPATH_LOC=("(//a[@class='oxd-main-menu-item'])[6]", "XPATH")
    DASHBOARD_PAGE_BT_XPATH_LOC=("//a[@class='oxd-main-menu-item active']", "XPATH")
    DIRECTORIES_PAGE_BT_XPATH_LOC=("(//a[@class='oxd-main-menu-item'])[8]", "XPATH")
    MAINTAINANCE_PAGE_BT_XPATH_LOC=("(//a[@class='oxd-main-menu-item'])[9]", "XPATH")
    BUZZ_PAGE_BT_XPATH_LOC=("//a[@href= '/web/index.php/buzz/viewBuzz']", "XPATH")


class AdminPageLocators:

    USER_MANAGEMENT_BT_XPATH_LOC=("//span[@class='oxd-topbar-body-nav-tab-item']", "XPATH")
    JOB_BT_XPATH_LOC=("(//span[@class='oxd-topbar-body-nav-tab-item'])[2]", "XPATH")
    ORGANIZATION_BT_XPATH_LOC=("(//i[@class='oxd-icon bi-chevron-down'])[3]", "XPATH")
    QUALIFICATIONS_BT_XPATH_LOC=("//*[text()='Qualifications ']", "XPATH")
    NATIONALITIES_BT_XPATH_LOC=('//*[text()="Nationalities"]', "XPATH")
    CORPORATE_BRANDING_BT_XPATH_LOC=("//*[text()='Corporate Branding']", "XPATH")
    CONFIGURATION_BT_XPATH_LOC=("//*[text()='Configuration ']", "XPATH")
    #USERS_MANAGEMENT
    USERS_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-link']","XPATH")
    #JOB----
    JOB_TITLES_BT_XPATH_LOC=("(//span[@class='oxd-topbar-body-nav-tab-item'])[2]","XPATH")
    PAY_GRADES_BT_XPATH_LOC=("(//a[@href='#'])[2]","XPATH")
    EMP_STATUS_BT_XPATH_LOC=("(//a[@href='#'])[3]","XPATH")
    JOB_CATEGORIES_BT_XPATH_LOC=("(//a[@href='#'])[4]","XPATH")
    WORK_SHIFTS_BT_XPATH_LOC=("(//a[@href='#'])[5]","XPATH")
    # ORGANIZATION------
    GENERAL_INFORMATION_BT_XPATH_LOC=("//*[text()='General Information']","XPATH")
    LOCATION_BT_XPATH_LOC = ("(//a[@href='#'])[2]","XPATH")
    STRUCTURE_BT_XPATH_LOC = ("(//a[@href='#'])[3]","XPATH")

      #QUALIFICATIONS------------
    SKILLS_BT_XPATH_LOC = ("//a[text()='Skills']", "XPATH")
    EDUCATION_BT_XPATH_LOC = ("(//a[@href='#'])[2]","XPATH")
    LICENSES_BT_XPATH_LOC =("(//a[@href='#'])[3]","XPATH")
    LANGUAGES_BT_XPATH_LOC =("(//a[@href='#'])[4]","XPATH")
    MEMBERSHIPS_BT_XPATH_LOC = ( "(//a[@href='#'])[5]","XPATH")
     #CONFIGURATION-------
    EMAIL_CONFIG_BT_XPATH_LOC =("//*[text()='Email Configuration']","XPATH")
    EMAIL_SUBSCRIPTION_BT_XPATH_LOC =("//*[text()='Email Subscriptions']","XPATH")
    LOCALIZATION_BT_XPATH_LOC =("//*[text()='Localization']","XPATH")
    LANGUAGE_PACKAGES_BT_XPATH_LOC =( "//*[text()='Language Packages']","XPATH")
    MODULES_BT_XPATH_LOC =("//*[text()='Modules']","XPATH")
    SOCIAL_MEDIA_AUTHENTICATION_BT_XPATH_LOC =("//*[text()='Social Media Authentication']","XPATH")
    REGISTER_OAUTH_CLIENT_BT_XPATH_LOC =("//*[text()='Register OAuth Client']","XPATH")
    LDAP_CONFIG_BT_XPATH_LOC =("//*[text()='LDAP Configuration']","XPATH")


class LeavePageLocators:
    APPLY_PAGE_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-item']","XPATH")
    MYLEAVE_PAGE_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-item'])[2]", "XPATH")
    ENTITLEMENTS_PAGE_BT_XPATH_LOC=("//span[@class='oxd-topbar-body-nav-tab-item']", "XPATH")
    REPORTS_PAGE_BT_XPATH_LOC=('//*[text()="Reports "]',"XPATH")
    ADD_ENTITLEMENTS_CONFIGURE_PAGE_BT_XPATH_LOC=("(//span[@class='oxd-topbar-body-nav-tab-item'])[3]", "XPATH")
    ADD_ENTITLEMENTS_LEAVE_LIST_PAGE_BT_XPATH_LOC=("//*[text()='Leave List']", "XPATH")
    ADD_ENTITLEMENTS_ASSIGN_LEAVE_PAGE_BT_XPATH_LOC=("//*[text()='Assign Leave']", "XPATH")
    #ENTITLEMENTS-----------
    ADD_ENTITLEMENTS_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-link']","XPATH")
    EMPLOYEE_ENTITLEMENTS_BT_XPATH_LOC = ("(//a[@class='oxd-topbar-body-nav-tab-link'])[2]","XPATH")
    MY_ENTITLEMENTS_BT_XPATH_LOC = ("(//a[@class='oxd-topbar-body-nav-tab-link'])[3]","XPATH")
    #REPORT--------------
    LEAVE_ENTITLEMENTS_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-link']","XPATH")
    MY_LEAVE_ENTITLEMENTS_BT_XPATH_LOC =("(//a[@class='oxd-topbar-body-nav-tab-link'])[2]","XPATH")
    #CONFIGURE-----------
    LEAVE_PERIOD_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-link']","XPATH")
    LEAVE_TYPES_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-link'])[2]","XPATH")
    WORK_WEEK_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-link'])[3]","XPATH")
    HOLIDAYS_BT_XPATH_LOC = ("(//a[@class='oxd-topbar-body-nav-tab-link'])[4]","XPATH")


class TimePageLocators:
    TIMESHEET_BT_XPATH_LOC=("//*[@class='oxd-icon bi-chevron-down']", "XPATH")
    ATTENDENCE_BT_XPATH_LOC=("//*[text()='Attendance ']","XPATH")
    REPORTS_BT_XPATH_LOC = ("(//span[@class='oxd-topbar-body-nav-tab-item'])[3]","XPATH")
    PROJECT_INFO_BT_XPATH_LOC = ("(//span[@class='oxd-topbar-body-nav-tab-item'])[4]", "XPATH")

    # TIMESHEET-----------
    MY_TIMESHEET_BT_XPATH_LOC = ("//a[@class='oxd-topbar-body-nav-tab-link']","XPATH")
    EMPLOYEE_TIMESHEET_BT_XPATH_LOC = ("//*[text()='Employee Timesheets']","XPATH")

    #ATTENDENCE-------------------
    MY_RECORDS_BT_XPATH_LOC = ("//*[text()='My Records']","XPATH")
    PUNCH_INOUT_BT_XPATH_LOC = ("//*[text()='Punch In/Out']","XPATH")
    EMPLOYEE_RECORDS_BT_XPATH_LOC = ("//*[text()='Employee Records']","XPATH")
    CONFIGARATION_BT_XPATH_LOC = ("//*[text()='Configuration']","XPATH")

    # REPORT------------
    PROJECT_REPORTS_BT_XPATH_LOC=("//*[text()='Project Reports']","XPATH")
    EMPLOYEE_REPORTS_BT_XPATH_LOC = ("//*[text()='Employee Reports']","XPATH")
    ATTENDENCE_SUMMARY_BT_XPATH_LOC = ("//*[text()='Attendance Summary']","XPATH")

    # PROJECT_INFO-------------
    CUSTOMERS_BT_XPATH_LOC = ("//*[text()='Customers']","XPATH")
    PROJECTS_BT_XPATH_LOC = ("//*[text()='Projects']","XPATH")


class ReportPageLocators:
    REPORTS_NAME_TB_XPATH_LOC=("//*[@placeholder='Type for hints...']","XPATH")
    SUB_BT_XPATH_LOC=("//*[text()=' Search ']", "XPATH")
    RESETS_NAME_TB_XPATH_LOC=("//*[@placeholder='Type for hints...']","XPATH")
    RESET_BT_XPATH_LOC=("//button[text()=' Reset ']","XPATH")
    GET_LIST_XPATH_LOC=("/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div","XPATH")
    REPORT_BT_XPATH_LOC=("(//a[@class='oxd-topbar-body-nav-tab-item'])[3]", "XPATH")


class EmployeeListPageLocators:
    EMPLOYEE_NAME_TB_XPATH_LOC=("//input[@placeholder='Type for hints...']", "XPATH")
    EMP_ID_TB_XPATH_LOC=("(//input[@class='oxd-input oxd-input--active'])[2]", "XPATH")
    STATUS_BT_XPATH_LOC=("//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']","XPATH")
    EMP_STATUS_BT_XPATH_LOC=("//*[text()='Full-Time Contract']", "XPATH")
    INCLUDE_BT_XPATH_LOC=("//div[text()='Current Employees Only']", "XPATH")
    SUPERVISOR_NAME_TB_XPATH_LOC=("(//input[@placeholder='Type for hints...'])[2]", "XPATH")
    JOB_TITLE_BT_XPATH_LOC=("(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]", "XPATH")
    JOB_TITLE_IS_BT_XPATH_LOC=("//*[text()='Account Assistant']", "XPATH")
    SUB_UNIT_BT_XPATH_LOC=("(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[4]", "XPATH")
    SUB_UNIT_IS_BT_XPATH_LOC=("//*[text()='Administration']", "XPATH")
    RESET_BT_XPATH_LOC=("//button[@class='oxd-button oxd-button--medium oxd-button--ghost']","XPATH")
    EMP_LIST_BT_XPATH_LOC=("//a[@class='oxd-topbar-body-nav-tab-item']", "XPATH")


class PIMConfigurationPageLocators:
    CUSTOM_FIELD_XPATH_LOC=( "//*[text()='Custom Fields']","XPATH")
    REPORTING_METHODS_XPATH_LOC=("//*[text()='Reporting Methods']","XPATH")
    TERMINATION_REASONS_XPATH_LOC=("//*[text()='Termination Reasons']","XPATH")
    OPTIONAL_FIELDS_BT_XPATH_LOC=("//*[text()='Optional Fields']","XPATH")

    SSN_FIELD_ENABLE_OPTIONAL_FIELDS_XPATH_LOC=("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH")
    SIN_FIELD_ENABLE_OPTIONAL_FIELDS_XPATH_LOC=("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH")
    ENABLE_OPTIONAL_FIELD_SAVE_BT_XPATH_LOC=("//button[@type='submit']", "XPATH")

    SSN_FIELD_DISABLE_OPTIONAL_FIELDS_XPATH_LOC = ("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH")
    SIN_FIELD_DISABLE_OPTIONAL_FIELDS_XPATH_LOC = ("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH")
    DISABLE_OPTIONAL_FIELD_SAVE_BT_XPATH_LOC = ("//button[@type='submit']", "XPATH")

    ENABLE_ALL_OPTIONAL_FIELDS_BT_XPATH_LOC=("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']", "XPATH")
    ENABLE_ALL_OPTIONAL_FIELDS_1_BT_XPATH_LOC=("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]", "XPATH")
    ENABLE_ALL_OPTIONAL_FIELDS_2_BT_XPATH_LOC=("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH")
    ENABLE_ALL_OPTIONAL_FIELDS_3_BT_XPATH_LOC=("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[3]", "XPATH")
    ENABLE_ALL_OPTIONAL_FIELDS_SAVE_BT_XPATH_LOC=("//button[@type='submit']", "XPATH")

    DISABLE_ALL_OPTIONAL_FIELDS_BT_XPATH_LOC = ("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']", "XPATH")
    DISABLE_ALL_OPTIONAL_FIELDS_1_BT_XPATH_LOC = ("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]", "XPATH")
    DISABLE_ALL_OPTIONAL_FIELDS_2_BT_XPATH_LOC = ("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]", "XPATH")
    DISABLE_ALL_OPTIONAL_FIELDS_3_BT_XPATH_LOC = ("(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[3]", "XPATH")
    DISABLE_ALL_OPTIONAL_FIELDS_SAVE_BT_XPATH_LOC = ("//button[@type='submit']", "XPATH")


    ADD_BT_XPATH_LOC=("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']", "XPATH")
    FIELD_NAME_TB_XPATH_LOC=("(//input[@class='oxd-input oxd-input--active'])[2]","XPATH")
    SCREEN_BT_XPATH_LOC=("//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']","XPATH")
    DETAILS_BT_XPATH_LOC=("//*[text()='Personal Details']","XPATH")
    TYPE_BT_XPATH_LOC=("(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]","XPATH")
    TYPE_DETAILS_BT_XPATH_LOC=("//*[text()='Text or Number']","XPATH")
    CUSTOM_FIELD_SAVE_BT_XPATH_LOC=("//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']","XPATH")

    CUSTOM_FIELD_RECORDS_XPATH_LOC=("//*[text()='Custom Fields']", "XPATH")

    REPORTING_METHODS_ADD_BT_XPATH_LOC=("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']", "XPATH")
    NAME_TB_XPATH_LOC=("(//input[@class='oxd-input oxd-input--active'])[2]", "XPATH")
    REPORTING_METHODS_SAVE_BT_XPATH_LOC=("//button[@type='submit']", "XPATH")

    REPORTING_METHODS_RECORDS_BT_XPATH_LOC=("//*[text()='Reporting Methods']","XPATH")

    TERMINATION_REASONS_ADD_BT_XPATH_LOC=("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']", "XPATH")
    TERMINATION_REASONS_NAME_TB_XPATH_LOC=("(//input[@class='oxd-input oxd-input--active'])[2]", "XPATH")
    TERMINATION_REASONS_SAVE_BT_XPATH_LOC=("//button[@type='submit']", "XPATH")

    TERMINATION_REASONS_RECORDS_BT_XPATH_LOC=("//*[text()='Termination Reasons']", "XPATH")