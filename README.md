# DutchPoliceInternetForensics
 ##Readme- Secure Software Development Assessment- Coding output




##**Purpose of Program**
###This is a python program developed using Django Framework, to demonstrate secure software for Dutch Police Internet Forensics.  This program demonstrates successful secure login to the platform, using 2 factor-authentication as both a general and government user. It is used to securely store messages in a database, mitigating the risk of sensitive data being exposed. 


##**Instructions for use**

###**How to run the system**
###Using a terminal, navigate to, and start the virtual environment – Folder is “Env_site” (create a virtual environment if you don’t have one)
    *Type **“Source bin/activate”**- Mac
    *Type **“Scripts\activate”** - Windows
###Still using the terminal, navigate to the location of the Django Project and start Python –cd project/DutchPoliceSystem
    *Type **“python manage.py runserver”**
    *Type **“python3 manage.py runserver”** if having multiple versions of python

###Once Python is running, using your preferred browser, navigate to URL – https://localhost:8000

###**General User**
###**To create a new user -**
    *From https://localhost:8000, click on **“Register User” **
    *Follow the instructions and fill in the form
###After user is created, you will be redirected to the standard login screen

###**Login Process**
    *Enter username and password credentials
        *OTP prompt will appear in Terminal. 
    *Enter the OTP 
        *If login is successful, user is redirected to dashboard.

###**General User- Create Message**
        *Click on “Create Message” 
        *Fill in the form and select “send”. Form will be securely sent to the Police.

###**Police User**
####**Login Process**
    *Enter username and password credentials
        *OTP prompt will appear in Terminal. 
    *Enter the OTP 
        *If login is successful, user is redirected to dashboard.

###**View Messages received**
    *Click on **“All Messages”** to view all messages received from the general users

###**Register new user**
    *Click on **“Register”** to add a new police user

###**Test Login Data**
###For test purposes, User Accounts have been created to test functionality.

###**Police User**
###Username: Police01    Password: police01
###**General User**
###Username: user02    Password: donkey123 

##Software and Libraries used 

###Django was the main framework we used during the implementation as it has the capability of scaling the project at a later stage of future development. With this framework, pre-installed libraries that are open source are ready to be used and this assisted us as it saved significant time of implementation with the libraries. As we were to use the Bycrpt library to securely store the passwords of the users, we realised that Django has an authentication library installed that assists in validation and hashing the password prior to storing the database.
###As identified in our design document, the SQLite library was to be used however due to the chosen framework, during the installation of the framework SQLite was pre-installed within the framework providing us a database to start with.
###Django has libraries that can be used for creating tests to ensure the functionality of the system works as required, hence we did not use the unit testing library as initially thought.  

##Libraries implemented
    *RSALIB 
    *PYOTP 
###Due to time constraints and lack of programming experience in Django, secure application development and login was prioritized, therefore we have omitted the following functionalities during the implementation of a secure system
    *User Permissions and Roles
    *User Login Auditing
    *Update and Deleting records from the database- Our aim for this project was to focus on storing the encrypted data securely in the database and therefore we were unable to create this feature.
    *With the level of experience, it was not possible to decrypt the encrypted message stored in the database to display to the police users



##Privacy and Security regulations
###By implementing the stated libraries, data compliance for standards such as GDPR are met. User data is protected through encryption, MFA and hashing, and through the use of permissions to ensure users have access only to resources they are entitled to.

## References:
    *Kablian (2022) How to encrypt and decrypt strings in python?, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/how-to-encryptand-decrypt-strings-in-python/ [Accessed: December 8, 2022].
    *Pyauth (2021) Pyauth/pyotp: Python one-time password library, GitHub. Available at: https://github.com/pyauth/pyotp [Accessed: December 8, 2022]. 


