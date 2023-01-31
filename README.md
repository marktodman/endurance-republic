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

### E-commerce Business Model

Endurance Republic is a business to consumer (B2C) business model. We are selling places on organised adventure events in beautiful locations. Customers pay for their place via the website and can expect to have secured their place on an organised event as per the description presented for each event. Endurance Republic is responsible for organising and running the event to fulfill the contract with the customer.

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

![Color palette](/static/img/er-logo.png)
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

![Newsletter Sign Up](/static/img/readme/endrep-mailchimp.png)
<br>
</details>
<br>

<details>
<summary><strong>Facebook Business Page</strong></summary>
<br>

![Facebook Summary](/static/img/readme/endrep-facebook.png)
<br>
br>

![Facebook Header](/static/img/readme/endrep-facebook1.png)
<br>
br>

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

## Programs

- Heroku: Container-based cloud Platform used to deploy the VoyageVert app and host the Postgres database
- AWS: Cloud hosting platform used to host static CSS files and media images
- Stripe: Managing secure payments
- GitPod: Developer platform for managing code, files and version control
- GitHub: Repository for all code. Also used to manage agile development approach
- Apple Notes: Sketching wireframes
- Lucidchart: Producing Functional Structure Flowchart and Entity Relationship Diagram
- Coolors: Color palette
- Free Logo Services: Logo generator
- Google Fonts: Fonts
- Mailchimp: Audience marketing software. Specifically supports the newsletter sign up.
