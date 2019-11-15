# BookIt - Ecommerce Site for Books 

<img class="text-center" src="https://code-institute.s3-eu-west-1.amazonaws.com/BookIt/mac_screen.jpg">

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

<img class="text-center" src="https://bookit-uploads.s3-eu-west-1.amazonaws.com/img/email_order_confirmation.png">

## Features

Each site page has been detailed individually below and all features explained.

### Home Page

- shop window to the site
- all users are able to access this page and at a glance be invited to explore further.  
- a carousel of books on display and quotes from a few favourite
- 3 of the newest feature books on offer 
- click on a feature book for more information

### About Page

- all users are able to access this page.  
- author of the month section. Author can be changed each month by the site admin in the admin dashboard by a simple checkbox.  
- javascript image slider shows relaxing reading. 

### All Books

- all books are available to all users 
- click on a book or button to see individual book page  
- book page has been paginated to show 6 books per page
- search section.  All books can be search by book title or filtered by author or category.


### Book (Single Book Page)

- all users can access the invididual book page
- image of the book cover 
- JQuery lightbox gallery provides individual thumbnails for the first 5 pages of the book
- book title, book description, ISBN, price, book categories, author and description of author provided. 
- only registed and logged in users can access "add to cart" button.
- if no stock available logged in user will see message advising the book is out of stock 
- users not registered are invited to register via a link so they may purchase the book.  
- contact us button for all users.  If user logged in contact form will auto-populate fields such as book title, username and email 
- an email will be sent to admin to alter them that a new message has been sent.

### Shopping Cart/Checkout

- delivery details such as billing and shipping address are all handled via the stripe payment
- only logged in users can access the shopping cart/checkout page  
- page is accessed by logged in user when item is added to cart either on topnav bar or when user selects "add to cart" button. 
- users has various options on this page: 
    - amend item quantity 
        - user can only add to items when stock available.  If no further stock available the add button is removed
    - delete a book item 
    - go back and continue shopping
    - pay with card 

### Stripe Pay with Card

- this is where the user can enter their details as follows:
    - email 
    - billing and shipping address
    - phone number 
    - double check the amount to pay 
    - enter card details

### Thank You Page

- when user has paid for the order they will be directed to a thank you page 
- the user will receive an email confirming there order has been placed  


### Registration

- all fields are required 
- email validation to detect a valid email pattern
- validate password and confirm password match.  
- alert message will advise the user if the username or email address already exists  
- registered user is automatically loggged in

### Login

- login with username and password.  
- alert message will advise user if the username or password is incorrect  
- when user logged in the top navigation bar changes from register and login to profile and logout.  
- a forgotton password link should user forget password

### Profile 

-  details username and email 
- a link for user to change password  
- order history details with link to invidual orders

### Admin Dashboard

- available only to the administrator of the site  
- admin can add / edit / delete, books, authors, users and groups  
- contact form messages can be reviewed by admin
- order details can be reviewed by admin
- stock levels can be edited
- author of the month changed
- select if the book is available 
- customized dashboard to match with the site theme

### Features Left to Implement

- Another feature ideas would be to implement book reviews / recommendations.  A members readers club with chat forum.

## Technologies Used

Many languages, frameworks and libraries have been used on this project:

### Repository
github - Github has been used throughout the project. At each stage throughout the development of the application the changes have been pushed to the repostory to provide a history of commits and changes of each new feature

### Frontend
- Django Framework - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. [Django Framework](https://www.djangoproject.com/)
- HTML5 - Semantic HTML5 has been implemented thoughout the site.
- CSS3 - used for the styling of the site and to provide a more visually pleasing effect.
- Javascript - For slider on about page and alert.
- JQuery - the project uses JQuery to simplify DOM manipulation and for the inclusion of lightbox plugin. [JQuery](https://jquery.com/) [Lightbox Plugin](https://lokeshdhakar.com/projects/lightbox2/)
- bootstrap - Bootstrap was implemented to assist with site layout and responsive design [bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- Font Awesome - visual icons have been used from Font Awesome version 5. [Font Awesome](https://fontawesome.com/)
- Google Fonts - for the typeography of the site. [Google Fonts](https://fonts.google.com/)
- AWS - storage for all images so to keep the site as light as possible. Also where possible all links are CDN. [AWS](https://aws.amazon.com/) 
- Stripe - Payment integration system. [stripe](https://stripe.com/ie)
- MailGun - Easy SMTP integration, RESTful API abstracts away the messy details of sending transactional or bulk email. [mailgun](https://www.mailgun.com/)

### Backend
- SQLite - Database for local hosting and development
- Postgres - Database for remote hosting and production
- Python - Language used with the Django Framework

### Hosting
Heroku - the application has been hosted on heroku [heroku](https://heroku.com)

## Testing

See [TESTING.md](https://github.com/jacqueline-walsh/bookit/blob/master/TESTING.md) file

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

