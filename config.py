class Config:

    # Input Parameters for testcases / pages

    # URL
    base_url = "https://tutorialsninja.com/demo/"

    # Register User Page valid inputs
    valid_register_first_name = "qa"
    valid_register_last_name = "automation"
    valid_register_email = "qaautomation@gmail.com"
    valid_register_telephone = "1234567890"
    valid_register_password = "QRX@Xa6kQTDDSi"
    valid_register_confirm_password = "QRX@Xa6kQTDDSi"

    # Register User Page invalid inputs
    invalid_register_first_name = "qa$"
    invalid_register_last_name = "automation@#"
    invalid_register_email = "qaautomation123@gmail.comm"
    invalid_register_telephone = "1234%%%(&*)67890"
    invalid_register_password = "QAAutomation@123"
    invalid_register_confirm_password = "QAAutomation@123"
    blank_password = ""
    different_register_confirm_password = "QAjasdAutomation@123"

    # Invalid Login
    login_invalid_username = "qaauto@mation123@gmail.com"
    login_invalid_password = "QRX@Xa6kQTDDSi123"

    # Edit Your Account Information Page inputs
    edit_firstname = "automationqa"
    edit_lastname = "pythonplaywright"
    edit_telephone = "0987654321"

    # Forgot Password Page
    email_get_by_label = "qaautomation@gmail.com"

    # Modify Your Address Book Entries inputs
    modify_firstname = "python"
    modify_lastname = "automation"
    modify_address = "pycharm"
    modify_city = "pytest"
    modify_country = "India"
    modify_region = "Maharashtra"