
### PROJECT  NAME 
 +  Safari Tours

### AUTHORS
 + Betty Weru
 + Denis Kisavi
 
 ## DESCRIPTION 
 - A python web application that allow users to login and book slots for their desired destinations and also leave reviews for their previous safaris
 
 >Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Email  | Account email, ``eg user@gmail.com``|
| Password  | Account password, ``eg 12345678``|

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Email  | User email, ``eg johndoe@testmail.com``|
| Password  | Account password, ``eg password123``|
| Confirm Password  | Account password, ``eg password123``|

> Booking inputs

| Inputs | Description  |
|---|---|
|  Name | The name of one booking the slot ie; ``your name``  |
|  Email | The email address of one booking slots ``johndoe@gmail.com``|
|  Destination | the desired you wish to travel ``lake region``|


## User Story

- User can sign in if they have no account.

- User can login to their account.

- User can book a travelling destination.

- User can view their booking history and profile information.

- User can logout of the application.

- User can leave a review of previous visits.

## <a href="https://tours-nd-travel.herokuapp.com///">Live preview of the site</a>

## Cloning
* On your terminal, run the following commands:
* $ git clone https://github.com/Kisavi/Safari-Tours.git
* $ cd Safari-Tours
* Create a virtual environment $ pv -m venv --without-pip virtual
* Activate the virtual environment $ source virtual/bin/activate
* Install Dependancies $ pip install -r requirements.txt
* Inside your root directory create a new file ```start.sh``` and add the following:
* ```python(version) manage.py server```
* Run chmod a+x start.sh  
* Run the application $ ./start.sh
## Development
#### Want to make a contribution to enhance an existing module or fix a bug? Great!
* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request
## Technology Used
* python3.8
* flask
* SQLite

## Known Bugs
#### 
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Contact Information
* For any inqueries feel free to write to us through
  + betty.weru@student.moringaschool.com
  + denis.kagunda@student.moringaschool.com
## Licence
* MIT License
* Copyright (c) 2022 Denis Kagunda


