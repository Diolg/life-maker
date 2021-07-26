# Life Maker

![Home page](/media/life_maker_screenshot.png)


[View the live project here](http://life-maker.herokuapp.com/)

## Application for people, who want to improve or change their life with the help of the coaching sessions 
# Project description
“Life Maker” is an e-commerce application that allows people who want to improve their life or change their lifestyle, find the necessary guidelines in the form of coaching sessions in different categories: Health, Lifestyle, Career.  

The purpose of the application is to allow users to easily and quickly find the categories of interest to them, choose the necessary topic to work with the coach, see a brief description of the topic of the sessions, read brief information about the coach.  

The user can select the number of sessions (the duration of the session is indicated in the description) and make purchase online. Additionally, users have the opportunity to create their own account, select the number of sessions, edit the number of sessions or delete them from the shopping-bag. At the same time, users can leave their comments under the posts of the application blog.  

There are the following categories of Users:  

1.	General Users
3.	Admin (the Application Owner/the project team)  

Thus, the Application will help to:
-	Register/Sign in to the User Account
-	Sign out from the User Account
-	Easily view the list of sessions categories.
-	Easily view the list of sessions in each category.
-	Sort sessions by category/price
-	Search sessions with the search option
-	Choose sessions and add them to the shopping bag
-	Choose/edit the amount of sessions
-	Delete sessions from the shopping bag
-	Purchase the needed quantity of sessions
-	Leave comments under the application blog posts

# User Stories  

## General  

## Users First Time Visitors

-	As a first time user, I want to easily understand the main purpose of the application due to the clear layout.
-	As a first time user, I want to be able to intuitively navigate through the application.
-	As a first time user, I want the application be responsive on all devices.
-	As a first time user, I want to be able to use the application on any device .
-	As a first time user, I want to be able to navigate the application from any kind of devices.
-	As a first time user to the website, I want to easily understand the main purpose of the website.
-	As a first time user I want to easily register and login/out.
-	As a first time user I want to easily recover my password in case i forget it.
-	As a first time user I want to easily fins all the categories and sessions on the screen.
-	As a first time user i want to easily sort sessions by categories.
-	As a first time user i want to easily sort sessions by price. 
-	As a first time user i want to easily search specific sessions.
-	As a first time user i want to be able to easily access interesting to me sessions, to see their price, description, short information about coach and reviews.
-	As a first time user i want to easily add products to the shopping bag from the all sessions list or after opening the session details page.
-	As a first time user i want to easily increase or decrease number of each session.
-	As a first time user i want to easily purchase or delete the product.
-	As a first time user I want to be able to see the price of eah session as well as the total cost of the shopping bag.  
-	As a first time user I want to have an intuitively clear, fast and secure payment method.
-	As a first time user I want to easily understand how to create my own account.
-	As a first time user I want to have my own profile page with the shopping history.
-	As a first time user I want to receive onscreen or email notifications confirming my succes or failure of my actions.  
-	As a first time user i want to easily see the rating of each coaching session.
-	As a first time user i want to explore more information/articles about the problems i try to solve.
-	As a first time user i want to share my opinion regarding posted articles in the application blog.

## Returning visitors  

-	As a returning user I want to easily sign in to my account
-	As a returning user I want to easily be able to view my previous purchases.
-	As a returning user I want to edit my personal details in my account.
-	As a returning user I want to follow up if there are new coaching sessions on the website.
-	As a returning user I want to follow up new blog’s posts.
-	As a returning user I want to explore other users’ opinioin about the raised in the blog subjects.

## Admin (or a project team member)  

1.	As an Admin i want to easily add, update and delete products (sessions).
2.	As an Admin i want to easily view, update and delete customer orders.
3.	As an Admin i want to easily edit, update and delete blog posts.  

# Database Model
	[database](/media/life-maker-db_new.pdf)


# UX
The purpose of the project is to design a responsive website for all kinds of devices (mostly for the desktops and smartphones) for making navigation fast and efficient. The design has been specially made in a laconic style so that the user can easily define their actions and navigate easily.  
Thus, Users can:  

1. Due to the Home page:
-	Clearly understand that the project’s purpose is to allow people to improve their life or change their lifestyle, find the necessary guidelines in the form of coaching sessions in different categories: Health, Lifestyle, Career.  
-	Clearly understand that due to the button “choose sessions with our coaches” it is possible to be redirected to the full list of sessions to choose.  

2. Due to the Navigation bar (toggled option on mobile devices):
-	Clearly understand that there is a search option to find specific sessions by a key word.
-	Clearly understand that it is always possible to be redirected to the home page by the Logo (left side) and Home link.
-	Clearly understand that it is always possible to find information on all sessions due to the “All sessions” link as well as a drop-down menu and sort sessions by Price/Category.
-	Clearly understand that it is always possible to find information on Life Style sessions due to the “Life Style” link as well as a drop-down menu with Relationshops/Awareness development options.
-	Clearly understand that it is always possible to find information on Health sessions due to the “Health” link as well as a drop-down menu with Mental health/Sports options.
-	Clearly understand that it is always possible to find information on Career sessions due to the “Career” link as well as a drop-down menu with Creating CVhealth/Creating Personal Letter options.
-	Clearly understand that it is always possible to find some more additional information due to the Blog link and leave comments on Articles in case the User is Registered/Logged in.
-	Clearly understand that it is always possible to get to the personal Account and depending on situation Sign in/Sign Up/Sign Out. 
-	In case if the Regular User is Signed In, it is always possible to view the User’s profile with previous created orders (or to see that the shopping bag is emplty).
-	In case if the Admin User is Signed In, it is always possible to view the User’s profile with previous created orders (or to see that the shopping bag is emplty) or to do the Project Administration (add/edit/delete products).
-	Clearly understand that it is always possible to get to the personal Account and see the Shopping Bag.  

3.  Due to the All Sessions page:
-	Easily find all presented sessions with coaches.
-	Title of the Session.
-	Price
-	Category it belongs to
-	Rating
-	Edit/Delete options for Admin  

4. After hitting the Session photo, User can:
-	Clearly see (besides the Session Title/Price/Category/Rating) the Sessions description and Coach description. 
-	Easily find how to increase/deacrease session quantity in case of the future Purchase
-	Easily find how to add the Session to the Shopping Bag by hitting the relative  button.
-	Easily find how to get back to sessions by hitting the respective  button.
-	Edit/Delete options for Admin.  

5. After adding the Session to the Shopping Bag, User can:
-	Clearly see the Success/Error toast-message with the additional info. 
-	In case of Success, User clearly sees the Order information in the toast message: Session title/Quantity/Total price/Button to Secure Checkout.  
-	Easily go to the Secure Checkout due to the respective button.  

6. After hitting the Secure Checkout button, User can:
-	Clearly see the Shopping Bag with Coach photo/Session title/Quantity/Total price/Button to Secure Checkout/ Button to Keep Shopping.  
-	Clearly see the possibility to Edit/Remove the Sessions Quantity.  

7. After hitting the Secure Checkout button, User can:
-	Clearly see the Order details with Coach photo/Session title/Quantity/Order Price/Total price/ 
-	Clearly see the Order Info Form to fill out
-	Clearly see the field for entering the Card number for making  pruchase
-	Clearly see the Edit Bag/Complete Order buttons
-	Clearly see how much the User is charged.  

8. After hitting the Secure Checkout button, User can:
-	Clearly see the Order details with Order Number/Price/User name/Address and Phone Details/Total price/ 
-	Clearly see the toast (success/error) message
-	In case of success clearly see the toast message with the Order Confirmation (Order Number and message that the User will get the confirmation email)
-	Clearly see the link to Return to the Shopping.  

9. All forms are validated what makes it easier for User to apply correct actions.  

10. According to the specific actions User gets the Success/Error messages in case of successful or wrong actions.  

11. User can save previous Order Info for the easier interaction with the application.  

12. User can reset the password in case if it is forgotten.  

13. User can follow the project updates or contact the project representatives through the social links on the Footer.

## Application structure
The Website consists of 7 applications: BAG, BLOG, CHECKOUT, HOME, LIFE-MAKER, PRODUCTS, PROFILES.  
Each application allows Users to take respective actions for:  

-	familiarizing themselves with coaching sessions, 
-	choosing the right product, 
-	finding the right product, 
-	saving the desired product, 
-	editing the quantity of the product in the shopping bag, 
-	deleting products from the shopping bag
-	getting information about the planned order
-	making a purchase of the desired product
-	paying safely for the desired product
-	getting feedback about the purchase
-	reviewing with additional information about the lifestyle (for example, in a blog)
-	leaving comments

# Design

## Colour Scheme

-	The main colors used throughout the website page are as follows:      white (#fff), wine-red (rgb(233, 15, 15)), dark grey (#343A40), black (#000).
-	The overall color scheme is quite laconic in order to give user the possibility to focus in the main website purpose to easily find the appropriate product.
-	The simple logo on the left side of the navbar is presented in white and wine-red colors combination.
-	The background image together with the dark-grey navbar and footer creates the impression of consistency and is assotiated with a peaceful and calm environment.
-	The links on the navbar are presented in the wine-red color with the white hover effect to make contrast with the overall calm grey-white color pallete.
-	The dropdown menu on the navbar are created with the dark-grey background and white font to follow the consistency and be easy to read.
-	The links on the footer are presented in the wine-red color with the white hover effect to make it easier for the User to find the Project on the socail media.
-	All toast messages are created with the dark-grey background and white font to follow the consistency and be easy to read.
-	All buttons are transparent with the grey hover-effect when hitted as well as with the white text. This is done in order not to violate the general concept of the site, aimed at creating a calm atmosphere for the user.
-	To follow the consistency, the Sessions cards with the product description are created with the dark-grey background and white/red font.
-	All forms are created with white input fileds in order to make contrast with the grey background pallete.

## Typography  

The owner used 'Montserrat', sans-serif font type for all text content, including buttons. The reason for choosing this font is that it has a comfortable look and easy to read on any device. At the same time it is stylish and matches the rest of the website design.  

## Imagery  

The large, background image with a theme of stones is applied to convey the main idea of the website about harmony and balance. This image is provided throughout all application’s pages to keep the style consistency. The main idea of the photo is stones arranged vertically and keeping balance. The background of the photo is a wave, which symbolizes the preservation of balance in any situation.

# Wireframes
[Here you can find the wireframes](/media/life_maker_wireframes_new.pdf)



# Features  

## Existing features  

-	The website is responsive on all device sizes according to the initial goal.

-	Navigation bar  

1. Collapsible left-side Navigation bar (Bootstrap 4.4.1) with a toggle button (Mobile Collapse) allows making navigation bar responsive and comfortable to use on all devices.
2. The toggle button in mobile view makes it comfortable for users to navigate from smaller devices. The navbar is fixed-top, what allows users to easily navigate throughout the website.

-	Internal links on the navigation bar:
1.	Logo on the top-left side allows any time to revert back to “Home” page when clicked.
2.	“Home” - also allows to return to the Home page when clicked.
3.	Search bar allows to search for desired Sessions by Sessions names or keywords in the sessions description.
4.	“All Sessions” with dropdown menu allows to sort the sessions by Category/Price (from low ti high) or check all list of Sessions.
5.	“Life Style” with dropdown menu allows to select desired Session Category
6.	“Health” with dropdown menu allows to select desired Session Category
7.	“Career” with dropdown menu allows to select desired Session Category
8.	“Blog” allows to check the articles and leave comments for registered Users.
9.	“My Account” allows to reach the Profile, check the Order information or Log Out for Registerde/Logged-in Users.
10.	“My Account” allows to Register/Login for non-registered/non-logged in Users.
11.	“Shopping bag” icon with link leads to the Registerde/Logged-in Users Shopping Bag.  

-	Buttons
Buttons are provided by the Bootstrap (4.4.1) and allow users to easily navigate to the required page or execute a desired action. Buttons allow to sign in/sign up/sign out, create/edit/delete products from the shopping bag or during the checkput process or make/reset actions, cancel actions.  

-	Toast-messages 

Due to the js functionality, these messages in the upper right corner of the screen allow you to receive confirmation or adjust your actions and make the site more interactive.  
  
-	 Validated forms

They are provided on the pages:  

1.	Sign In
2.	Sign Up
3.	Sign Out
4.	Checkout
5.	Search  

-	Footer  

1. All pages contain the same footer.
2. Social media links on left, to Facebook, Twitter, Instagram.  

-	All Sessions page
1. Provides Users with Cards with clickable Coaches Images with the additional information in order to be able to choose a needed Session.
2. Admin is provide d the possibility to delete/edit the Sessions from Cards.
3. The JS functionality provides the possibility to scroll up to the top of the page with a red-black button on the right side of the screen.  

-   Session details Page  

1. Increase/Decrease Sessions Quantity buttons are provided.
2. “Add to bag” button is provided.
3. “Keep Shopping” button is provided (redirects User to “All Sessions” page).
4. Admin is provided the possibility to delete/edit the Sessions.  

-   Shopping Bag Page  

1. Edit/Remove Sessions Quantity Buttons are provided.
2. “Keep Shopping” button is provided (redirects User to “All Sessions” page).
3. “Secure Checkout” button is provided.  

-   Checkout Page  

1. Validated form with Name/Email/Delivery details is provided. In this case the User has an option to choose the needed country from the dropdown menu.
2. A Stripe payment field is provided below the delivery form, what allows to make a purchase.
3. “Edit Bag” (returns to the “Shopping Bag” page)/”Complete Order” buttons are provided.
4. In case If the User is logged in, an option to save the delivery information to the profile at the bottom of the form is provided in the checkbox.
5. A loading overlay is provided after the User hits the “Complete Order” button.
 
-	Blog Page  

1. Blog page is presented with posted Articles with the month/date/time
2. There is a link below each article “Read more” for logged in Users.
3. Logged in Users can follow the link and get access to the full Article and possibility to leave Comments.
4. There is a validates Form displayed with Name/Email/Body fields.
5. There is “Submit” button displayed below the From.
6. Once the “Submit” button is hit the new Comment is displayed below the Article.
7. Admin has the right to add/edit/delete Posts from the database.  

- Sign UP  

1. Non-registered Users have the possibility to Sign Up from My Account on the Navbar.
2. A validated Form with the Email/Name/Password input fields is displayed.
3. Once the Form is filled in, User sees the displayed message with the notification that a Confirmation email is sent. The real emails sending is accomplished with the help of the Google Account settings.  

## Features to Add  

-	Admin possibility to Add/Edit/Delete Blog posts on the frontend side.
-	Admin possibility to Add/Edit/Delete Blog Comments on the frontend side.
-	Functionality for getting by User the real Email Order Confirmation.





