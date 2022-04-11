# BRIXICON

![mobileMenuScreenshot](https://user-images.githubusercontent.com/11600460/162638021-4be29374-eecb-45ea-9931-163a22d95d59.png)

http://brixicon.herokuapp.com/get_brixicals
The Brixicon is a LEGO jargon website giving definitions for all the popular terms used in the LEGO community.


## Author
Jeremy Walker


## Project Overview
![image](https://user-images.githubusercontent.com/11600460/162638275-1d42f481-6f04-431a-bf22-7e62c5708394.png)

Brixicon allows you to quickly and easily find that obscure LEGO term that everyone is blogging about in their latest online posts!  Bright and cheery it represents all that is LEGO giving you clear descriptions of everything from AFOL(Adult Fan of LEGO) to UCS(Ultimate Collector Series) with images included to clarify.  Brixicon has full user authentication and allows registered users to add entries to the Brixicon if there is something missing.  Every entry includes a up and down vote feature to gauge user interest in each entry.  The Brixicon is the premier online responsive destination whether you're sitting at home on your laptop, on the go on your mobile device, or visiting us from your desktop.

http://brixicon.herokuapp.com/get_brixicals

## HOW TO USE
Here are two premade profiles for testing purposes.

### Standard User(allows you to add entries and edit a profile)
username = usertest
password = usertest

### Admin User(allows Standard user functionality as well as being able to edit and delete entries)
username = admin
password = password

# Table of Contents
- [BRIXICON](#brixicon)
  * [Author](#author)
  * [Project Overview](#project-overview)
  * [HOW TO USE](#how-to-use)
    + [Standard User(allows you to add entries and edit a profile)](#standard-user-allows-you-to-add-entries-and-edit-a-profile-)
    + [Admin User(allows Standard user functionality as well as being able to edit and delete entries)](#admin-user-allows-standard-user-functionality-as-well-as-being-able-to-edit-and-delete-entries-)
- [Table of Contents](#table-of-contents)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope)
    + [Project Goals](#project-goals)
      - [User Goals](#user-goals)
      - [Developer Goals](#developer-goals)
      - [Website Owner Goals](#website-owner-goals)
    + [User Stories](#user-stories)
    + [Design Choices](#design-choices)
      - [Colors](#colors)
      - [Typography](#typography)
      - [Images](#images)
      - [Design Elements](#design-elements)
      - [Animations and Transitions](#animations-and-transitions)
    + [Wireframes](#wireframes)
    + [Features](#features)
      - [Future Features](#future-features)
- [Information Architecture](#information-architecture)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Database Choice](#database-choice)
    + [Data Models](#data-models)
- [Technologies Used](#technologies-used)
  * [Programming Languages](#programming-languages)
  * [Framework & Extensions](#framework---extensions)
  * [Fonts](#fonts)
  * [Tools](#tools)
- [Defensive Programming](#defensive-programming)
  * [Testing](#testing)
    + [Validation Testing](#validation-testing)
    + [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
    + [Manual Testing](#manual-testing)
    + [Defect Tracking](#defect-tracking)
    + [Outstanding Defects](#outstanding-defects)
  * [Deployment](#deployment)
    + [Deploy Locally](#deploy-locally)
    + [Deploy To Heroku](#deploy-to-heroku)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## UX

### Strategy
The original intent for this site was to be a much more robust LEGO themed destination.  A discussion forum, a LEGO set database, and a personal collection database were planned.  Those extra functionalities proved to be too time intensive for the scope of this project.

### Scope
In the future the other options discussed in the strategy section will be implemented one at a time along with a search function to allow users to find the best deals on the sets/parts that they are looking for from many sources on the internet.  For now this will help generate users and interest and eventually drive ad revenue to be able to further expand the offerings.

### Project Goals
As you can see the site is decked out in LEGO style colors.  Very akin to the inside of a LEGO brand physical store.  The idea behind the bright primary colors is to promote happiness and joy, and that is the scope of this site.  

#### User Goals

> - New users from the moment they enter the site will see a simple easy to use and understand site that delivers fast queries to any search term that they provide. 
> - Registered and logged in users are given the extra capability to be able to add their own entries to the database to contribute with the information sharing.
> - Admin level users are able to monitor user submissions and edit and delete them if necessary. 

#### Developer Goals

As the developer of this site I wanted to be able to provide an open forum for LEGO enthusiasts to share knowledge of LEGO terms and additionally showcase my talent and abilities to future clients/employers. 

#### Website Owner Goals

As owner of this site you could easily start to monetize the traffic that you would get.  Affiliate links to amazon products, links to online LEGO selling forums, and advertising for other sites and products would all be revenue streams.

[Back To Table of Contents](#table-of-contents)


### User Stories

As a new user I would be able to quickly look up that quirky obscure word that everyone on the blogs is using and be able to use it too with confidence.

As an existing user I will be able to research new terms and add things to the database to be able to enrich other users with my knowledge.

As the admin i will be able to monitor activity on the site by editing and deleting entries as is needed.


[Back To Table of Contents](#table-of-contents)


### Design Choices

#### Colors

The color palette for this site was inspired solely by the logo for LEGO and the color scheme used in official LEGO stores.  It's fun and cheery and promotes happiness and joy!
![Brixicon Color Palette](https://user-images.githubusercontent.com/11600460/162647018-630c3b10-a926-4e18-8f18-779496b9335a.png)

#### Typography

No special font types were used for this site.  Custom stylings were applied to Headers for pages and edit and creation boxes.  colors were kept to the primary color scheme.  

#### Images

Explain why you used certain icons and images on your site

#### Design Elements

Site design elements to be used in this creating are as follows:
> - desktop navigation
> - mobile navigation
> - containers/cards
> - buttons
> - text input
> - textarea inputs
> - images
> - icons

#### Animations and Transitions

On the main page when you hover over one of the up or down vote items it will change color, enlarge, and turn slightly.  

### Wireframes

![brixicon_wireframe](https://user-images.githubusercontent.com/11600460/162647691-c7489fd8-c5c1-480b-9974-801e8ff5b1f6.png)

[Back To Table of Contents](#table-of-contents)

### Features

The main page features a search function to bring up specific "Brixicals" or entries in the database.
![image](https://user-images.githubusercontent.com/11600460/162649528-2c394cac-1d64-40d2-b275-0988869018cf.png)

Users can register with the site to be able to add their own Brixicals.  The user that added the brixical gets credit for it at the bottom of the entry.
![image](https://user-images.githubusercontent.com/11600460/162649605-2041b51e-a369-4471-a6c6-319d99997929.png)

Users can up/down vote their favorite entries.
![image](https://user-images.githubusercontent.com/11600460/162649674-53a9b3db-4c9f-4190-9958-466d124038d9.png)

Admin can edit/delete brixicals.  
![image](https://user-images.githubusercontent.com/11600460/162649720-ec68b132-0acc-4ba5-9f78-9b688f0b34ec.png)

#### Future Features

In the future additional developements would include;
> - A set / brick database of all released sets/parts.
> - A personal database to track your own collection of LEGO.
> - A forum to discuss all things LEGO.
> - Auction/sales for users to trade / sell LEGO.


# Information Architecture

## Entity Relationship Diagram

![Untitled Diagram drawio](https://user-images.githubusercontent.com/11600460/162652603-79d641be-f9b6-4cce-9e68-b81e630ce129.png)


## Database Choice
MongoDB was used as the database for this site.

### Data Models
CREATE, READ, UPDATE, AND DELETE functionality are achieved with both data models.  

With the user's table a new user is able to CREATE a new profile(register.html), READ the profile (view_profile.html), and UPDATE a profile (update_profile.html).

With the brixical table a registered user can CREATE a new entry(add_brixical.html), and READ entries(brixicals.html).  The Admin level user can UPDATE brixicals(edit_brixical.html), and DELETE an entry(delete functionality within python program).


# Technologies Used

> - Wireframes were created with Balsamiq(https://balsamiq.com/) A free and easy to use wireframe creation program. 
> - Custom favicon was created here https://favicon.io/favicon-converter/ Using a picture of a single stud brick I created a custom Favicon to use cross platform.
> - Color palette was created here https://coolors.co/ 
> - CSS customization was achieved using https://materializecss.com/ I took the materialize css file and made modifications to some of the classes and media queries to better suit my site.
> - Database technology was done through https://www.mongodb.com/ I aslo paired that up with Flask and it's jinja templating to perform data requests and pushes.
> - All Python hosting was accomplished with https://heroku.com/ Gitpod pages doesn't allow python driven pages.
> - Site was designed and tested here https://gitpod.com/ 
> - Repository for files was here https://github.com/
> - Additional database management was achieved through https://flask.palletsprojects.com/en/2.1.x/

## Programming Languages

- [CSS3](https://www.w3schools.com/w3css/default.asp) - used to style DOM appearance. 
- [HTML5](https://www.w3schools.com/html/default.asp) -  used to define DOM elements. 
- [JQuery](https://jquery.com) - used to initialize handlers for user interactive elements such as Bootstrap framework pieces like: check boxes, date pickers, menu toggles.
- [JavaScript](https://www.javascript.com/)  -  used to help handle challenge member entry.
- [Python](https://www.python.org/) the project back-end functions are written using Python. Django and Python is used to build route functions.
- [Flask](https://flask-doc.readthedocs.io/en/latest/) - python based templating language
- [mongodb](https://www.mongodb.com/cloud/atlas)- a fully-managed cloud database used to store manage and query data sets
- [Markdown](https://www.markdownguide.org/) Documentation within the readme was generated using markdown

[Back To Table of Contents](#table-of-contents)

## Framework & Extensions

Requirements for the site are as follows:
Python(site programming and interface with data), Flask(python to mongoDB connections and site programming), MongoDB(data modeling), and Werkzeug(site security).


## Fonts

- Button and text input Icons: [Font Awesome 5](https://fontawesome.com/icons?d=gallery)

## Tools
Balsamiq
favicon.io
coolor.co
diagrams.net
Gitpod
Heroku
Chrome Developer Tools

[Back To Table of Contents](#table-of-contents)

# Defensive Programming

I used  Werkzeug for site security.  Password hashing was the main method to enrypt sensative data.
   
[Back To Table of Contents](#table-of-contents)

## Testing

I tested this site personally on laptop/desktop and android devices.  I had others test it via Apple devices(Iphone 12 / SE / and IPAD).  I also used Chrome Developer tools to emulate a number of mobile devices and tablets.

### Validation Testing

- [CSS Validator](https://jigsaw.w3.org/css-validator/) Css errors with 3rd parties are being ignored(materialize and font-awesome).![image](https://user-images.githubusercontent.com/11600460/162661767-8b4211f8-28a8-4578-b664-7fa1a448637f.png)

- [HTML Validator](https://validator.w3.org/)![image](https://user-images.githubusercontent.com/11600460/162660683-3418cbe2-6086-4141-aa79-68f19d27f427.png)

- [PEP8 Validator](http://pep8online.com/) ![image](https://user-images.githubusercontent.com/11600460/162660419-bec0b3e2-4408-4a09-8fb4-492defd0ceae.png)


### Cross Browser and Cross Device Testing


| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| real phone: iPhoneSE          | safari      | iOs        | XS 375 x 667  |
| dev tools emulator: GalaxyS20 | Chrome      | android    | SM 412 x 915  |
| browserstack: iPhone 10x      | Chrome      | iOs        | SM 375 x 812  |
| dev tools emulator: ipad mini | safari      | iOs        | M 768 x 1024  |
| dev tools emulator: ipad air  | safari      | iOs        | LG 820 x 1180 |
| browserstack                  | Chrome      | windows    | XL 1920 x 946 |


### Manual Testing

>  **Register Page**
>  Go to the Register page: http://brixicon.herokuapp.com/register
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Be logged in and go to register page url http://<YOUR APPP>.herokuapp.com/register, should have error saying you are already registered and be on profile page
   
>  **Edit Profile Page**
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Try to submit the form with inputs invalid and verify that an error message appears

>  **Add Brixical Page**
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Try to submit the form with inputs invalid and verify that an error message appears
>    - [x] Try to submit the form with duplicate entry and verify that an error message appears

   >  **Edit Brixical Page**
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Try to submit the form with inputs invalid and verify that an error message appears
>    - [x] Try to submit the form with duplicate entry and verify that an error message appears


### Defect Tracking

### Outstanding Defects
See github issue tracking for details of bugs and solutions.
   
## Deployment

### Deploy Locally

I could not deploy locally.  I had to use Heroku for all my deployment and testing after uploading to github.

### Deploy To Heroku

1.  Create connection to Github repository.
2.  In Heroku settings create key list and populate with data from python file to connect to mongoDB.
      IP
      MONGO_DBNAME
      MONGO_URI
      PORT
      SECRET_KEY
3.  In Deploy tab make sure "automatic deploys" is enabled.
4.  Push all changes to github and ensure you sync changes.

## Credits

### Content

Data for Brixicon came from https://blog.firestartoys.com/a-lego-glossary/.
   
### Media

Imagery for Brixicon came from https://blog.firestartoys.com/a-lego-glossary/.
Where images were not availble from there images were found using Google Image search.
Were this site to go to any commercial state I would take my own pictures to use to avoid any image use issues.

### Acknowledgments

I loosely followed some of the Code Institute course work to start the basic app routes and data acquisitions.  I then branched out and had to adapt most of it to my specialized situations.
   
I used text and images from https://blog.firestartoys.com/a-lego-glossary/ for content and media as this was an exercise to showcase skills in coding and design not data entry and photography.
   
I'd like to acknowledge my mentor Malia Havlicek for her advice and extensive review of my site.  It was crucial to getting this project done in time for submittal.  
