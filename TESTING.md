# BookIt - Ecommerce Site for Books - Testing 

[W3C Markup Validation]( https://validator.w3.org/) was used to validate HTML


[W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS

Each functionality has been run and tested at each stage of development and any bugs or issues have been resolved, before moving on to another step.  

Media queries have been used to ensure CSS is working optimally on all mobile devices and user testing has been carried out on both desktop and mobile devices.

Python Unit testing has been run on the site successfully.

[Pylint](https://pypi.org/project/pylint/) has been installed on Visual Studio Code Editor which validates python code.

[Travis](https://travis-ci.org/) a continuous integration & continuous delivery platform has been integrated on the github page and passes all tests.


### manual testing of the registration form:

- Go to the "Registration" page [registration](https://bookit-online-book-store.herokuapp.com/accounts/register)
- Try to submit the empty registration form and an alert message pops up on the first name field, "please fill in this field"
- Try to submit the registration form with username of 4 characters and a message pops up, "Please lengthen this text to 6 characters or more (you are currently only using 4 characters)".
- Try to submit an incorrect email with just the name 'julie' and an alert message pops up, "Please include an '@' in the email address, 'julie' is missing an '@'"
- Try to submit the form with all fields correctly completed and the username, "samSmith" and an alert message pops up, "Error username already exists"
- Try to submit the form with all fields correctly completed and the email, "sam@gmail.com" and an alert message pops up, "Error that email already exists"
- Try to submit the form with a password of "pass", and an alert message pops up, "Please lengthen this to 8 characters or more.  (you are currently using 4 characters)" 
- Try to complete the form with mismatch passwords and an alert message pops up, "Error passwords do not match"
- Try to submit the form with all inputs valid and verify that a success message appears.

The site has been intensively user tested to ensure the following:

- all links are fully functioning
- validation on forms prompting and working correctly
- registration return error message if username already in database
- password and password confirm return match if same
- mobile views are in good design and order
- user experience has been an enjoyable experience with no frustration of getting lost or confused
- flash messages appear and are correctly displayed
- data is being received and stored correctly on the database
- email confirmation are recieved correctly by both admin and user

### Unit Testing

Unit testing has been carried out in order by seperation of concerns, test_urls.py, test_views.py, test_models.py and test_forms.py for each applicable component.  However, this is a new concept for the tester and future learning and research could improve this testing exercise going forward.

An overall coverage report was run on the testing with a final score of    .  To run a coverage report the following needs to be run in the terminal:
`pip install coverage`
`coverage run manage.py test`
`coverage html`

- NOTE running `coverage html` will produce a folder in the root director named, htmlcov inside this folder look for the index.html and open this in the browser.  This provides an indepth detail of all tests and gives the tester, insight on what code still needs further testing.

### Bugs and Fixes

Stripe payment has a customized bookit logo at the top of the modal payment form.  However, when images where uploaded to AWS the link to the image was broken.  It wasn't until testing that this was realised.  The image link has been amended in order to fix this bug, see image below.

<img class="text-center" src="https://code-institute.s3-eu-west-1.amazonaws.com/BookIt/bug_and_fix.jpg">

### Useful resources

[assertion methods](https://docs.python.org/3/library/unittest.html#assert-methods)
[]
