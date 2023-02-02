# Endurance Republic

## By Mark Todman

![Launch page screenshot.](/static/img/readme/endrep-amiresponsive.png)

The deployed [Endurance Republic](https://endurance-republic.herokuapp.com/) app.

The [GitHub repository.](https://github.com/marktodman/endurance-republic)

---
## OVERVIEW
1. [Endurance Republic Concept](#endurance-republic-concept)
1. [Strategy](#strategy)
1. [Scope](#scope)
1. [Structure](#structure)
1. [Skeleton](#skeleton)
1. [Surface](#surface)
1. [Planning](#planning)
1. [Features](#features)
1. [Marketing & SEO](#marketing-and-seo)
1. [Resources](#resources)
1. [Testing](#testing)
1. [Deployment](#deployment)
1. [Future Development Ideas](#future-development-ideas)
1. [Credits](#credits)

---
## ENDURANCE REPUBLIC CONCEPT

The concept for Endurance Republic is an adventure event company E-commerce web app. [Endurance Republic](https://endurance-republic.herokuapp.com/) is deisgned to present a showcase of events to interested potential participants. The foucs of the web app is to engage potential participants interested in adventure sports and provide them with information in order to book on to the varied events. There are range of different adventure events, including different activities and different locations around the World. They are all exciting challenges in stunning locations.

---
## STRATEGY

To create a web application that engages users in booking onto adventure race events.

### Target Audience:

- Adventure racing enthusiasts
- People who like organised outdoor challenges
- People who are looking for a new challenge
- Outdoor enthusiasts looking for motivation and/or inspiration

### E-commerce Business Model:

Endurance Republic is a business to consumer (B2C) business model. We are selling places on organised adventure events in beautiful locations. Customers pay for their place via the website and can expect to have secured their place on an organised event as per the description presented for each event. Endurance Republic is responsible for organising and running the event to fulfill the contract with the customer.

The site is marketed through a Facebook business page and email marketing, through newsletter sign up. Other social channels will also be built into the marketing strategy. SEO is implemented through keyword metadata to allow users to discover the site through organic search.

---
## SCOPE

1. Visually appealing and intuitive user experience
2. Scalable design that allows for the application to grow as more events are added
3. Extensive frontend functionality for Users to support an engaging user experience and maintain account information
4. Extensive frontend functionality for Admins to support rapid testing and deployment
5. Responsive site design that delivers excellent user experience across platforms
6. E-commerce functionality to allow users to make online purchases

---
## STRUCTURE

### Functional Structure

1. HOME PAGE: the home page contains a clear mission statement and instructions to get started with on the application. At this point the user can link straight to the content or registration. Returning users can login from the home page. Register and Login are also available from the Navbar.
2. EVENTS PAGE: a responsive list of cards that details the events available. Each Event card has information about the description, distance, difficulty rating, location, start date, and price. The Events page can be accessed directly through the Navbar. This page is responsive and scalable and will grow as more Events are added.
3. BAG PAGE: once a customer is logged in, they will be able to book an event. Clicking on Book My Place! will place the event in the users bag, which is accessible through the cart icon in the Navbar. The bag page allows the customer to remove the item from the bag or proceed to the Checkout.
5. CHECKOUT PAGE: once a customer accesses the secure checkout page they are asked for billing details and emergency contact details which are saved to their profile. Credit card information is required to make the purchase. Credit card functionality is supported by Stripe. The checkout page provides customers with feedback on compliance and activity to provide a reassuring UX.
6. CHECKOUT SUCCESS PAGE: a successful purchase takes the customer to a checkout success page. This page contains the order summary with a breakdown of the order information. There are also messages to inform the customer about site actions
7. ADMIN PANEL PAGE: the admin panel page on the frontend is only accessible by a Superuser account. The Admin Panel page become visible in the Navbar once a Superuser is authenticated. The Admin Panel provides a summary of all Events. All Events are visible in the Admin Panel whether published or draft. All Events can be edited or deleted from the frontend Admin Panel.
8. ADD EVENT PAGE: Superusers also have access to an Add Event page. These pages becomes visible in the Navbar once a Superuser is authenticated. This page has full capabilities to add all required information to create an Event.
9. CONTACT PAGE: customers can use the Contact page to complete a contact enquiry. The form includes name, email and text content. The form is submitted directly to the database.
10. LOGIN / LOGOUT PAGES: Username / Email and password is required for returning users to login. Login will be remembered, depending on browser settings. When users seek to logout (via Navbar), they are asked to confirm. This is to prevent accidental logout via the Navbar. Successful login and logout are confirmed by onscreen messaging and users are returned to the home page.


<details>
<summary><strong>Flowchart of Functional Structure</strong></summary>
<br>

![Endurance Republic Function Structure](/static/img/readme/endrep-flowchart.png)
</details>
<br>

### Database Structure

Six models were created to produce the required database structure. 

1. ACTIVITY MODEL: A fully custom model. The Acivity Model determines on which activity each event is based. This model is in the event app. The includes a type and whether or not this is published, or draft. This allows the site administrator to create new activity groups, on which events can be based.
2. EVENT MODEL: A fully custom model. This model is in the event app. The Event Model contains all the information for a specific Event, which is used to display events to a site user. This model has the event name, description, duration, distance, location, date, difficult, price, published status and featured image.
3. CONTACT MODEL: A fully custom model. The Contact model is contained in the contact app and is displayed on the Contact page and consists of name, email, reason and the date on which the contact was created.
4. ORDER MODEL: A customised model. This model contains all the information required in the checkout app. The customised additional fields are: emergency contact, emergency phone number and personal medical information. This information is required at checkout to ensure that the site owner has the safety information for each participant. The order model is related to the UserProfile.
5. USERPROFILE MODEL: A customised model. This model contains billing information which can be used at checkout. The customised additional fields are: default emergency contact, default emergency phone number and default medical information. This information can be edited on the profile page in case user details change. This information is then accessed in the checkout page to prepopulate checkout.
6. ORDERLINEITEM MODEL: This model is for the line items in each order. It is related to the order and event models.

<details>
<summary><strong>Entity Relationship Diagram (ERD)</strong></summary>
<br>

![Endurance Republic ERD](/static/img/readme/endrep-erd.png)
</details>
<br>

---

## SKELETON

The skeleton of the site was designed in accordance with the scope, focusing on consistent and intuitive UX that could easily scale as the site data expanded with additional events. Wireframes for the main user and admin pages were sketched using Apple Notes. 

The wireframes provided a basic outline for the site, which was modified according to development requirements during production and user feedback.

<details>
<summary><strong>Wireframes</strong></summary>
<br>
Home Page Wireframe:

![Home Page Wireframe](/static/img/readme/endrep-home-wf.png)
<br>
<br>
Events Page Wireframe:

![Events Page Wireframe](/static/img/readme/endrep-events-wf.png)
<br>
<br>
Contact Page Wireframe:

![Contact Page Wireframe](/static/img/readme/endrep-contact-wf.png)
<br>
<br>
Bag Wireframe:

![Bag Page Wireframe](/static/img/readme/endrep-bag-wf.png)
<br>
<br>
Checkout Page Wireframe:

![Checkout Page Wireframe](/static/img/readme/endrep-checkout-wf.png)
<br>
<br>
Admin Panel Page Wireframe:

![Admin Panel Page Wireframe](/static/img/readme/endrep-admin-wf.png)
<br>
<br>
Profile Page Wireframe:

![Profile Page Wireframe](/static/img/readme/endrep-profile-wf.png)
<br>
<br>
</details>
<br>

---
## SURFACE

The surface was designed to be clean and allow focus on the Event information. The event styling was based on cards which included destination images, together with descriptive information and clear actions. 

Color palletes were chosen to reflect the theme of the outdoors and compliment the logo. A color pallete was chosen using [Coolors](https://coolors.co/). A dark blue background with white text and white cards was utilised to reflect the outdoors theme and to help key information stand out for the user.

The logo was designed using a logo generator at [FreeLogoServices](https://www.freelogoservices.com).

<details>
<summary><strong>Endurance Republic Logo</strong></summary>
<br>

![Endurance Republic Logo](/static/img/er-logo.png)
<br>
</details>
<br>
<details>
<summary><strong>Color Palette</strong></summary>
<br>

![Color palette](/static/img/readme/endrep-palette.png)
<br>
</details>
<br>

Event cards were chosen to be white to allow the important information to standout. This design was taken through the site with color text on a white background for all forms and tables. 

Buttons were styled to standout and compliment the logo with hover actions to provide user feedback. All delete, remove or cancel buttons were styled in red as a widely accepted color to direct user caution.

Two fonts were chosen for the site using [Google Fonts](https://fonts.google.com/). Cabin Sketch was used for the Endurance Republic written logo present on every page. Raleway was used for the text for the Navbar and main site content throughout the site to satisfy the UX objectives.

---

## PLANNING

## Agile Development Practices

Agile development practices were used to manage delivery throughout this project. The processes and tools are detailed below.

### Features

Initially, Features were determined to deliver the project goals defined by the Scope (above):

#### Features:

1. Accessing Event information and Navigating the Site

2. Frontend Administration to speed up changes, testing and deployment

3. Booking Events through a secure checkout

4. Profiles and management of account information

5. Customer engagement, marketing and SEO

### User Stories

User Stories were created to define the incremental elements required to deliver each Feature. The User Stories were then prioritised through the Product Backlog and tasks were identified to deliver each User Story.

The mapping of the User Stories to each Features was completed on this [Google Sheet](https://docs.google.com/spreadsheets/d/1lci3SKE9jDQtD43J5pXzI07rO_IVGJonrqBMwjrL_qk/edit?usp=share_link)

[GitHub Issues](https://github.com/marktodman/endurance-republic/issues) was used to record the User Stories. User Stories then prioritised for completion. The completion of the User Stories was managed through a [Kanban Board in a GitHuB Project](https://github.com/users/marktodman/projects/4). Based on prioritisation, each User Story was moved through the stages of Todo >> In Progress >> Done. Only one User Story (Automated Testing) currently remains in Todo and all tasks relating to the other User Stories are complete.

---

## FEATURES

## Navbar

The navbar is a responsive element, which collapses to a hamburger icon on medium and small screens. The navbar is persistent on all pages. The contents of the navbar change depending on whether the user is 1) a guest 2) an authenticated user 3) a superuser 4) whether there are items in the cart.

<details>
<summary><strong>Navbar Features</strong></summary>
<br>
Guest Navbar. Register and Login navigation is available:

![Guest Navbar](/static/img/readme/endrep-guestnavbar.png)
<br>

Authorised User Navbar. Register and Login not present and Profile icon appears:

![Signed In Navbar](/static/img/readme/endrep-authusernav.png)
<br>

Authorised User Navbar with item in cart. Cart changes to include a '+' and number of items in cart appears:

![Cart Navbar](/static/img/readme/endrep-authusercartnav.png)
<br>

SuperUser Navbar. Admin dropdown in Navbar. Dropdown shows Admin Panel and Add Event links:

![Admin Navbar](/static/img/readme/endrep-superusernav.png)
<br>

![Admin Navbar](/static/img/readme/endrep-superusernav1.png)
<br>
</details>
<br>

## Home Page

In addition to the navbar, the home page contents also change depending on when a user (either authenticated or superuser) is signed in. 

<details>
<summary><strong>Home Page Features</strong></summary>
<br>

A guest user has links to Login and Register on the home page as well as the navbar:

![Guest Homepage](/static/img/readme/endrep-guesthome.png)

An authenticated user will not have the Login or Register links on the home page:

![Authenticated Homepage](/static/img/readme/endrep-signedinhome.png)
<br>
</details>
<br>

## Events Page

The Events pages provides all available events. The page is responsive and scalable. On larger screens there are three event cards across the page. On medium size screens this reduces to two and on smaller screens, like mobiles, this reduces to one. As new events are added and published these will be added as Event Cards to the existing screen. Currently there is no limit to the number that would be displayed and there is no pagination. Pagination would have to be considered if the UX becomes impacted by the inclusion of too many events.

Each Event is presented on an Event Card which includes the details of each event, including the price and a button to Book a place which places the event in the customers cart. Only authenticated users can add an event to the cart.

<details>
<summary><strong>Events Page Features</strong></summary>
<br>

The Event page:

![Event Page](/static/img/readme/endrep-eventpage.png)
<br>

![Event Page](/static/img/readme/endrep-eventpage1.png)

If a guest user tries to book an event they will get redirected to the sign in page with a helpful message:

![Events redirect](/static/img/readme/endrep-eventmsg.png)
<br>
</details>
<br>

## Shopping Cart Page

Once an authenticated user clicks to book a place on an Event, it is added to their shopping cart. The shopping cart page can be accessed through the cart nav element, which changes to yellow, changes design to include a '+' and lists the number of items in the cart in the navbar (see navbar section above for image).

The shopping cart page provides a summary of the items in the cart. It also provides the option to remove the item from the cart, to 'keep shopping' or to proceed to 'secure checkout'.

A user cannot add more than one of the same event to the cart as this would create issues for multi-person registration, which is beyond the scope of this project (see Future Developments section below). If a user tries to add more than one of the same event, they will receive a message in the browser with instructions (see image below).

<details>
<summary><strong>Shopping Cart Page Features</strong></summary>
<br>

![Shopping Cart Page](/static/img/readme/endrep-cart.png)
<br>

Message if user tries to put more than one of the same event in their cart:

![Events redirect](/static/img/readme/endrep-cartmsg.png)
<br>
</details>
<br>

## Checkout Page

The checkout page consists of a form for the user to submit their personal details, emergency contact details, billing details and payment details. Emergency contact details are included as they are critical for those participating in adventure events. The checkout page also includes an order summary. There is form validation, so all required fields must be complete before submission. There is validation on the payment information, so only valid card payments will be processed.

<details>
<summary><strong>Checkout Page Features</strong></summary>
<br>
The checkout page requires completion of personal details, including emergency contact and medical information. This additional information is collected at checkout and displayed on the user profile. The checkout page also provides an order summary:

![Checkout Page](/static/img/readme/endrep-checkout.png)
<br>

The checkout page also includes form information for billing and payment details:

![Checkout Page](/static/img/readme/endrep-checkout1.png)
<br>

Form validation message if user tries to complete checkout without providing required fields:

![Checkout form validation](/static/img/readme/endrep-form.png)
<br>

Card form validation message if user tries to complete checkout without valid credit card information:

![Card validation](/static/img/readme/endrep-card.png)
<br>

</details>
<br>

## Checkout Success Page

Following successful submission of required fields and valid credit card information, the user is shown a checkout success page.

<details>
<summary><strong>Checkout Success Page Features</strong></summary>
<br>

The checkout success page shows the order summary details, including a unique order number:

![Checkout success summary](/static/img/readme/endrep-checkoutsuccess.png)
<br>

Checkout success message to the customer:

![Events redirect](/static/img/readme/endrep-checkoutsuccessmsg.png)
<br>
</details>
<br>

## Profile Page

When users register for the site, a profile is automatically created and the profile icon appears in the navbar. Authenticated users have access to profile page, through which they can manage all of their personal information including full name, email, emergency contact information, medical information, and billing details. This information is stored in the database and automatically retrieved to pre-populate the checkout page. If details are changed (or added0 during checkout this information is also automatically updated in the profile. The profile page also displays any orders, together with a link to the checkout success page containing the detail of each order.

<details>
<summary><strong>Profile Page Features</strong></summary>
<br>

The Profile page allows a user to update their information and provides and order summary:

![Profile page](/static/img/readme/endrep-profile.png)
<br>
</details>
<br>

## Admin Panel and Add Event

Authenticated superusers have access to an Admin Panel which provides full CRUD functionality for Events through the frontend. 

All Events are summarised in the Admin Panel page by Event Name, Description, Duration, Distance, Location, Start Date, Price and Status. All Events are shown whether draft (not displayed on the Events page) or published (displayed on the Events page). From the admin panel, Events can be edited or deleted. Events are added to the database through the Add Event page.

<details>
<summary><strong>Admin Panel Features</strong></summary>
<br>

The Admin panel page summaries Event data for the admin and provides edit and delete functionality:

![Admin Panel page](/static/img/readme/endrep-admin.png)
<br>

The edit Event page pulls the event data from the database and allows for full changes. All changes are saved to the database:

![Edit event page](/static/img/readme/endrep-editevent.png)
<br>

![Edit event page](/static/img/readme/endrep-editevent1.png)
<br>

Admins are warned that deletion cannot be undone. They have to click to continue.

![Delete event warning page](/static/img/readme/endrep-delete.png)
<br>

Admins receive notification that the deletion has been successful.

![Delete notify page](/static/img/readme/endrep-deletenotify.png)
<br>

Admins can add Events to the database. This form includes all database fields.

![Add Event page](/static/img/readme/endrep-addevent.png)
<br>

![Add Event page](/static/img/readme/endrep-addevent1.png)
<br>

Admins get confirmation of add events and choice of follow on actions.

![Add Event page](/static/img/readme/endrep-addeventconf.png)
<br>

</details>
<br>

## Contact Us

All users can access the Contact Us page to submit a request to the company. Users are asked to supply name, email and a reason for contact. The submit button posts the data to the admin area in the backend.

<details>
<summary><strong>Contact Page Features</strong></summary>
<br>

The Contact Us form:

![Contact page](/static/img/readme/endrep-contact.png)
<br>

![Contact page](/static/img/readme/endrep-contacttest.png)
<br>

The user receives notification of submission and options for follow on actions.

![Contact page](/static/img/readme/endrep-contactsub.png)
<br>

The contact information is added to the database and visible on the backend.

![Contact database](/static/img/readme/endrep-contactdata.png)
<br>
</details>
<br>

## Custom 404 Page

There is a customer 404 page to ensure that users looking for unavailable content are redirected back to relevant content on the site.

<details>
<summary><strong>Custom 404 Page</strong></summary>
<br>

![Custom 404 page](/static/img/readme/endrep-404.png)
<br>

</details>
<br>

## Email Confirmations

Successful orders receive email confirmation sent to the supplied email. Email verification requests are also sent following sign up.

<details>
<summary><strong>Successful order email example</strong></summary>
<br>

![Checkout success email](/static/img/readme/endrep-successemail.png)
<br>

</details>
<br>

---

## MARKETING and SEO

Marketing and SEO are critical components of the B2C E-commerce business model for Endurance Republic. Key features have been incorporated to support marketing activities, including a newsletter subscription and a Facebook business page. 

The newsletter audience will enable the the site owner to engage with their customers and potential customers through permission to send them marketing newsletters. The newsletter sign up is linked to Mailchimp which enables the business owner to effectively manage marketing campaigns with their audience.

The Facebook page supports audience engagement and attracts new potential customers to the site. There are social links on the site which open a link to the social sites in a new tab. The Facebook link is directed to the Endurance Republic Facebook page.

![Social Links](/static/img/readme/endrep-social.png)

<details>
<summary><strong>Newsletter Subscription</strong></summary>
<br>

![Newsletter Sign Up](/static/img/readme/endrep-newsletter.png)
<br>
<br>

The newsletter submission is recorded in Mailchimp:

![Newsletter Sign Up](/static/img/readme/endrep-mailchimp.png)
<br>
</details>
<br>

<details>
<summary><strong>Facebook Business Page</strong></summary>
<br>

![Facebook Summary](/static/img/readme/endrep-facebook.png)
<br>
<br>

![Facebook Header](/static/img/readme/endrep-facebook1.png)
<br>

![Facebook Post](/static/img/readme/endrep-facebook2.png)
<br>
</details>
<br>

---

## RESOURCES

## Languages

- Python
- HTML5
- CSS3
- JavaScript

## Frameworks & Libraries

- Django: The web app is built using the Django framework
- Bootstrap5: Frontend framework used to provide structure, style and responsive behaviour

<details>
<summary><strong>Python Libraries</strong></summary>
<br>

![Python libraries](/static/img/readme/endrep-requirements.png)

<br>
</details>
<br>

## Programs

- Heroku: Container-based cloud Platform used to deploy the VoyageVert app and host the Postgres database
- ElephantSQL: Host for the deployed production database
- AWS: Cloud hosting platform used to host static CSS files and media images
- Stripe: Managing secure payments
- GitPod: Developer platform for managing code, files and version control
- GitHub: Repository for all code. Also used to manage agile development approach
- Apple Notes: Sketching wireframes
- Lucidchart: Producing Functional Structure Flowchart and Entity Relationship Diagram
- Coolors: Color palette
- Free Logo Services: Logo generator
- Google Fonts: Fonts
- Mailchimp: Audience marketing software. Specifically supports the newsletter sign up
- Pexels: images for this project were sourced free of charge

---

## TESTING

## Validation Testing

## Lighthouse Report

Lighthouse report results are available for all guest accessible pages.

<details>
<summary><strong>Lighthouse Report Results</strong></summary>
<br>

Home page:

![Lighthouse Report](/static/img/readme/endrep-lighthouse1.png)
<br>
Events page:

![Lighthouse Report](/static/img/readme/endrep-lighthouse2.png)
<br>
Contact page:

![Lighthouse Report](/static/img/readme/endrep-lighthouse3.png)
<br>
Register page:

![Lighthouse Report](/static/img/readme/endrep-lighthouse4.png)
<br>
Sign in page:

![Lighthouse Report](/static/img/readme/endrep-lighthouse3.png)
<br>
</details>
<br>

## HTML Validation

The W3C HTML validator results are available for all guest accessible pages.

<details>
<summary><strong>HTML Validation Report Results</strong></summary>
<br>

Home page:

![W3C Report](/static/img/readme/endrep-html1.png)
<br>
Events page:

![W3C Report](/static/img/readme/endrep-html2.png)
<br>
Contact page:

![W3C Report](/static/img/readme/endrep-html3.png)
<br>
Register page:

![W3C Report](/static/img/readme/endrep-html4.png)
<br>
Sign in page:

![W3C Report](/static/img/readme/endrep-html5.png)
<br>
</details>
<br>

## CSS Validation

The custom CSS file located in the route static folder was tested using the [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) via direct code input and no errors were found:

<details>
<summary><strong>CSS Validation Report Results</strong></summary>
<br>

![W3C CSS Validation](/static/img/readme/endrep-css.png)
<br>
</details>
<br>

## Code Linting

Flake8 was used to check for code errors and to improve code readability. Flake8 was run from the gitpod terminal using the command python3 -m flake. In additon, certain files were excluded from the final assessment to improve the readability of the report. Excluded finals include directory files not altered during the project, migration files and environment files. All remaining warnings are considered acceptable to code readability and do not represent bugs.

<details>
<summary><strong>Flake8 Report Results</strong></summary>
<br>

![Flake8 report](/static/img/readme/endrep-flake.png)
<br>
</details>
<br>

## JavaScript

All JavaScript was passed through [JSHint](https://jshint.com/) to check for errors. All code passed with no errors.

<details>
<summary><strong>JSHint Report Results</strong></summary>
<br>

![JSHint report](/static/img/readme/endrep-js1.png)
<br>


![JSHint report](/static/img/readme/endrep-js2.png)
<br>
</details>
<br>


## Manual Testing

Manual testing of all site functionality was undertaken throughout production and following deployment of the production site.

All results of manual testing (48 test cases) are recorded in this [Google Sheet](https://docs.google.com/spreadsheets/d/14tIKAgv5rKZdjcnPGnsoGoLWkCGqxY6eJ_GAbqWo2Yc/edit?usp=sharing).

### Stripe

The Stripe card testing documentation can be found [here](https://stripe.com/docs/testing).

Dummy card information was used for all manual testing. All widely accepted cards from many global locations can be tested on the site.

Manual site testing was mostly undertaken using the dummy Visa Credit Card details:

![Stripe dummy card](/static/img/readme/endrep-stripedets.png)

<details>
<summary><strong>Example Stripe Webhook Results</strong></summary>
<br>

![Stripe Webhook Results](/static/img/readme/endrep-webhooks.png)
<br>
</details>
<br>

---

## DEPLOYMENT

The Endurance Republic web app is deployed via [GitHub](https://github.com/) and [Heroku](https://www.heroku.com/).

The deployed Endurance Republi web app: [Endurance Republic](https://endurance-republic.herokuapp.com/)

There are several elements to successful deployment:

1. The code base needs to be in a repository: GitHub
1. A database is required to host the data: ElephantSQL
1. Images and media need to be hosted: Amazon Web Services (AWS)
1. Payments need to be processed: Stripe
1. Sending emails: Gmail
1. The web app needs to be hosted and manage integration of the above services: Heroku

## GitHub Repository

The code is located in a [GitHub repository](https://github.com/marktodman/endurance-republic).

### Forking the GitHub Repository

To use this code and make changes without affecting the original code, it is possible to 'fork' the code on the GitHub repository through the following steps:

1. Create an account at [GitHub](https://github.com/).
1. Log into your GitHub account.
1. Go to the GitHub repository for [Endurance Republic](https://github.com/marktodman/endurance-republic).
1. Click the 'Fork' button in the upper right-hand corner of the page.
1. A copy of the repository will be available in your own repository.

## Heroku Deployment 

The site is deployed to [Heroku](https://www.heroku.com) through the following steps:

1. Log in to Heroku or create an account if required.
1. On the Welcome page click the button labelled 'New' in the top right corner, just below the header.
1. From the drop-down menu select 'Create new app'.
1. Enter a unique app name. 
1. Select the relevant geographical region.
1. Click to 'Create App'.
1. Navigate to 'Settings' and scroll down to the 'Config Vars' section. 
1. In stages (see below) you will need to add the Config Vars for:
    * ElephantSQL: Key: DATABASE_URL Value: your ElephantSQL instance URL
    * AWS: Key: AWS_ACCESS_KEY_ID Value: your AWS access key ID
    * AWS: Key: AWS_SECRET_ACCESS_KEY Value: your AWS secret
    * AWS: Key USE_AWS Value: True
    * Django Secret Key: Key: SECRET_KEY Value: your secret key
    * Stripe: Key: STRIPE_PUBLIC_KEY Value: your stripe public key
    * Stripe: Key: STRIPE_SECRET_KEY Value: your stripe secret key
    * Stripe: Key: STRIPE_WH_SECRET Value: your stripe webhook secret
    * Gmail: Key: EMAIL_HOST_USER Value: your email address
    * Gmail: Key: EMAIL_HOST_PASS Value: your app password
1. Click on the 'Deploy' tab.
1. Next to 'Deployment method' select 'GitHub'.
1. Connect the relevant GitHub repository.
1. Under 'Manual deploy' choose the correct branch and click 'Deploy Branch'. 
1. Under 'Automatic deploys' you can select 'Automatic Deploys' so that the site updates when updates are pushed to GitHub.

## ElephantSQL

1. Create an account at [ElephantSQL](https://customer.elephantsql.com/login) or use GitHub to login
1. Create a new instance
1. Create a name (suggest your project name)
1. Select a plan (suggest Tiny Turtule free plan)
1. Select region for hosting near to you
1. Create instance
1. Copy the database URL - this will be required for Heroku Config Vars and to migrate the development database

### Migrate from development database to ElephantSQL

1. In the terminal: pip3 install dj_database_url==0.5.0 psycopg2
1. Freeze requirements.txt
1. In settings.py import os and import dj_database_url
1. Set the default database to dj_database_url.parse('your-database-url-here') - do not commit with this in your settings.py!
1. Migrate changes in the terminal
1. Create SuperUser for the new database via the terminal whilst connected to the ElphantSQL database
1. Confirm migrations in ElephantSQL by executing a table query in the browser tab of the instance
1. Important! Change settings.py for the development database to 'DATABASE_URL' before commiting any changes

### Connecting ElephantSQL database to Heroku

1. Go to settings and click on 'Config Vars'
1. Add 'DATABASE_URL' to the Key
1. Add your ElephantSQL instance url to the Value
1. Click 'Add'

## Amazon WebServices

1. Create an account at aws.amazon.com
1. Open the S3 application and create an S3 bucket
1. Select AWS Region.
1. Uncheck the "Block All Public access setting" & acknowledge that the bucket will be public, it will need to be public in order to allow public access to static files.
1. In the Properties section, navigate to the "Static Website Hosting" section and click edit
1. Under the Properties section, turn on "Static Website Hosting", and set the index.html and the error.html values.
1. In the Permissions section, click edit on the CORS configuration and set the following configuration: ![Preview](/static/img/readme/cors.png)
1. Click to edit the bucket policy and set to S3 Bucket Policy and generate the policy
1. Go to the Access Control List and set the List objects permission for everyone under the Public Access section.
1. Open the IAM application to control access to the bucket and set up a user group
1. Click on Policies, and Create Policy.
1. Click on the JSON tab and import a pre-built Amazon policy called AmazonS3FullAccess:
1. Set the following settings in the JSON tab:
* Click Review Policy, give it a name and description and click Create Policy.
* To attach the policy to the group, navigate to Groups, then Permissions, and under Add Permissions, select Attach Policy.
* To create a user for the group, click Add User
* Add the user to the group created, making sure to download the CSV file which contains the user's access credentials.
* Note the following AWS code in settings.py. An environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage:

## Connecting Gmail

Gmail is a simple solution to send real emails from the web app. This is how to set up Gmail to send emails.

1. Create a Gmail account at google.com, login, go to accounts settings and click on Other Google Account Settings
1. Go to accounts and import then click on Other account settings
1. Turn on 2-step verification and follow the steps to enable
1. Click on app passwords, select Other as the app and give the password a name, for example Django or your app name
1. Click create and a 16 digit password will be generated, copy this 16 digit password
1. Add the following to settings.py:
![Preview](/static/img/readme/endrep-gmail.png)
1. Set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in the deployment host (Heroku)

## Stripe

1. Register for a [stripe account](https://stripe.com/)
1. Create an Account for your project
1. Go to the Developers section
1. Go to API keys section to access publishable and secret keys for use in settings.py and Heroku deployment
1. In the Developers section of your stripe account click on Webhooks
1. Create a webhook endpoint with the url of your website: url/checkout/wh/
1. Setup webhook handler and webhooks files in the checkout app
1. Ensure your STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WH_SECRET are all set in settings.py and production deployment host (Heroku)