class Config:

    # Input Parameters for Testcases

    # BASE URL
    valid_base_url = "https://tutorialsninja.com/demo/"

    # Register User Page - Valid Inputs
    valid_register_first_name = "qa"
    valid_register_last_name = "automation"
    valid_register_email = "qaautomation@gmail.com"
    valid_register_telephone = "1234567890"
    valid_register_password = "QRX@Xa6kQTDDSi"
    valid_register_confirm_password = "QRX@Xa6kQTDDSi"

    # Register User Page - Invalid Inputs
    invalid_register_first_name = "qa$"
    invalid_register_last_name = "automation@#"
    invalid_register_email = "qaautomation123@gmail.comm"
    invalid_register_telephone = "1234%%%(&*)67890"
    invalid_register_password = "QAAutomation@123"
    invalid_register_confirm_password = "QAAutomation@123"
    invalid_different_register_confirm_password = "QAjasdAutomation@123"

    # Register User Page - Blank Inputs
    invalid_blank_first_name = ""
    invalid_blank_last_name = ""
    invalid_blank_email_address = ""
    invalid_blank_telephone = ""
    invalid_blank_password = ""
    invalid_blank_confirm_password = ""

    # Register User Page - Invalid Login
    invalid_login_username = "qaauto@mation123@gmail.com"
    invalid_login_password = "QRX@Xa6kQTDDSi123"

    # Edit Your Account Information Page - Valid Inputs
    valid_edit_firstname = "automationqa"
    valid_edit_lastname = "pythonplaywright"
    valid_edit_telephone = "0987654321"

    # Forgot Password Page - Valid Inputs
    valid_email_get_by_label = "qaautomation@gmail.com"

    # Modify Your Address Book Entries - Valid Inputs
    valid_modify_firstname = "python"
    valid_modify_lastname = "automation"
    valid_modify_address = "pycharm"
    valid_modify_city = "pytest"
    valid_modify_country = "India"
    valid_modify_region = "Maharashtra"