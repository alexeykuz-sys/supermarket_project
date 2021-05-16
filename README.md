
Fast and Fresh Supermarket is a ecommerce online supermarket. The website is built to allow users to access, browse and purchase the products. The website offers CRUD functionality that allows users to add, edit and delete products, favourites and reviews. The site is designed to be intuitive and easy to navigate and use, promoting a simple layout with effective and purposeful features.


**Project Requirements:**

Build an interactive front-end website that responds to user actions and alters the way the site displays data/information.

Required Technologies : HTML, CSS, JavaScript, Python, Django, Amazon 3S. 
A live version of the site is available [LIVE SITE]()  

**Contents**

1.  [UX Development](https://github.com/alexeykuz-sys/supermarket_project#ux-development)
    
2.  [Project Goals](https://github.com/alexeykuz-sys/ms4-ecommerce#project-goals)
    
3.  [UX Requirements](https://github.com/alexeykuz-sys/supermarket_project#ux-requirements)
    
4.  [Developer's goal](https://github.com/alexeykuz-sys/supermarket_project#developers-goals)
    
5.  [Users](https://github.com/alexeykuz-sys/supermarket_project#users)
    
6.  [User Goals](https://github.com/alexeykuz-sys/supermarket_project#user-goals)
    
7.  [User Stories](https://github.com/alexeykuz-sys/supermarket_project#user-stories)
    
8.  [Design Choices](https://github.com/alexeykuz-sys/supermarket_project#design-choices)
    
    -   [Fonts](https://github.com/alexeykuz-sys/supermarket_project#fonts)
    -   [Icons](https://github.com/alexeykuz-sys/supermarket_project#icons)
    -   [Colours](https://github.com/alexeykuz-sys/supermarket_project#colours)
    - [Database design](https://github.com/alexeykuz-sys/supermarket_project#database-design)
    -   [Features and Future Releases](https://github.com/alexeykuz-sys/supermarket_project#features-and-future-releases)
    -   [Technologies used](https://github.com/alexeykuz-sys/supermarket_project#technologies-used)
9.  [Manual Testing](https://github.com/alexeykuz-sys/supermarket_project#manual-testing)
    
10.  [Testing User Stories](https://github.com/alexeykuz-sys/supermarket_project#testing-user-stories)
    
11.  [Bugs and De-bugging](https://github.com/alexeykuz-sys/supermarket_project#bugs-and-debugging)

 12.  [Project Deployment](https://github.com/alexeykuz-sys/supermarket_project#project-deployment)
    
13.  [Credits](https://github.com/alexeykuz-sys/supermarket_project#credits)
    
14.  [Acknowledgements](https://github.com/alexeykuz-sys/supermarket_project#acknowledgements)



====

# [](https://github.com/alexeykuz-sys/supermarket_project#ux-development)UX Development

Fresh and Fast website will help users to have online access to their groceries and to be able to purchase them and have them delivered withn 30 min.
The primary goal of the website is to have easy access to grocery store.

# [](https://github.com/alexeykuz-sys/supermarket_project#project-goals)Project goals

The purpose of this project is to create website that allow users to access, use, choose, add, edit and delete, order products from onlinse supermarket. In addition, users can create the list of their favourite products, to have a quick access to their favourite products. Users can leave the reviews for the previously purchased goods.
The website has to be easy to navigate and use, with clear purpose of the buttons and screen space.

# [](https://github.com/alexeykuz-sys/supermaket_project#ux-requirements)UX requirements

The website targets the users that dont want to spend time in the shop and prefer to have easy access to all products. They want to have fast and clear navigation pane that includes the user's favourite products to be able to purchase them with max of 3 clicks. 
# [](https://github.com/alexeykuz-sys/supermarket_project#developers-goals)Developer's Goals

The site owner has the following goals:

-   To provide users with clean and easy way to see all products
-   To give users control over the categories of products they want to see.
-   To give users control over which products they want to see as favourite.
-   To give users visual notifications of their successful or failed actions.
-   To give users possibility to pay for the products they wish to purchase.

# [](https://github.com/alexeykuz-sys/supermarket_project#users)Users:

It became a norm to purchase goods online. There is no limitation to users able to use this website.

# [](https://github.com/alexeykuz-sys/supermarket_project#user-goals)User goals:
The users goal is to identify application allowing them to have enjoyable and easy online shopping experience.
# [](https://github.com/alexeykuz-sys/supermarket_project#user-stories)User Stories

**- First Time Visitor Goals:**

1.  As a visitor to the website, I want to easily understand the main purpose of the website.
2.  As a visitor easy to register and login/out
3.  As a visitor I want to see all the products on the screen
4.  As a visitor i want an easy to sort products by categories.
5.  As a visitor i want an easy to search specific products.
6.  As a visitor i want to be able to access individual products, to see product description and reviews.
7.  As a visitor i want an easy to to add products to the shopping bag either from the list of all products or after checking the details of the product.
8.  As a visitor i want to be able to increase or decrease number of each product i wish to purchase or remove completely with one click.
9.  As a visitor I want to be able to see clear price of eah product, total cost of the shopping bag and shipping cost.
10. As a visitor I want to have simple, effective and secure payment.
11. As a visitor I want to have my own profile page with the shopping history.
12. As a visitor I want to receive onscreen or email notifications confirming my succes or failure of my actions.


**- Returning Visitor Goals:**

1.  As a returning Visitor I would like to see better variety of the products.
2.  As a returning Visitor I would like to have a better choice of payment methods.


# [](https://github.com/alexeykuz-sys/supermarket_project3#design-choices)Design Choices

When designing website I took inspiration from various shopping websites like Sainsbury and Ocado Zoom. The website was adapted to fit user requirements. 
The webpages consist of :
1.  The website is built mobile first principle.
2.  Navbar - navbar has two lines layout. Top part of the navbar provides access to My Account, search bar and shopping bag. Lower part offers users direct access to the different categories and favourite products. Navbar is visible on all pages.
3.  All Products Page - single page representing all products availalble in the shop with possibility to add each of them to the shopping bag or to review individual products.
4.  Individual product page - each product page has the product image, name, category, rating, quanity bar and add to bag button, product description, reviews, add to favourites button and return to all products page button.
5.  Login/Register Page  - user has to input username  password that are restricted to min and max number of characters.
6.  Profile Page - user profile page, basic information and previous shopping history.
7.  Shopping bag page - shopping bag provides the list of all products to be purchased and separate part showing the total cost of the shopping bag, delivery cost and total charge. It is possible to edit shopping bag, i.e. edit the items quantity, delete items from the bag.
8.  Checkout page - checkout page, provides user infirmation and delivery address, credit card details and total amount to be charged.
9.  Checkoutsuccess page provides user with the summary of the purchased products, invoice number and email confirmation.
10. The website provides user with various widget notifications, giving user positive visual experience and simplify navigation and shopping expereinccreate recipes


# [](https://github.com/alexeykuz-sys/supermarket_project#users)Users:


# [](https://github.com/alexeykuz-sys/supermarket_project#user-goals)User goals:

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzE5NTU3MTYsNzQ3MDM5MzcsLTE3NT
M5NzYyNjAsODMxNjU3NTIzLC00MjI4MTc4NjRdfQ==
-->