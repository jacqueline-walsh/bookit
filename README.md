# BookIt - ecommerce site for books 

<img class="text-center" src="https://code-institute.s3-eu-west-1.amazonaws.com/BookIt/mac-screen.jpg">

[![Build Status](https://travis-ci.org/jacqueline-walsh/bookit.svg?branch=master)](https://travis-ci.org/jacqueline-walsh/bookit)


## UX
 
BookIt!  The online books store for book lovers across the world. Register, login, browse or search for that book you have always wanted to read.  Have a query on a particular book, you can send us a message on our contact us form.  Order your book, pay online and an email confirmation will be sent to you with confirmation of your order.  Go to the profile page to view your order history.  It's all just a click away. 

BookIt design concept is to give the user a clean modern experience with quick access to what the user needs, with search or browse functionality.  A topbar allows the user to access the registration, login and profile pages.  The main navigation provides one click links to home, about and all books.  Only registered and logged in users can see the add to cart button.  For the site owner / admin stock levels on each book is recorded and will indicate to the user when a book is out of stock and when the site owner needs to add more stock.

### Links to resources

- [Live Site](https://bookit-online-book-store.herokuapp.com/)
- [Github](https://github.com/jacqueline-walsh/bookit)
- [Wireframes](https://github.com/jacqueline-walsh/bookit/tree/master/wireframes)
- [Trello](https://trello.com/b/hiyXz2DG/bookit-book-aution-site)

### User Story

The user is a first time visitor to the site:

- User looks at the main navbar and see they are able to view the home page, about page and all books.
- User also notes that there is a top navigation bar which has a register and login link.  
- User clicks on all the about page and reads all about the site and can see who the author of the month is and with a short description.
- User sees that on the book page there are buttons to check out each individual book in detail.
- User is a big fan of Harry Potter and the author, JK Rowling, they type the author's name into the search section and click the search bar.
- User can see a selection of JK Rowling books and they click on the image for the book, The Cursed Child.
- As the user is not registered with the site they are unable to see a add to cart button but instead have a link to enable them to register and buy the book.
- User click the register link and is presented with the registration form.  Which is clear and easy to use with validation messages to help complete the form - The correctly.  They register their details and click submit.
- On registration the user is logged in automatically. 
- User can then proceed to click the button, "add to cart".
- User is directed to the view cart page.  
- User clicks the pay with cart button and completes the transaction by adding billing address, shipping address, card details and submitting the payment.
- User is directed to the thank you page with their order number.
- User receives an email, giving details of the order purchased.

<img src="https://bookit-uploads.s3-eu-west-1.amazonaws.com/img/email_order_confirmation.png" width="100%">

## Features

Each site page has been detailed individually below and all features explained.

### Home Page

This is the shop window to the site.  All users are able to access this page and at a glance be invited to explore further.  There is a carousel of books on display and quotes from a few favourite.  Below there are 3 of the newest feature books on offer that the user can click on for more information.

### About Page

The Who we are page.  All users are able to access this page.  There is a section for author of the month, where the author can be changed each month by the site admin in the admin dashboard by a simple checkbox.  A javascript image slider shows relaxing reading. 

### All Books

All books are available to all users and can be clicked on to provide the user with more information about the book.  The book page has been paginated to show 6 books per page.  

At the top of the page there is a search panel where the user can search for any book in the system by either, title, author or category.

### Book (Single Book Page)

There is an image of the book cover with individual thumbnails for the first 5 pages of the book which the user can click on and view with a lightbox gallery.

More information can be found about the book including, book Title, book description, ISBN, price, categories, author, description of author.  For users not registered and logged in there is a link inviting the user to register so they may purchase the book.  For users already registered and logged in there is a 'add to cart' button.  however if the book currently out of stock the 'add to cart' button is removed and a simple message advising the user that the books is out of stock.  All users can click on a contact us button and complete a simple form for more information on that book.  Where possible the contact for will auto-populate fields such as book title, username and email.  An email will be sent to admin to alter them that a new message has been sent.

### Shopping Cart

Only logged in users can access the shopping cart page.  This can be accessed by the user either by an icon on the top navigation bar or when the user clicks the 'add to cart' button on the book page and is directed automatically to the shopping cart page.  The users has various options on this page, either amend quantity to purchase, delete a book item, go back and continue shopping or pay with card.  The user is only able to add to cart what is in stock, so should the user order the last book the add to quantity button is removed and they are not able to by what is not in stock.  When a book is purchased the admin stock will be reduced accordingly until the book is out of stock at which time a notice will be placed on the book page, until admin updates the stock level.  

### Stripe Pay with Card

This is a stripe feature to allow the user to pay for the order by card.  This is where the user can enter, email, billing and shipping details, phone number, check the amount to pay and then enter their card details.

### Thank You Page

When user has paid for the order they will be directed to a thank you page and will also receive an email with a breakdown of their order confirmation.  


### Registration

Registration page will all fields required, validation on email and matching passwords.  An Alert message will advise the user if the username or email address already exists.  Once registered the new user is automatically loggged in and directed to the home page.

### Login

User can login with username and password.  An alert message will pop up advising the user if the username or password is incorrect.  Once logged in the user is directed to the home page.  When logged in the top navigation links change from register and login to profile and logout.  There is also a forgotton password link the user can use should they forget their password.

### Profile 

This page lists the username and email and also a link to change password.  This page also hosts the order history and gives details of all previous purchased with individual links to each order placed.

### Admin Dashboard

This section is only available to the administrator of the site.  Here the admin can add / edit / delete, books, authors, users and groups.  Admin can see contact form messages sent by the user and all orders placed.  Admin can control the stock levels, change author of the month, choose whether the book is available or not.  The admin dashboard has been customized to match with the site theme.

### Features Left to Implement

- Another feature ideas would be to implement book reviews / recommendations.  A members readers club with chat forum.

## Technologies Used

Many languages, frameworks and libraries have been used on this project:

### Repository
github - Github has been used throughout the project. At each stage throughout the development of the application the changes have been pushed to the repostory to provide a history of commits and changes of each new feature

### Frontend
Django Framework - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. [Django Framework](https://www.djangoproject.com/)
HTML5 - Semantic HTML5 has been implemented thoughout the site.
CSS3 - used for the styling of the site and to provide a more visually pleasing effect.
Javascript - For slider on about page and alert.
JQuery - the project uses JQuery to simplify DOM manipulation and for the inclusion of lightbox plugin. [JQuery](https://jquery.com/) [Lightbox Plugin](https://lokeshdhakar.com/projects/lightbox2/)
bootstrap - Bootstrap was implemented to assist with site layout and responsive design [bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
Font Awesome - visual icons have been used from Font Awesome version 5. [Font Awesome](https://fontawesome.com/)
Google Fonts - for the typeography of the site. [Google Fonts](https://fonts.google.com/)
AWS - storage for all images so to keep the site as light as possible. Also where possible all links are CDN. [AWS](https://aws.amazon.com/) 
Stripe - Payment integration system. [stripe](https://stripe.com/ie)
MailGun - Easy SMTP integration, RESTful API abstracts away the messy details of sending transactional or bulk email. [mailgun](https://www.mailgun.com/)

### Backend
SQLite - Database for local hosting and development
Postgres - Database for remote hosting and production.
Python - Language used with the Django Framework.

### Hosting
Heroku - the application has been hosted on heroku [heroku](https://heroku.com)


## Testing

Each functionality has been run and tested at each stage of development and any bugs or issues have been dealt with accordingly, before moving on to another step.  

Media queries have been used to ensure CSS is working optimally on all mobile devices.  

Unit testing has been carried out on the site successfully.

[Travis](https://travis-ci.org/) a continuous integration & continuous delivery platform has been integrated on the github page and passes all tests.  See [travis test](https://github.com/jacqueline-walsh/bookit/blob/master/site-resources/docs/Travis_test_passed.png)


### manual testing of the registration form:

    1. Go to the "Registration" page [registration](https://bookit-online-book-store.herokuapp.com/accounts/register)
    2. Try to submit the empty registration form and an alert message pops up on the first name field, "please fill in this field"
    3. Try to submit the registration form with username of 4 characters and a message pops up, "Please lengthen this text to 6 characters or more (you are currently only using 4 characters)".
    4. Try to submit an incorrect email with just the name 'julie' and an alert message pops up, "Please include an '@' in the email address, 'julie' is missing an '@'"
    5. Try to submit the form with all fields correctly completed and the username, "samSmith" and an alert message pops up, "Error username already exists"
    6. Try to submit the form with all fields correctly completed and the email, "sam@gmail.com" and an alert message pops up, "Error that email already exists"
    7. Try to submit the form with a password of "pass", and an alert message pops up, "Please lengthen this to 8 characters or more.  (you are currently using 4 characters)" 
    8. Try to complete the form with mismatch passwords and an alert message pops up, "Error passwords do not match"
    9. Try to submit the form with all inputs valid and verify that a success message appears.

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

## Deployment

Heroku has been used for the deployment of the site, see settings below for further details:

A free cloud hosting platform which simplify the deployment process.

### Heroku Settings added Config Vars

KEY | VALUE
--- | -----
DATABASE_URL | link to db |
AWS_ACCESS_KEY_ID | aws access key |
AWS_SECRET_ACCESS_KEY | aws secret key |
AWS_STORAGE_BUCKET_NAME | aws bucket name |
EMAIL_ADDRESS | email address |
EMAIL_PASSWORD | email password |
EMAIL_HOST_PASSWORD | password |
EMAIL_HOST_USER | host name |
SECRET_KEY | site secret key |
STRIPE_PUBLISHABLE_KEY | stripe key |
STRIPE_SECRET_KEY | stripe secret key |


### Deploy to Heroku via Terminal
- Go to heroku and create a new app
- In terminal carry out the following steps
    - $ heroku login
    - $ git add .
    - $ git commit -m "message for deployment"
    - $ git push heroku master
- Heroku then launches the application and provides a link to the new live site
- Go to heroku and select more tab in top right and click on Restart All Dynos
- Select tab to Open app in browser next to more tab.

## Deployment from Github to localhost

*Local deployment relies on a database connection and therefore you will need to set up your own environment*

1. Clone / download the repository at [https://github.com/jacqueline-walsh/bookit.git](https://github.com/jacqueline-walsh/bookit.git)
2. Create a virtual environment 
    - `python3 -m venv env`
3. Activate virtual environment 
    - `source env/bin/activate`
4. Install required packages:
    - `pip install -r requirements.txt`
5.  run
    - `python manage.py migrate`
6.  create admin superuser
    - `python manage.py createsuperuser`
7.  then run 
    - `python manage.py makemigrations`
8.  again run
    - `python manage.py migrate`   
9. finally, to run application:
    - `python manage.py runserver`
10. This should now run on your local environment on `http://127.0.0.1:8000/`


## Credits

### Content
- Amazon online shopping for book and author details

### Media
- The photos used in this site were obtained from ...
    - [Google images](https://www.google.com/search?q=books+images&tbm=isch&tbs=rimg:CS3g2DGFtxWhImC7IrcZTs5MBiaL7jB_1JhBZmcnATwpTTbOyIcQ-uExgfNM9ZvKLxaXAQSZr322t-pWYghj6UTg7qfLGKeVZtxPg9Eb5SqFidpueAxzgi46x08t9RwOKn1Sp5zcdUpCcHNoqEgm7IrcZTs5MBhHWe4XDtUZI4yoSCSaL7jB_1JhBZEUp4VZij5omCKhIJmcnATwpTTbMRgy-BJxHwoMUqEgmyIcQ-uExgfBGALIpe877dSioSCdM9ZvKLxaXAEZY8D2Bj2DvwKhIJQSZr322t-pUROZprjGP7fxYqEgmYghj6UTg7qREzf966UE20dyoSCfLGKeVZtxPgEYwLqjaSacBhKhIJ9Eb5SqFidpsRJv9s7XXv3OAqEgmeAxzgi46x0xHgwCgIK-SWuSoSCct9RwOKn1SpEbJuOQGO3mL4KhIJ5zcdUpCcHNoRf4mDAEgf-4o&tbo=u&sa=X&ved=2ahUKEwiDjYjFrZHlAhWGQEEAHWEmAK4QrnZ6BAgBEBc&biw=2560&bih=1209&dpr=2#imgrc=iFgNISutgL4vaM:)
    - [Amazon online shopping](https://www.amazon.co.uk/)
    - [3D Carousel](https://codepen.io/jaskiranchhokar/pen/wmGXav. -  https://www.cssscript.com/automatic-3d-image-rotator-pure-css/)
    - [Javascript slider](https://codepen.io/gabrieleromanato/pen/dImly)
    - [colour scheme](https://www.materialpalette.com/?ref=producthunt)

### Acknowledgements

- I received inspiration many different sources surfing the web, but not least of all from [Django documentation](https://docs.djangoproject.com/en/2.2/)

