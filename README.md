# [Space Travel Agency](https://space-travel-agency.herokuapp.com/)
![Preview image]()

Who hasn’t looked at the stars and thought, I wonder what it’s like out there.
Now with XXX you can see for your self.

XXX is a full stack e-commerce web application for a fictitious space travel company, where users can book several trips outside of earth, e.g to the moon or to a space hotel.
The site offers different travel destinations and has an online shop.

This website is for educational purposes only. Don’t use real credit card details, instead use the following details for testing purposes:
Card number: 4242 4242 4242 4242 
Use any expiration date (month/year) in the future and any CVC code. 

This website is the fourth ‘Milestone Project’ as part of the Full Stack Development course of Code Institute, which is about Full Stack Frameworks with Django. The focus lies on using the Django framework, using an authorisation and authentication system and using Stripe for payments.

#### A live website can be viewed [here](https://space-travel-agency.herokuapp.com/)

# Table of Content
- [User Experience (UX)](#user-experience-ux)  
	* [Strategic level](#strategic-level)
        * [User stories](#user-stories) 
	* [Scope level](#scope-level) 
        * [Requirements](#requirements) 
	* [Structure level](#structure-level)
        * [Interaction Design and Information Design](#interaction-design-and-information-design)
        * [The pages](#the-pages) 
	* [Skeleton level](#skeleton-level)
        * [Wireframes](#wireframes)
	* [Service Level](#service-level)
        * [Colors](#colors)
        * [Typography](#typography)
- [Features](#features)
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    * [Languages](#languages-used)
    * [Frameworks and libraries](#frameworks-and-libraries-used)
    * [Tools and Programmes](#tools-and-programmes-used)
- [Testing](#testing)
- [Deployment](#deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
    * [Forking this GitHub Repository](#forking-this-github-repository)
    * [Cloning this GitHub Repository](#cloning-this-github-repository)
    * [Setup local deployment](#setup-local-deployment)
- [Credits](#credits)

***
# **User Experience (UX)**
## **Strategic level**

I’ve always been interested in space and inspired by the recent space flights (Bezos, Branson, Musk), I came up with the idea for a future commercial space travel company that offers various space trips. 
Users can choose from various destinations: a trip around the earth, a space walk, a trip to a space hotel, a trip around the moon, a trip to mars.
Users can create an account to safe orders or travel details.

The target audience are people that want to go to outer space, who want to want to travel outside of earth and experience traveling in space or feeling weightlessness. 
These can be first time users, people who have never been to space and want to experience this. Or returning users, for instance people who have been to space and want to go a step further.

The primary goal is to provide an intuitive, interactive web app, which provides users with a platform to book a space trip. 
The secondary goal is to sell space travel related products. 
The project goals are showing my knowledge and applying my added skills that I’ve learned, such as Django.

### **User stories:**  
See userstories...

## **Scope level**
Based on the user stories I’ve deducted on the following requirements:

**Requirements**
1. A home page with navbar and CTA.
2. A responsive design.
3. A page where all travels are displayed.
4. An option to register and login/logout.
5. Defensive programming, e.g. confirmation on buying, deleting, logging out, etc.
6. A profile page where registered users can log in, add, edit and delete personal information.
7. A shop page.
8. An about page where users can get more information about the company and/or the trips.
9. A contact page with contact form where users can contact the site’s owner.
10. Individual pages for travels and products.
11. Indication/banner for offers or deals, maybe a discount code.
12. A shopping cart icon with relevant info that is displayed at all times.
13. An admin page with options to Create, Read, Edit and Delete (CRUD)travels/products.
14. An option to search the site.
15. An option to filter or sort.
16. An indication of search term and numbers of results.
17. A checkout page with details on the shopping items.
18. An option to adjust items in the shopping bag.
19. Secure checkout via Stripe payment.
20. Email confirmation on purchase.

**extra requirements**
1. An option to subscribe to a newletter.
2. An option to delete a profile.
3. An option to recover the password.
4. The option to see reviews on travels/products.
5. The option to Create, Read, Edit and Delete (CRUD) own reviews.

## **Structure Level**
### **Interaction Design and Information Design**
The overall look is kept the same on each page as much as possible, to enhance single-use-learning:
- The header and footer are kept mostly the same on each page.
- Buttons are styled in the same way.
- The layout is consistent inside each page.
- The use of colours are kept the same on each page.

The navigation is kept simple and consistent:
- responsive navigation bar at the top of the page.
- A landing page with clearly indicating the options and information for first time users.
- The logo at the top of the page is also the link to the home page.
- Buttons can be used to navigate.

The information provided should be easily visible:
- Visual aids are used, like icons and complementary colours.
- The amount of information is kept to a minimum.
- The user gets an indication of which page they are, e.g. by using headers.

The user is given feedback, in order to enhance a pleasant user experience:
- The user gets a visual feedback during certain actions (e.g. focussing on, clicking on, hovering over buttons and links).
- Messages(toasts) are used to confirm or inform about current actions.
- Modal pop ups are used as defensive programming, i.e. prompting the user if they are sure of their action.
- The user get's a feedback when an error has occurred (via warning text or error handlers). In case of error handlers there is a button that leads back to the home page.

### **The pages**
        FRONTEND  
The website has xx pages, plus 3 error handler pages. Each page will have a navbar and a footer, except for the error handler pages.
The links in the navigation bar are shown depending on whether a user is logged in or not and if the user is the admin or not.
The main navigation bar has links to home, trips, shop, about, account, shopping basket and search.
When a user is logged in, the register and login links are hidden and a profile link and logout link are shown.
When the user is admin, an extra link for site managing is shown.  

The footer has a section with contact details, an overview of some important links and links to socials.

#### Description of the pages

- **The landing page/home page:** *(index.html - route: /, /home)*  
The main page has the main navbar. Below that is a hero image and a short explanation for the site. 

- **The 403 error handler page:** *(403.html - errorhandler: 403)*  
This page is shown in case of forbidden access.

- **The 404 error handler page:** *(403.html - errorhandler: 404)*  
This page is shown in case no page is found.

- **The 500 error handler page:** *(403.html - errorhandler: 500)*  
This page is shown in case of an internal service error.


Below is a chart of the webpages and their mutual connections:  
![pages chart]()

        BACKEND 
During development the Sqlite3 database is used. This is the default database used by Django.
During production PostgreSQL is used in conjunction with deployment on Heroku.

Explanation of the models used?
Chart of the models used.


## **Skeleton Level**
### Wireframes
- [Wireframes for Home Page](https://github.com/chizzletaz/BakeAndBinge/blob/main/README/wireframes/landing.pdf)  



## **Service Level**

### **Colors**
To ensure that colours match well, I've chosen to use the colours of Materialize.  
In food, bright colours signify flavours such as sweets and desserts - pink is expecially associated with baking and sweets.  
Therefore the main colour is pink. As a contrasting colour I've chosen green.

![colourB&B](https://github.com/chizzletaz/BakeAndBinge/blob/main/README/images/coloursB&B.png)  

- ![#ff4081](https://via.placeholder.com/15/ff4081/000000?text=+) #ff4081 is used as the main colour and is the pink accent-2 colour of Materialize.
This colour is used for buttons that have to stand out, shadow-text and the underline of the links upon hovering.  
- ![#fce4ec](https://via.placeholder.com/15/fce4ec/000000?text=+) #fce4ec is the pink lighten-5 colour on Materialize. This colour is used for the background of the modals.    
- ![#009688](https://via.placeholder.com/15/009688/000000?text=+) #009688 is the standard button colour of Materialize. I've kept this colour for the less important buttons (the submit button in the footer and the info button on the profile page).  
- ![#80cbc4](https://via.placeholder.com/15/80cbc4/000000?text=+) #80cbc4 is the teal lighten-3 colour on Materialize. This colour is used for the background colour of the flash messages.
- ![#fefefa](https://via.placeholder.com/15/fefefa/000000?text=+) #fefefa is used as the background colour. It is a slightly off white colour and emphasizes a simple and clean design.  
- ![#66bb6a](https://via.placeholder.com/15/66bb6a/000000?text=+) #66bb6a is used for the border of the edit buttons.  
- ![#d32f2f](https://via.placeholder.com/15/d32f2f/000000?text=+) #d32f2f is used for the border of the delete and cancel buttons.  

### **Typography** 
For the title(h1) and the logo, I've used .  
> ![example of kaushan script text](https://github.com/chizzletaz/BakeAndBinge/blob/main/README/images/kaushan-script.png)  

To keep the design consistent, I've decided to use 

---
# **Features**
# TO BE EDITED
## **Existing Features**

- **Responsiveness** on all viewports, which allows users to use the website on all devices.
- A **navigation bar**, which allows users to easily navigate the website. On devices below 992px, the navbar collapses into a hamburger menu, to reduce the real estate and to create a cleaner, calmer look.
- A **subscription option**, which allows users to subscribe to the newsletter, by entering their email address in the subscribe card. 

- **Recipe cards**, which allow users to see information about a recipe. By clicking on the recipe, the user is redirected to the recipe page.
- **Register functionality**, which allows users to create an account, by filling in the register form. 
- **Login functionality**, which allows users to log in their account, by filling in the login form. 
- **Logout functionality**, which allows users to log out of their account, by clicking the logout button.
- A **CTA (Call to Action button) button**, which allows users to register to the website (incase they don't have an account yet).
- A **search bar**, which allows users to search recipes, by entering a keyword into the search bar.
- **Category buttons**, which allow users to filter recipes by category, by clicking on the corresponding button.
- **Error handler pages**, which handle *'forbidden access'*, *'page not found'* and *'internal server'* errors, by giving users information on the error that has occurred and redirect the user back to the home page.
- A **collapsible**, which allows users to get more information about a product on the shop page, by clicking on the three dots icon.

**Modals** 
- A modal for how to add a recipe, which gives users information on how to add a new recipe.
- A confirmation modal as a defensive programming tool, which allows users to confirm to delete a recipe or category (in case of admin) or to log out.

**Icons**
- Social media icons, which allow users to go to the corresponding social platform, by clicking on the social icon.
- Icons as a visual aid, which allow users to quickly and intuitively see what is meant. E.g. a cross-icon to signify a delete function, a plus-icon to signify to add a recipe or category or an @-icon to enter an email address.

**Forms**
- A form that allows users to get in contact with the website owner, by filling in the form.
- A form that allows users to add a new recipe, by filling in the form on the add-recipe page.
- A form that allows users to edit a recipe, by editing the prefilled recipe form on the edit-recipe page.
- A form that allows the admin to add a new category, by filling in the form on the add-category page.
- A form that allows the admin to edit a category, by editing the prefilled form on the edit-category page.

**CRUD (Create, Read, Update, Delete) functionality**  
*Create:*  
- Admin can create new trips and products.  

*Read:*  
- All users can search and view trips and products.  

*Update:*
- Admin can edit trips and products.

*Delete:*
- Admin can delete trips and products.

## **Features left to implement**
- **Rating/liking products and trips** by users.
- **Sharing option** via social media, email or other ways of communication.
- A **favourite option**, so users can save their favourite trips andor products on their profile page.
- **Deleting a profile**, when a user doesn't want to use the account anymore.
- **Pagination**, in case the number of recipes gets too large. It would be more user friendly to have pagination.
---
# **Technologies used**

### **Languages used**  
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup.  
- [CSS](https://en.wikipedia.org/wiki/CSS) for styling.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) for interactivity.
- [Python3](https://www.python.org/) for backend programming.

### **Frameworks and libraries used**   
- [Bootstrap v5.1.0](https://getbootstrap.com/) a frontend-framework with precoded code-snippets, like navigation bar, modals, and to help with the responsiveness of the website.
- [jQuery](https://jquery.com/), a javascript library for easier DOM traversing and manipulation and shortening of javascript. 	
- [Google fonts](https://fonts.google.com/) for the fonts used on the website. 
- [Font Awesome](https://fontawesome.com/) for the icons used on the website. 
- [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. 
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) is a fast, expressive, extensible templating engine for Python.

### **Tools and Programmes used**
- [Balsamiq](https://balsamiq.com/) for making the wireframes. 
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
 to debug and checking/testing the website.
- [Git](https://git-scm.com/) for version control.  
- [GitHub](https://github.com/) for storing the files and version control of the website.  
- [Visual Studio Code](https://code.visualstudio.com/) for coding (IDE) the website.
- [PostgreSQL](https://www.postgresql.org/) used as an open source relational cloud database during development.
- [Amazon AWS](https://aws.amazon.com/) used to store static files after deployment.
- [Heroku](https://www.heroku.com/) a cloud platform for deploying the website.
- [W3C Markup Validation Service](https://validator.w3.org/) to check for markup validity.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the CSS-code.
- [JSHint](https://jshint.com/) to check the Javascript code.
- [PEP8 checker](http://pep8online.com/) to check the python code for PEP8 requirements. 
- [Favicon]( http://antifavicon.com/) to make the favicon for the website.
- [Coolors](https://coolors.co/) to make the colour scheme.
---
# **Testing**
For testing results, see [Testing.md](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/TEST.md)

---
## **Deployment**
Heroku is used to deploy this application, since GitHub can only deploy static websites.

This application was developed using VSCode as IDE, commited to Git and pushed to GitHub.
The GitHub repository is linked to the Heroku App via automatic deployment (see below).
Every time commits and pushes are sent to GitHub, the Heroku App is updated shortly after.
Committing to GitHub is done as follow:  
```
    git add .
    git commit -m "commit message"
    git push
```

### Deployment to Heroku  

1. **Create a Heroku App**
    1. Create a new app by clicking the ‘New’ button.
    ![new Heroku app button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/new-app.png)
    2. Give a unique name and set region to your nearest region.
    ![name and region input](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/name-region.png)
    3. Click ‘Create App’.
    4. Click on the 'Resources' tab, in Add-ons type: postgress and choose 'Heroku Postgres'.
    ![postgres add-on](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/postgress.png)  
    5. For plan name choose the free plan and click submit form.

2. **Setup the Postgres Database**
    1. In your IDE install dj_database_url and psycopg2.   
        ```
        pip3 install dj_database_url
        pip3 install psycopg2-binary
        ```
    2. Create a requirements file.  
        ```
        pip3 freeze > requirements.txt
        ```
    3. Import dj_database_url in `settings.py`.
    4. Backup the database if you're using a local database instead of fixtures.  
        ```
        python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
        ```  
        p.s. make sure you're connected to your mysql database.  
    5. Scroll down to DATABASES, comment out the default configuration and add the database url from Heroku   
        ```
        DATABASES = {
                'default': dj_database_url.parse('DATABASE_URL')
        }
        ```
        You can the database url from Heroku's Config Vars in the Settings tab. 
        > Note: The DATABASE_URL from Heroku is an environment variable and shouldn't be committed in version control.
    6. Run migrations.  
          ```
          python3 manage.py migrate
          ```
    7. In case of using a local database type:  
        ```
        python3 manage.py loaddata db.json
        ```  
        to import the data from the mySQL database to Postgre.
    8. In case of using fixtures:  
        First import the categories:  
        ```
        python3 manage.py loaddata categories
        ```  
        And then the products:  
        ```
        python3 manage.py loaddata products
        ```  
    
3. **Create a superuser**  
    - Type: `python3 manage.py createsuperuser`  
    - Add a username and password.

4. **Make a distinction between local and remote database**  
    Create an if-statement in `settings.py` so that when the app is running on Heroku it connects to Postgres(remote) and otherwise, it connects to sequel light(local).  
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
5. **Install gunicorn**  
    Gunicorn will replace the development server once the app is deployed to Heroku and will act as the web server.  
    type: `pip3 install gunicorn`

6. **Create a Heroku 'Procfile'**  
    The Procfile is what Heroku looks for to know which file runs the app and how to run it.
    1. In the terminal type: **touch Procfile** or create a new file named 'Procfile' in the root.
    2. Inside the Procfile type:   
    ```
    web: gunicorn <Github appname>.wsgi:application
    ```

7. **Connect to Heroku in the terminal**
    1. Login to your account on the Heroku website.
    2. Go to account settings (click on your avatar).
    3. Scroll down to the API Key section.
    4. Click 'Reveal' and copy your API Key.
    5. Login to Heroku via CLI  
     ```
     heroku login -i
     ```
    6. Login with your email but use the API Key as the password.
    7. Temporarily disable the collection of static files until AWS has been setup.  
        ```
        heroku config:set DISABLE_COLLECTSTATIC=1 --app <Heroku appname>
        ```  
    8. Add the hostnames to allowed hosts in `settings.py`.  
        ```
        ALLOWED_HOSTS = ['<heroku appname>.herokuapp.com', 'localhost', '127.0.0.1']
        ```
       where 127.0.0.1 is the IP of the localhost, so that the app can also run locally.
    9. Commit to GitHub.
    10. Commit to Heroku. Make sure you have git remote initialized.  
        ```
        heroku git:remote -a <Heroku appname>
        ```  
        Push to Heroku.  
        ```
        git push heroku
        ```

8. **Setup automatic deployment from GitHub/Connect Heroku app to GitHub.**  
    1. Go to the Deploy tab.  
    ![deploy tab](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/deploy.png)  
    2. Under 'Deployment method', Click on 'Connect to GitHub'.
    ![connect to github button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/connect-to-github.png)
    3. Under 'Connect to GitHub', enter the GitHub repository name and click ‘Search’ and click 'Connect'.
    ![connect repository name](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/search-repo.png)
    4. Scroll down to Automatic deploys and click the ‘Enable Automatic Deploys’ button.  
    ![enable automatic deploy button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/automatic-deploy.png)

9. **Set up Amazon AWS**
    1. Login to AWS or create an account.
    2. Search for S3 and click it.
    3. Create a new bucket  
    ![create new bucket](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/bucket.png) 
    4. Give the bucket a unique name.
    5. Select the region closest to you.
    ![S3 name and region](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/s3-name-region.png)
    6. Uncheck block all public access and acknowledge that the bucket will be public.  
    ![S3 allow public access](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/s3-access.png)
    7. Click 'Create bucket'.  
    ![Create bucket](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/create-bucket.png)
    8. Set basic settings
        - Click on the bucketname.
        - Click the 'Properties' tab.
        - Scroll down to 'Static website hosting' and click 'Edit'
        ![Static website hosting](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/static-website-hosting.png)  
        - Click 'Enable' and enter the default values for index and error document.
        ![Enable hosting settings](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/enable-hosting.png)  
        - Click 'Save changes'.
    9. Set permissions
        - Click on the 'Permissions' tab.
        - Scroll down to 'CORS' and click 'Edit'.
        - Past the following configuration:
        ```
            [
                {
                    "AllowedHeaders": [
                        "Authorization"
                    ],
                    "AllowedMethods": [
                        "GET"
                    ],
                    "AllowedOrigins": [
                        "*"
                    ],
                    "ExposedHeaders": [

                    ]
                }
            ]
        ```
        - Click 'Save changes'
    10. Set Bucket Policy
        - In the Permissions tab scroll to Bucket Policy and click 'Edit'.
        - Click on 'Policy generator'  
        ![policy generator button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/bucket-policy.png)
        - In the new window that opens select 'S3 bucket policy' as the 'Type of Policy'.
        - Add * to 'Principal'.
        - Select 'GetObject' in 'Actions'.
        - Copy your ARN from the other tab and paste it in the ARN field.
        - Click 'Add Statement'.
        ![policy generator](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/policy-generator.png)
        - Click 'Generate policy'.
        - Copy the policy and paste it in the Bucket Policy of the first tab.
        - Add '/*' to the end of the resource key.
        - Click 'Save changes'.
        - Scroll down to Access control list (ACL) and click 'Edit'.
        - Select 'List' for Everyone (public access) and select 'I understand...' at the bottom.
        ![Acces control list](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/acl.png)
        - Click 'Save changes'.
    11. Create AWS groups, policies and users
        - Click Iam (via search bar or Services).
        - Create a group
            - Click on 'Users groups' on the left.  
            !['User groups'](/https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/iam-group.png)
            - Click 'Create group' and enter a group name.
            - Scroll down and click 'Create group'.
        - Create the policy used to access the bucket
            - Click on 'Policies' on the left.
            - Click 'Create policy'.
            - Click the JSON tab and then on 'Import managed policy'.
            - Search for 'S3' in the pop up window and select 'AmazonS3FullAccess' and click 'Import'.  
            !['AmazonS3FullAccess'](/https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/iam-policies.png)
            - Copy your ARN (Open S3 in a new tab, click the bucket name, click Permission tab, click Bucket policy and copy the ARN)
            - Paste it in the 'Resource' in the JSON tab.  
            !["Resource"](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/iam-policy.png)
            - Click 'Next: Tags', then 'Next: Review'.
            - Give the policy a name and description.
            - Click 'Create policy'.
        - Attach the policy to the group
            - Click 'User groups' on the left.
            - Click the group name.
            - Click the 'Permissions' tab.
            - Click 'Add permission', then click 'Attach Policies'.  
            !['Attach Policies'](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/iam-group-policy.png)
            - Search for the policy that you created above, select it.
            - Click 'Attach policy'.
        - Create a user to put in the group
            - Click 'Users' on the left.
            - Click 'Add user' and create a username.
            - Select 'Access Key - Programmatic access' and click 'Next: Permissions'.
            - Select the group you want to add the user to.
            - Click 'Next: Tags', then 'Next: Review' and 'Create User'.
            - Download the .csv file and save it well, since it contains this users access key and secret access key and can't be downloaded again.
    12. Connect Django to S3
        - Install boto3 and django-storages.  
        ```
        pip3 install boto3  
        pip3 install django-storages
        ```  
        - Add these to requirements.
        ```
        pip3 freeze > requirements.txt
        ```  
        - Add storages to INSTALLED APPS in `settings.py`.
        - Add the following settings to `settings.py`.  
        ```
        if 'USE_AWS' in os.environ:
            # Cache control
            AWS_S3_OBJECT_PARAMETERS = {
                'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                'CacheControl': 'max-age=94608000',
            }
            
            # Bucket Config
            AWS_STORAGE_BUCKET_NAME = '<bucket name>'
            AWS_S3_REGION_NAME = '<bucket region>'
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
        ```  
        > 'Cache control' will tell the browser that it's okay to cache static files for a long time.  
        > 'Bucket Config' will tell Django which bucket it should be communicating with.  
        > 'Static and media files' will tell where to find static and media files.  
        > 'Override static and media URLs in production' will tell which url's to use in production.    

        - Go to Heroku and add these values to the Config Vars (under Settings):
        ![Heroku Config Vars](/https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/config-vars.png)  
        - Create a custom class to tell django that in production we want to use s3 to store our static files.  
        - Add the folowing code to custom_storages.py  
        ```
            from django.conf import settings
            from storages.backends.s3boto3 import S3Boto3Storage


            class StaticStorage(S3Boto3Storage):
                location = settings.STATICFILES_LOCATION


            class MediaStorage(S3Boto3Storage):
                location = settings.MEDIAFILES_LOCATION
        ```  
        - Push to GitHub.
    13. Add media files to S3
        - In your Amazon S3 bucket click 'Create folder' and name it 'media'.
        - Open the folder and click 'Upload'.
        - Click 'Add files' and select all your product images.
        - Under 'Permissions' select 'Grant public-read access'.
        - Select 'I understand...' and click 'Upload'.
10. **Setup Stripe**
    1. Add Stripe keys to Config Var
        - Login to Stripe or create and [account](https://dashboard.stripe.com/register).
        - Click developers and then API Keys.
        - Copy the public and secret key and add them to Config Vars in Heroku.  
        ```
        STRIPE_PUBLIC_KEY = <your Stripe public key>
        STRIPE_SECRET_KEY = <your Stripe secret key>
        ```  
    2. Create a webhook endpoint
        - In Stripe - Developers click 'webhooks'.
        - Click 'Add endpoint'.
        - Enter your heroku url and add /checkout/wh/ to it.
        ```
        https://<projectname>.herokuapp.com/checkout/wh/
        ```  
        - Select 'receive all events' and click 'Add endpoint.
        - Scroll down to 'Signing secret' and click 'Reveal signing secret'.
        - Copy the signing secret and add to the Config Vars in Heroku.

---
### Forking this GitHub Repository
A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.
To achieve this follow these steps:
1. Login to GitHub and follow this link to [the GitHub Repository](https://github.com/chizzletaz/SpaceTravelAgency).
2. At the top right of the page, click on the fork button.  
![fork button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/forking.png)
3. You now have a copy of the repository in your GitHub account.

### Cloning this GitHub repository
1. Log in to GitHub and follow this link to [the GitHub Repository](https://github.com/chizzletaz/SpaceTravelAgency)
2. Click on the ‘Code’ button 
![Code button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/github-clone.png)
3. To clone using HTTPS, copy the link that is displayed by clicking on the copy icon 
![save icon](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/github-copy.png).
4. Open a terminal in your preferred IDE (e.g. VSCode or Atom)
5. Use  the ‘git clone’ command and add the link that you copied in step 3.
6. Or for VSCode: click 'Explorer' or 'Shift + CMD + E'. 
7. Click the button 'Clone Repository', add the url you copied above and hit enter.
8. A clone will be created locally.

> For more info on how to clone a repository check [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### Setup local deployment
1. **Clone or fork this repository (see above)**.
2. **Install the requirements by typing:**  
        ```
        pip3 install -r requirements.txt
        ```  
   in the terminal.
3. **Set the environment variables.**
    1. If you're using GitPod.
        - In your workspace click 'Settings'.
        - In Environment Variables insert the following variables:
        ```
        'DEVELOPMENT', 'True'
        'SECRET_KEY', '<your secret key>'  e.g. from a key generator
        'STRIPE_PUBLIC_KEY', '<your stripe public key>'
        'STRIPE_SECRET_KEY', '<your stripe secret key>'
        'STRIPE_WH_SECRET', '<your stripe webhook secret>'
        ```
    2. If you're using a local IDE, like VSCode.
        - Create a .gitignore file in the root directory, if there isn't one.
        - Open the .gitignore file and add 'env.py' to it, if it isn't in there. 
        - Create an env.py file and set the environment variables by adding the following text: 
        ```
            import os

            os.environ["STRIPE_PUBLIC_KEY"] = '<your stripe public key>'
            os.environ["STRIPE_SECRET_KEY"] = '<your stripe secret key>'
            os.environ["STRIPE_WH_SECRET"] = '<your stripe webhook secret>'

            os.environ["SECRET_KEY"] = '<your secret key>'  e.g. from a key generator

            os.environ["DEVELOPMENT"] = 'True'
        ```  
    > See [above](#setup-stripe) how to get your stripe keys.  
    > Tip: use this [key generator](https://miniwebtool.com/django-secret-key-generator/)   
4. **Migrate the database models**
    - Check migrations
    ```
    python3 manage.py makemigrations --dry-run
    ```
    - Make migrations
    ```
    python3 manage.py makemigrations
    ```
    - Check migrate
    ```
    python3 manage.py migrate --plan
    ```
    - Migrate
    ```
    python3 manage.py migrate
    ```

5. **Load product data.**
    - Type `python3 manage.py loaddata db.json`
6. **Create a superuser account**
    - `python3 manage.py createsuperuser
    - Add a username and password. 
7.**Run the app.**
   - In the terminal, type: `python3 <your python file name>.py`  
        
---
# **Credits**
### code
- Text slide in from left and right - [Menucool](http://www.menucool.com/ui/slide-in-when-scrolling)

- Show and hide search bar - [W3schools](https://www.w3schools.com/jquery/eff_toggle.asp)

- Disable dates in bootstrap date picker - [Manoj](https://stackoverflow.com/questions/44236542/disable-friday-and-saturday-in-datepicker)
 
- Format numbers in Django to Display prices with commas. [Ned Batchelder](https://stackoverflow.com/questions/346467/format-numbers-in-django-templates)

- Change the scrollbar css - [CSS-tricks](https://css-tricks.com/almanac/properties/s/scrollbar/)

- Using 'cleaned_data' on contact form - [Django Docs](https://docs.djangoproject.com/en/3.2/ref/forms/validation/)
### Content
Recipes:
- [Twix pie](https://veganwifey.com/een-vegan-twix-taart/)  
 
- Adjusting the heigth of the textarea to fit the content - [Martin Prestone](https://stackoverflow.com/questions/2803880/is-there-a-way-to-get-a-textarea-to-stretch-to-fit-its-content-without-using-php)

The other recipes are my own or come from my own collection of recipes written on a piece of paper.  

### Media
earthview1.jpg 
	https://earth.google.com/

earthview2.jpg
	https://besthqwallpapers.com/download/148672/1440x900
space-hotel-room.jpg
	https://www.architecturaldigest.com/story/worlds-first-space-hotel-open-2027
space-hotel.jpg
	Architectual digest (https://www.architecturaldigest.com/story/worlds-first-space-hotel-open-2027)
moon.jpg
	https://en.wikipedia.org/wiki/Moon
moon2.jpg
	https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Helping_Heracles_EL3_to_survive_the_long_cold_dark_nights_on_the_Moon
moon3.jpg
	https://www.cloudynights.com/topic/640527-34-moon-with-an-old-friend/
mars.webp
	https://www.ad.nl/wetenschap/vanavond-ideaal-weer-om-mars-te-spotten~a230ac057/?referrer=https%3A%2F%2Fwww.google.com%2F
mars2.jpg
	scienties(https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.scientias.nl%2Fmars-lijkt-in-ieder-geval-ondergronds-over-een-belangrijk-ingredient-voor-leven-te-beschikken%2F&psig=AOvVaw2whrgOVXpChlJ9U2zj8qug&ust=1630530459121000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOjbobmV3PICFQAAAAAdAAAAABAQ)
spacewalk.jpg
	https://gospacewalk.com/blog/introducing-spacewalk-to-the-workplace
spacewalk2.jpg
	https://www.dawn.com/news/1472001

space-background.jpg
	https://blogs.esa.int/space19plus/files/2019/03/nebula.jpg

space-background2.jpg
	https://wallpaperaccess.com/dark-space-desktop
no-image.png
	https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1200px-No-Image-Placeholder.svg.png
sleep-mask.jpg
	https://m.media-amazon.com/images/I/A1OyV3YHI4L._SY450_.jpg
clipon-lens.jpg
	https://m.media-amazon.com/images/I/71y8Kvz749L._AC_SL1500_.jpg  

- Error 500 image - <a href="https://www.freepik.com/free-photos-vectors/website">Website vector created by stories - www.freepik.com</a>  
- Error 403 image - <a href='https://www.freepik.com/free-photos-vectors/website'>Website vector created by stories - www.freepik.com</a>  
- Error 404 image - <a href='https://www.freepik.com/free-photos-vectors/technology'>Technology vector created by freepik - www.freepik.com</a>

---
# Acknowledgements
I want to give special thanks my mentor Antonio Rodriguez for  and guiding me through this project and helping me solve some of the challenges I faced.  
I want to thank Tutor support at CI and fellow Slack members for answering my questions.