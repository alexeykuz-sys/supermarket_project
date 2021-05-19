
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

# [](https://github.com/alexeykuz-sys/supermarket_project#fonts)Fonts

I have used Google Fonts to determine the best fonts suitable for each part of the website, I.e. Logo, Menu and Body information.

I opted to use Lato font for my website, which is one of the most popular fonts used by major internet companies.

[Top 10 Best Google Fonts](https://nestify.io/blog/top-10-best-google-fonts/)

# [](https://github.com/alexeykuz-sys/supermarket_project#icons)Icons

???????

# [](https://github.com/alexeykuz-sys/supermarket_project#colours)Colours

The colours were determined by the pallet of Cooler website:

-   For navbar #c0c650  [![navbar]()]()

-   For buttons #1d7ba9.  [![Buttons](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/static/colors/bgColor.png)](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/static/colors/bgColor.png?raw=true)

# [](https://github.com/alexeykuz-sys/supermarket_project#database-design)Database design

????


# [](https://github.com/alexeykuz-sys/supermarket_project#features-and-future-releases)Features and Future Releases

View my wireframes  [here](https://github.com/alexeykuz-sys/myRecipe-MS3/blob/master/wireframes.md). It's website with a landing page, register, log in/out and recipe editing page.  

Features to implement:

-   To add time slots choice 
-   ????

# [](https://github.com/alexeykuz-sys/supermarket_project#technologies-used)Technologies Used

**UX/UI design**

-   [Figma](https://figma.com/)

**Languages**

-   [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
-   [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)  
-   [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
-   [Python](https://www.python.org/)
-   [jQuery](www.jquery.com)

**Tools & Libraries**

-   [Git](https://git-scm.com/)
-   [Bootstrap](https://getbootstrap.com/)
-   [Icons8](https://icons8.com/)
-   [Google fonts](https://fonts.google.com/)
-   [Canva](https://canva.com/)
-   [Django](https://www.django.com/)
-   [Heroku](https://www.heroku.com/)
-   [Amazon AWS](https://aws.amazon.com/)

# [](https://github.com/alexeykuz-sys/supermarket_project#manual-testing)Manual Testing
All functions were tested for different screen sizes.
- **Landing Page**

Once website loaded, user sees the hero image, with login/register buttons and option to browse all products. Tested login and register button and link to all products page.

- **Navbar**

All page contains the navbar. Navbar contains Logo, search option and links to Profile and Shopping Bag. All links were checked.

The search section allows user to search products. User can search by the words in the name of the product or category. If such a word exists in products, the product will be shown n the screen underneath. 

Underneath the main menu, the user can click the menu list of the product categories and favourites, which were tested.

-**All Products Page**
 
All products page shows the cards of each product available in the store. Each card contains a product image, name, category, rating and the button add to the bag. Tested: product image leads to the product details page, category links offer a view of all products in the clicked category and the add to bag button adds the product to the shopping bag. The relevant notification pops up next to the shopping bag confirming user action.
The top of the page offers a link home, shows the number of available products. There is also a sort selector that sorts the product by price, name, category, in ascending and descending or alphabetical order, or price range. All links were checked and work well!

-**Single Product Page**

The single product page gives all user access to the product details, add to bag button and users reviews. 
In addition, access to product Edit and Delete functions, which appear only for logged in admin.  
I checked that Edit buttons opens the edit page, where admin only can edit all recipe fields and save recipe.
The user can choose the quantity of the product he wish to purchase and add it to the shopping bag.It was tested and works well.
The review section of the page consist of the list of all reviews left by users. Review owners can edit their reviews. Admin can delete any review left by any customer.
Add Review button opens a review form on the right side from the review list column and user can write their review and post it, after which they get notification and form disappears.
 
-**My Account**

My Account icon in the navbar opens a dropdown menu with the links to Product Management, My Profile and Logout.
The Product Management link was tested and is visible only to the website admin. and allows adding products to the store.
My profile and logout checked and are visible to all login users. My profile link opens the profile page where the user can update his delivery information and see previous orders. Logout link redirects the user to the sign-out card that either returns user to the store or signs him out from the store and redirects to the home page. 
The relevant on scree notifications pop-ups depending on the user actions


-**Shopping Bag**

The shopping bag icon appears in the navbar once the user added products to the shopping bag and shows the amount spent. In addition, a small widget pops up in the top corner of the screen, showing the user the item purchased, a button allowing the user to view the bag and the button either prompting the user to keep shopping if total spending is less than the minimum required or checkout button.
The shop has a minimum spend of £15 rule and it shows up on all checkout buttons to make sure the user can't access the checkout button unless the £15 threshold reached. Once reached the button change text to checkout and allows the user to proceed with the payment.

-**Checkout Page**

The checkout page has two columns. The left side offers the user details and delivery information, which prefilled in from the Profile page. The right side show all the products added to the shopping bag and the total cost including the delivery price. 
At the bottom of the page, the user has space to add the credit card payment details, which are not saved by the store and the user has to insert them each time he purchases in the store.
Underneath user has two options, either adjust the bag or complete the order. 
Both buttons were tested.  
Once the user presses the complete the order button he is redirected to the checkout success page with the details of the order number and total spent. The relevant email sent and receive with the order confirmation.
Back to the shop button was tested and leads back to all products page.

# [](https://github.com/alexeykuz-sys/myRecipe-MS3#testing-user-stories)Testing User Stories

User story testing:

1. Landing page.
- The page layout is simple and easy to navigate. It consists of basic colors, which do not distract visitor's attention.
- Navbar - The lLogo is clear and describes the purpose of the website. It has a link to the home page. 
Navbar menu has three options: Recipes, Register, and Log in. Each of them leads aing user to the relevantspecifi ages. The rRecipe page shows all recipes published by users. It is available for logged- in and guest users. 
Once a user has logged in, a user sees  new enu options:  Profile and Edit tis ge. The pProfile page is a simple card with user details. In the future, it will be developed into more detailed information with extra features allowing users to see their own recipes.
- Footer - simple footer that has links to social media and website slogan. All links open correct pages.
2. Log In and Log Out pages allow the user to log in/out. Log In page has required fields and check if the user inserted the correct username and password. The uUser receives screen notifications in the case user puts a wrong username or password.
3. Register page - allows users to register with a username and password. It has a requirement to put min number of symbols and a-z and 0-9.  if users insert fewer symbols, they get a warning notification. If the username already exists, the user gets a warning notification.
4. Profile page -once the user has successfully logged in, the user is redirected to the profile page. The pProfile page will be set up in the future development of the app.
5. New Recipe page -  Logged in users have access to this page. The page contains the form which the user has to be filled in. Once the user has finished and pressed the add button, the user receives a flash message of success and the screen redirected to the recipe page.
6. Logged in users also gain access to Edit and Delete buttons on thein get recipe page. Once the user decides to delete a recipe, the user receives a modal warning if he wants to delete the recipe to reconfirm the user's decision.

#### As a first-time guest visitor:

-   Upon visiting the website, I want to see the recipes available with the latest recipes at the top.
-   The navbar should be easy to find and contain links to show all recipes.
-   I should easily search recipes either by specific keywords or category: breakfast, lunch, or dinner.
-   I should expect results to show underneath the search field.
-   I should expect to be able to open each recipe and see ingredients and cooking instructionsshotsreie.

#### As a returning visitor:

-   As a returning user, interested in using the website regularly. I want to see clearly, where I can register as a user or log in.
-   Upon signing up, I am redirected to my profile page.
-   The navbar is now showing new menu options to add a new recipe.
-   Now, I can start adding my favorite recipes to the website. I should expect the add new recipe form to be comprehensive but easy to use.
-   I expect to be able to edit and delete recipes I have added to the website. Edit and Delete buttons appear on the recipe page for recipes added by the user.
-   Upon pressing the edit button, I expect to be redirected to the edit page, which is similar to add recipe button and allows edit all recipe fields.
-   Upon pressing the delete button, I expect to have the warning appear on my screen, asking if I m sure I want to delete the recipe. I expect to have it if I pressed delete mistakenlyreally wants to delete recipe to reconfirm user's decisision.

# [](https://github.com/alexeykuz-sys/supermarket_project#bugs-and-debugging)Bugs and Debugging

????

# [](https://github.com/alexeykuz-sys/supermarket_project#project-deployment)Project Deployment

I used VSCODE to build this project.

**Local Deployment**

To deploy the project to Github the following steps were taken:

Created a master branch in Github repository.
Repository was clone to VScode and local foder was created. 

**Version Control**

Used Git for version control.

**Development Environment**

All code was written on Visual Studio Code.

A virtual environment was created on VSCode to ensure that the packages installed are only installed in the virtual environment folder.
The code was then pushed to GitHub where it is stored in my Repository.
To create virtual enviroment I followed the following steps:

- Navigate to the folder of the installed files with cd <path>
- Create the virtual environment folder with python -m venv venv
- Activate the virtual environment with venv\Scripts\activate.bat

.Gitignore file was created, where i saved files that should not be pushed to Github:

core.Microsoft*
core.mongo*
core.python*
env.py
__pycache__/
*.py[cod]
node_modules/
venv
*.sqlite3
db.sqlite3
*.pyc
.env
db.json

In addition dotenv was installed to store local variables to ensure safety of the passwords.

The following variables were saved in venv file:

STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_WH_SECRET
SECRET_KEY  
DEVELOPMENT

Install project requirements by typing pip install -r requirements.txt

To deploy project and to run it locally, type python manage.py runserver in the terminal 
This will open a localhost address, which is provided in the CLI.
Either copy and paste the url shown below into a new browser tab, or hover over it and click follow link.

**Heroku Deployment**

To deploy the project to Heroku the following steps were taken:
created a Heroku account @ https://signup.heroku.com/
Create requirements.txt file in workspace for Heroku to understand installation files to run app. From CLI type type pip3 freeze --local > requirements.txt.
To install the Heroku command line on Gitpod, use the following command npm install -g heroku
Using the New buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us to push our changes using Git to update the application at any given time.
To login to Heroku from the CLI, use the command heroku login
To get the application up and running a Procfile is required that istructs Heroku which file is the entry point. Use the following command to create this: echo web: python app.py
Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands: git add . git commit -m "fist Heroku commit" git push
Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
To connect an existing repository from Github to Heroku use the following CLI syntax: heroku git:remote -a [followed by name of Heroku app]
To push to Heroku Master Branch, then simply use git push heroku master
To scale dynos and run the app in Heroku, use the CLI command: heroku ps:scale web=1
In order for the server instance on Heroku to know how to run our application, we need to specify a few Config Vars in Heroku. To do this go to Settings tab > Config Variables and input: AWS_ACCESS_KEY_ID; AWS_SECRET_ACCESS_KEY; DATABASE_URL; DISABLE_COLLECTSTATIC; EMAIL_ADDRESS; EMAIL_PASSWORD EMAIL_PASSWORD; SECRET_KEY; STRIPE_PUBLISHABLE; STRIPE_SECRET.
The following syntax will need to be added to your settings.py file to access the SECRET KEY for the new database URL DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
The Database can then be migrated to the Heroku Postgres (postgresql) database using the the commands mmakemigrations and migrate from the command line.
Once the build in Heroku is complete, click the Open app button.
Objects can then be added to the new postgres database using the Admin Panel and logging in with your superuser credentials.



# [](https://github.com/alexeykuz-sys/supermarket_project#credits)Credits

### [](https://github.com/alexeykuz-sys/supermarket_project#images)Images

The images for this app/website were taken from Unsplash:

[Ocado Zoom](https://zoom.ocado.com/)

I used Code Institute Task Follow up project as a reference and guidance in building this website


## [](https://github.com/alexeykuz-sys/supermarket_project#acknowledgements)Acknowledgements

Sites used for information and support

-   [W3C](https://www.w3.org/)
-   [Stack overflow](https://stackoverflow.com/)
-   [W3schools](https://www.w3schools.com/)
-   [CSS Tricks](https://css-tricks.com/)
-   [JS Commenting](https://jsdoc.app/about-getting-started.html)
-   [Django Documentation](https://www.djangoproject.com/)
-   [Python Documentation](https://docs.python.org/3/)
-   [Figma](www.figma.com)


#### [](https://github.com/alexeykuz-sys/supermarket_project#I-received-advice-and-support-from)I received advice and support from

-   Oluwafemi Medale (mentor)
-   Code Institute - Slack Community. (various students, tutors and mentors)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzE5NTU3MTYsNzQ3MDM5MzcsLTE3NT
M5NzYyNjAsODMxNjU3NTIzLC00MjI4MTc4NjRdfQ==
-->