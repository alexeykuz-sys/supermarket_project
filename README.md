
Fast and Fresh Supermarket is a ecommerce online supermarket. The website is built to allow users to access, browse and purchase the products. The website offers CRUD functionality that allows users to add, edit and delete products, favourites and reviews. The site is designed to be intuitive and easy to navigate and use, promoting a simple layout with effective and purposeful features.

![(https://github.com/alexeykuz-sys/supermarket_project/blob/master/static/pics/amiresponsive.PNG)
](https://github.com/alexeykuz-sys/supermarket_project/blob/master/static/pics/amiresponsive.PNG)


**Project Requirements:**

Build an interactive front-end website that responds to user actions and alters the way the site displays data/information.

Required Technologies : HTML, CSS, JavaScript, Python, Django, Amazon 3S. 
A live version of the site is available [LIVE SITE](https://ms4-supermarket-project.herokuapp.com/)  

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
    -   [Colours](https://github.com/alexeykuz-sys/supermarket_project#colours)
    -   [Database design](https://github.com/alexeykuz-sys/supermarket_project#database-design)
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

# [](https://github.com/alexeykuz-sys/supermarket_project#colours)Colours

The colours were determined by the pallet of Cooler website:

-   For navbar #c0c650  [![navbar](https://github.com/alexeykuz-sys/supermarket_project/blob/master/static/pics/acid_green.PNG)](https://github.com/alexeykuz-sys/supermarket_project/blob/master/static/pics/acid_green.PNG)

-   For buttons #1d7ba9.  [![Buttons](https://github.com/alexeykuz-sys/supermarket_project/blob/master/static/pics/celadon_blue.PNG)](https://github.com/alexeykuz-sys/supermarket_project/blob/master/static/pics/celadon_blue.PNG)

# [](https://github.com/alexeykuz-sys/supermarket_project#database-design)Database design

Database design is [here](https://github.com/alexeykuz-sys/supermarket_project/blob/master/static/pics/supermarket-dbdesigner.pdf)


# [](https://github.com/alexeykuz-sys/supermarket_project#features-and-future-releases)Features and Future Releases

View my wireframes  [here](https://github.com/alexeykuz-sys/supermarket_project/blob/master/wireframes.md).  

Features to implement:

-   To add time slots choice 
-   Sale items,
-   Free delivery option


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
-   [Google fonts](https://fonts.google.com/)
-   [Canva](https://canva.com/)
-   [Django](https://www.django.com/)
-   [Heroku](https://www.heroku.com/)
-   [Amazon AWS](https://aws.amazon.com/)

# [](https://github.com/alexeykuz-sys/supermarket_project#manual-testing)Manual Testing

All functions ad responsiveness were tested for different screen sizes.

**Navbar**

All Navbar links are coded within the navbar.html and main-nav.html that extends to each html page. The logo is a home link that has been tested and each link (e.g.Product Management, Register, Login; Shopping Bag, Profile, Logout) works correctly. Each link directs the user to the relevant page and the Logout button logs the user out of the site.

**Search Bar**

The Search bar is used to search all available products on the homepage. The search bar is located between logo and my account icon and available on each individual page. Mobile view has search icon, upon click of which search bar opens up.
The search bar returns items that are related to the search parameters, otherwise no items will be returned. This function works correctly.

**All Products Page**

Each product card contains links to edit productm, delete product and add to bag. Each link works and directs user to relevant page. Delete product link triggers a pop up window to reconfirm deletion and avoid accidental deletion of the product.

**Individual Product Page**

The page containts:
- Keep Shopping button that returns user to all products page.
- Category, Edit and Delete links that were tested and work as expected.
- quantity bar - user can choose how many items he wants to purchase. Tested and it works in the range of 1 to 99. The relevant plus and minus buttons get disabled once min and max allowed number has been reached.
- Add to bag buttons - adds chosen number of products to the shopping bag
and relevant widget pops up to confirm the action.


**Add Review Buttons**

Within each product page users can see all reviews. It has been tested and returns all the user reviews and ratings in chronological order.
Add review buttons opens up review form on the side of the page, where user can leave their reviews.
Each review contains Edit and Delete links. Review owner can edit review only. Review owner and Admin can delete reviews.
Review form disappears once review has been submited.

Each Customer review returns the Name, Review and the Date. All of these fields are stored in the Django database and linked to the individual product by the Foreign Key and Primary Key. 

**Shopping Bag**

The shopping bag page displays the products that the user has selected to purchase and the total shopping price. The user can amend the quantity of the products to be purchased using the quantity field. The total shopping price updates automatically with the change of the quantity. To remove product from the shopping bag user has to press Remove button. This function has been extensively tested.  
The Checkout button activates once user reach min spend limit and directs the usher to the Checkout page and the Keep Shopping button takes the user back to the Homepage. All items in shopping bag remains saved in the Cart.


**Checkout Page**

The Checkout page displays the products that the user has selected to purchase, their related quantities and prices, and the total shopping price. These elements have been tested and return the correct figures.

**Checkout - User Details Form**

checked that the form returns the information from the user profile page and does not allow user to proceed with payment unless required fields are filled out.

**Checkout - Payment Card Info Form**

The user is able to input their credit card information to purchase the selected quantities of products. This function has only been tested using Stripes dummy card information that consists of credit card number 4242424242424242.
This functionality has been tested and can be checked in the /admin/home/checkout/orders/ section of the Admin panel. These payments are also visible on the https://dashboard.stripe.com/payments page. It was tested with various webhooks and was confirmed that all the payments have been passed through the system. The payment will not submit through the Submit Payment button if the card information is incorrect or user information is not complete.

**Checkout - Submit Payment Button**

Submits the Payment and redirects the user to the checkout success page with the order details and order number. It also confirms that relevant invoice has been sent to user's email. The user then can go back to the shop by using back to the shop button.

**My Account**
My account tab directs user to Product Management page(available to users ith admin rights), My Profile, Registration, Login and Logout pages.

**Product Management page**

The admin can add products using this page. All fields were tested.

**My Profile Page**

This form allows the usher to update their delivery information. This information will be stored under the 'User' information in the Django database and can be utilised to pre-populate fields in the Checkout page.


**Registration Form**

In the Registration Page the user can set up an account by inserting a Username, Email Address, Password and Password Confirmation. The form automatically cross checks the the validity of the Email Address and Password Confirmation. There is an optional link for the user to Sign In if they already have an account.

**Login Page**

A user who has already registered can log in to the site either via the Log in Navbar menu item or on homepage using login button. 
This page authenticates the user against those stored in the database. A verified user will be logged in otherwise the relevant errors will be presented. There is a Forgotten password link and a link for a user who is not registered.

**Password Reset Page**

if a user has previously registered to the site they can insert their email address into the field and reset their password. An email is sent via smtp.gmail.com to the users email address. This functionality has been tested utilising multiple email addresses. The link in the email allows the user to create a new password and confirm. Once completed the user has to click button to be redirected back to the Login Page where they are able to login with thier email address or user name and password.This function has been rigorously tested.

**AWS S3**

The AWS S3 allows access to stored files within the site owners AWS bucket that are shared through the users AWS account. The testing of this functionality is shown in the availability of the stored data in the post prodution database andsite.

**W3 Html Validator**

All .html files were checked with the above validator.

**W3C CSS Validator**

css was checked with css validator

**PEP8 Online**

The (.py) files were checked using http://pep8online.com/


# [](https://github.com/alexeykuz-sys/supermarket_project#testing-user-stories)Testing User Stories

User story testing:

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


#### As a first-time guest visitor:

-   Upon visiting the website, I want to see the products available in the shop
-   The navbar should be easy to find and contain links to search bar and my account.
-   I should easily search products either by specific keywords or category.
-   I should expect results to show underneath the search field.
-   I should expect to be able to open each product and see its detailed description.
- I should easily add product to the shopping bag and choose the quantity
#### As a returning visitor:

-   As a returning user, interested in using the website regularly. I want to see clearly, where I can register as a user or log in.
-   Upon signing up, I want to see my favourite products

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
- Create a Heroku account at https://signup.heroku.com/

- In Heroku click the New buton and create a new app with apropriate title and choose region closest to user.

- Once the app is created click on the Resources button and choose the Heroku Postgres(free) to attach a postgres database to your project.

- To use Postgres user need to install in local enviroment one need to install dj-databas-url to connect with PostgreSQL and Psycopg2(PostgreSQL adapter)

```
pip install dj-database_url, Psycopg2
```

- Create requirements.txt file in workspace for Heroku to understand installation files to run app. 
```
pip freeze > requirements.txt.
```
- To connect to database Postgres in Heroku, user need to make the following changes in settings.py:

1. Import dj_database_url
```
import dj_database_url
```
2. To comment out

```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

and insert:

```
DATABASES = {
        'default': dj_database_url.parse(insert db  url from heroku config variable)
    }
```
Now, we can connect to Herku db and run migrations

```
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate
```

- The next step is to transfer database to Heroku using the following commands:

```
python manage.py loaddata categories.py
python manage.py loaddata products.py
```

- Once DB has been transfered we need to create superuser(admin)in Heroku
```
python manage.py createsuperuser
```
- The next step us to delete the herku DB url and uncomment django db url to make sure our database is not commited to github. Once its done please commit and push to github.

- After commiting we can use if statement to make sure that local Database used in local development and Postgress in Heroku

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

- To add Gunicorn which will act as webserver and freeze it

```
pip install gunicorn
pip freeze > requirements.txt
```
- Create Procfile to tell Heroku to create web dyno, which will run gunicorn and serve our Django app

```
web: gunicorn supermarket_project.wsgi:application
```

- To login to Heroku from the CLI, use the command
```
heroku login
```
- We need to disable static to prevent heroku to collect static files from our project, in CLI:
```
heroku config:set DISABLE_COLLECTSTATIC = 1 --app YOUR APP NAME
```
- To add heroku host address to allowed hosts in settings.py

```
   ALLOWED_HOSTS = ['ms4-supermarket-project.herokuapp.com', '127.0.0.1']
 ```
- Next step is to deploy app in heroku first by commiting to github and then to heroku using:
```
heroku git:remote -a NAME OF PROJECT
git push heroku master
```

- In Heroku to connect to github and enbla automatic deployment.
- To add SECRET_KEY in HEROKU and in settings.py

```
SECRET_KEY = os.environ.get('SECRET_KEY', '')
```
and set DEBUG to True if DEVELOPMENT in os
```
DEBUG = 'DEVELOPMENT' in os.environ
```
and commit again.

- To store static files an images we can create account and use Amazon service S3:
1. in Amazon S3 create new bucket
2. uncheck block all public access and acknowldge it public.
3. create bucket
4. create static website hosting and insert(index.html and error.html and save)
5. permissions tab
5.1. CORS configuration
5.2. Policy tab - create S3 Bucket Policy( principal *, Actions - Get Object)
5.3. Copy ARN from CORS to permission and create policy
5.4.  Copy policy into Bucket Policy and save
5.5. Access control - Everyone
6. Go to Amazon AIM service
6.1. Create Group
6.2. Click policies and in JSON tab to import S3 full access policy and copy and paste bucket ARN into json resources tab twice.
6.3. Click review policy and add name and description and then click create policy.
6.4. attach policy to the group.
6.5. Create user and attach to the group.
7. Download .csv file containing access and secret access key.

- After creating AWS service we can connect it to Django and Heroku

We need to install two packages:
```
pip install boto3
pip install django-storages
```
and freeze it and add 'storages' to Install APPS in settings.py


- In Heroku to enter in all your variables into Heroku's Config Vars.
```
AWS_SECRET_ACCESS_KEY	
AWS_ACCESS_KEY_ID	
USE_AWS
```

inside the Django setting.py you need to set up the AWS configs so the static files could be connected to AWS

```

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'ms4-supermarket-project'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
else:
    STATIC_URL = '/static/'
    STATICFILES_DIRS =(os.path.join(BASE_DIR, 'static'),)

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Remove collect static in heroku variables and in local development to create folder 'custom_storages.py and insert:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
Then to push to Heroku and we will see in the log that all static files were collected succesfully an we will see folders created in S3.

- Next step is to upload media files in S3
1. Create folder Media
2. Select all files and choose all images
3. Click next and in manage public permission to choose to add public access and upload.

- In admin we need to confirm superuser email address

- In Heroku to add stripe variables

- With all this complete the project is fully deployed.

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
