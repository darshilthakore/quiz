# Final Project

Web Programming with Python and JavaScript

This project is called __Testify__, whereby user can create an account, login and can give online tests from a catalogue of subjects and topics, and can check their score along with the answer key of the test which is given by the user.

The project quiz contain an app called __exam__ which contains the following files:
1. models.py
1. admin.py
1. views.py
1. urls.py
1. templates/exam/base.html
1. templates/exam/index.html
1. templates/exam/instructions.html
1. templates/exam/login.html
1. templates/exam/result.html
1. templates/exam/test.html
1. templates/exam/topics.html
1. static/exam/login.css
1. static/exam/style.css


## models.py

In the __models.py__ file, all the models required for the application to work are defined.

__Subject__ models defines the subjects present in our application _(eg. Computer Science, Social Science, General knowledge etc.)_ Each subject has a subject code _(eg. CS, SS, GK etc)_ and a name.

__Topic__ model defines the topic of a subject, whose test will be given by the user. Each topic has a code, name, subject, and a time limit for the test of that topic. _(subject field here is the foreign key for Subject model)_

__Question__ model defines the question structure. Each question corresponds to a particular topic.

__Choice__ model defines the choices for a particular question. A choice corresponds to a particular question only. The correct choice will have the `value=True` else it will be false.

__Result__ model defines the score obtained by the user in a test given by him/her.


## admin.py

In the __admin.py__ we have registered all the models defined in __models.py__, so that user with admin privileges can use the admin site to create new subjects, topics, or can enter new question sets to the topics etc.

## login.html

When the app runs for the first time, login page would be loaded, where user can register with new account or login with an existing account.

When user registers for a new account, he/she is redirected to the `register_view` in __views.py__, where all the details are used to register a new user and that user is logged in and redirected to `index` view.

If a user logins with existing account, he/she is redirected to `login_view` in __views.py__ and then he/she is authenticated. If successful, the it redirects to __login.html__, else to `index` view.

`index` view checks if there is any user authenticated or not, if not then he/she is asked to login again. `index` view retrieves all the required information used for loading the __index.html__ page from the databases by running the queries and passing them as context to the __index.html__ page.


## base.html

This file acts as an layout for all the other html pages, which helps in reducing the repetition of the same code.

## index.html

When the user logs in he/she is directed to the `index` view in the __views.py__ which sends all the informaton like _subjects, topics, activities etc._ which will be displayed over the __index.html__ page.

On the main page, user have an option to search the topics which he is looking for directly. Users can see the sujects which are available. On clicking any subject user can view the topics which belongs to the subject.

Whenever user enters any text in the search area, an AJAX request is made to the `search_view` view in the __views.py__ which will return the topics which match to the text entered by the user and displays the search results on the __index.html__ page


Also the list of all the topics of various subjects is shown on the index.html page. User can select any topic which will lead him/her towards the test for that topic.


On the right side, there is an Recent activity pane, where user can keep track of their recent tests given and the score obtained in that test.

An option to logout is provided for logging out the user and an option to the switch to the Home page, which is index.html page.


## topics.html

When the user clicks on any subject in the __index.html__ page, he redirected to the `topic_view` view in the __views.py__ which loads all the topics belonging to the subject clicked by the user and then renders the information in __topics.html__ file.

In __topics.html__ file, user can then see the topics for that subject and can select any topic which will lead him/her towards the test for that topic.

## instructions.html

After clicking the topic, user is redirected to the `instruction_view` in __views.py__ where necessary information from database is fetched and rendered to the instructions.html page.


instructions.html page contains the necessary information to keep in mind before beginning the test.

After reading the instructions, user can click on __Give The Test__ link.


## test.html

After clicking the __Give The Test__ link, user is redirected to `test_view` view in the __views.py__ , where the questions belonging to the topic selected and their corresponding choices and time limit for the test is fetched and rendered to the __test.html__ page.

When the __test.html__ loads, the time limit counter starts and the test begins.

User can see one question at a time, and can navigate through the questions by clicking the button corresponding to the question no.

By default, the color of the button corresponding to the questions are __grey__, but when a choice is made by the user for a question, then the color of the button corresponding to that question changes to __green__.

There is also an option to flag the question for future changes/selection, which on selecting will change the color of the button corresponding to that question to __yellow__.

If there are any questions whose choice is not selected, then the color of the button corresponding to that question will remain __grey__.

When the time limit is reached, the test will be submitted automatically. User can also submit the test before the time limit is reached by clicking on the __Finish Test__ button.


## result.html

When the test is finished, the selections made by the user is sent to the `score_calculator` view in __views.py__, where the answers given by the user are checked with the actual answers, and score obtained the user is calculated. Alongwith this, the result is also updated in the database.

After this, marks scored by the user, the responses given by the user to the questions and the correct answers of that questions is displayed on the __result.html__ page.

Also the __Recent Activity__ is updated with the information of the marks obtained in the recently given test.


## urls.py

All the views from the views.py are imported here in __urls.py__, and path for each view is defined in here.

## style.css and login.css

It includes the necessary stylings for all the html files.


# Steps for running

## using the application.

1. Navigate to the root directory of project in terminal.
1. Enter `pip3 install -r requirements.txt`.
1. Enter `python3 manage.py runserver`
1. Now open the url displayed on terminal on a browser.

## using the admin interface.

1. Create an admin superuser.
1. Add /admin at the end of the url for opening admin interface.
1. eg. `127.0.0.1:8000/admin`.