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
Copy your readme to http://ecotrust-canada.github.io/markdown-toc/ to make a table of contents.  This will help assessors to see the structure of your readme. Just test it out ast this tool isn't perfect. It tends to mess up with special characters like dashes.

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

#### Custom Javascript
- call attention to any custom javascript you created to help your User Experience you can organize this by functions or files

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

Provide a link to any google or other fonts used on your site using markdown links:

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

- [CSS Validator](https://jigsaw.w3.org/css-validator/) Css errors with 3rd parties are being ignored(materialize and font-awesome).
- [HTML Validator](https://validator.w3.org/)
- [PEP8 Validator](http://pep8online.com/) ![image](https://user-images.githubusercontent.com/11600460/162660419-bec0b3e2-4408-4a09-8fb4-492defd0ceae.png)



### Cross Browser and Cross Device Testing
Create a table that lists out what devices, browsers, and operating system you tested your application on and a brief description of why you chose the mixture you did. The point is to prove that you looked at the site across various browsers, operating systems, and viewport breakpoints.

| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| real phone: motog6            | chrome      | android    | XS 360 x 640  |
| browser stack: iPhone5s       | safari      | iOs        | XS 320 x 568  |
| dev tools emulator: pixel 2   | firefox     | android    | SM 411 x 731  |
| browserstack: iPhone 10x      | Chrome      | iOs        | SM 375 x 812  |
| browserstack: nexus 7 - vert  | Chrome      | android    | M 600 x 960   |
| real tablet: ipad mini - vert | safari      | iOs        | M 768 x 1024  |
| browserstack: nexus 7 - horiz | firefox     | android    | LG 960 x 600  |
| chrome emulator: ipad - horiz | safari      | iOs        | LG 1024 x 768 |
| browserstack                  | Chrome      | windows    | XL 1920 x 946 |
| real computer: mac book pro   | safari 12.1 | Mohave     | XL 1400 x 766 |
| browserstack                  | IE Edge 88  | windows 10 | XL 1920 x 964 |

### Manual Testing

You can track your test in various ways.  

But for any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. 

1. Markdown
>  A particularly useful form for describing your testing process is via scenarios, such as:
> 
>  **Register Page**
>  Go to the Register page: http://<YOUR APPP>.herokuapp.com/register
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Be logged in and go to register page url http://<YOUR APPP>.herokuapp.com/register, should have error saying you are already registered and be on profile page

2. Spreadsheet    
> Here is a [Manual Testing Template](https://docs.google.com/spreadsheets/d/189VpSeEG9oevSRhvb2WZl8zCk9L3s2iWQyrJ_1jjAGQ/edit?usp=sharing) that you can use as a starting point to keep track of your testing efforts. Make a copy of it in your own account and update as needed to reflect the browsers you are testing and features.  

3. GitHub Issues, Milestones & Boards
> You can also use agile tools in github to help track your testing and defects. Here's a document that I put together about that [process](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing)

It's ok to spot check specific functionality across devices and browsers but each page should be viewed as a whole for each device/browser combo at least once.

A quick way to check if items are exceeding the screen width of a project is to run this javascript in the console for various screen emulations:

```
var docWidth = document.documentElement.offsetWidth;
[].forEach.call(document.querySelectorAll('*'),function(el){if(el.offsetWidth > docWidth){console.log(el);}});
```

### Defect Tracking

You should mention  any  bugs or problems you discovered during your testing, even if you haven't addressed them yet.

Here is a [Defect Tracking Template](https://docs.google.com/spreadsheets/d/1tYB4X4wTCNEW_Y1no3hsGbclh2bLokl_I5Ev3s5EuJA/edit?usp=sharing) you use as a starting point to track defects. Make a copy of the sheet to your own account and update the Features sheet to match your project. 

Again, you could use [github issues](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing) to track you defects. Or write them up with markdown.
 
### Defects of Note
Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and how you finally ended up resolving them.


### Outstanding Defects
It's ok to not resolve all the defects you found. If you know of something that isn't quite right, list it out and explain why you chose not to resolve it.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages).

In particular, you should provide all details of the differences between the deployed version, and the development version, if any.

Remember to use proper markdown for commands and enumerated steps.

### Deploy Locally

Write out the steps you take starting from cloning the repository in github or clicking a gitpod button to run your code locally. Test it out and make sure it works. This can be running from your IDE of choice like VSCode or PyCharm or GitPod.

You may want to re-watch the videos when writing up this section.

### Deploy To Heroku

Write out steps you would take and test them to deploy your code to Heroku. Include a table of configuration variables as needed in your settings.py file without exposing your own values. Include links to users on how to set up such accounts for AWS, STRIPE or other programs.  

You may want to re-watch the videos when writing up this section.

## Credits

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did. 

### Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

### Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Example project as a starting point. Make note of that here.
