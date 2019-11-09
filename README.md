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


<img src="https://bookit-uploads.s3-eu-west-1.amazonaws.com/img/order_thank_you_page.png" width="100%">
<img src="https://bookit-uploads.s3-eu-west-1.amazonaws.com/img/email_order_confirmation.png" width="100%">
<img src="https://bookit-uploads.s3-eu-west-1.amazonaws.com/img/history_order_details.png" width="100%">


## Features

Each site page has been detailed individually below and all features explained.

### Home Page

This is the shop window to the site.  All users are able to access this page and at a glance be invited to explore further.  There is a carousel of books on display and quotes from a few favourite.  Below there are 3 of the newest feature books on offer that the user can click on for more information.

### About Page

The Who we are page.  All users are able to access this page.  There is a section for author of the month, where the author can be changed each month by the site admin in the admin dashboard by a simple checkbox.

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

This section is only available to the administrator of the site.  Here the admin can add / edit / delete, books, authors, users and groups.  Admin can see contact form messages sent by the user and all orders placed.  Admin can control the stock levels, change author of the month, choose whether the book is available or not.  

### Features Left to Implement

- Another feature ideas would be to implement book reviews / recommendations.  A members readers club with chat forum.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
