# Testing

A lot of testing was carried out, including Google Chrome developer tools, manual testing on desktops, laptops, mobile devices as well as different browsers (more detailed in the “Further Testing section”). The owner’s friends and family were asked to provide the feedback and test the website, what was considered in order to make the website more attractive visually and easier to navigate (more details in the “Known Bugs” section).  




# Manual testing of all elements and funcionality

- Navigation bar  

1. Click all the navbar items to verify they work properly and lead to respective pages.
2. Change the screen size (desktop, tablet, mobile) to ensure that the navigation bar is collapsible and the toggle button functions properly.
3. Non-logged/Loggedin Users see: Logo, Search, My Account, Shopping Bag as well as Home, All Sessions (with dropdown), Life Style(with dropdown), Health(with dropdown), Career(with dropdown), Blog links.
4. Non-logged/Loggedin Users can reach all the respective pages from the dropdown menu links.
5. Non-logged/Logged in Users can sort Sessions by Price/by Category in All Sessions dropdown menu.
6. Non-logged/Logged in Users can reach all Sessions categories from all dropdown menus.
7. Non-logged/Logged in Users can open Blog articles.
8. Non-logged Users can Register/Login from “My Account” and see the success toast message on the right top.
9. Logged-in Users when hit “My Account” can reach “My Profile” and “Logout”.
10. Admin when hits “My Account” can reach “My Product Administration”.
- Footer 
1. Resize window width to check the footer resposivity on different devices.
2. Social Media icons lead to the external links.
- Home page
1. Non-logged/Logged in Users see the “Choose your sessions with our coaches” button.
2. Non-logged/Logged in Users after hitting the “Choose your sessions with our coaches” button are redirected to the “All sessions page”  

- Sign-up/Sign-in/Sign-out functionality  

Registering  

1. When hitting Sign up, non-registered User is redirected to the Sign Up page with the form.
2. There is the alternative to Sign in in case if User is already registered.
3. If login/email are already used for registration User gets the notification below the respective input fields.
4. An error message displays if the emails entered do not match.
5. An error message displays if the passwords entered do not match.
6. If one of the required fields is not filled, User gets notification near to the respective input field.
5. After User signs up, a confirmation page displays with the notification that User will get an email to confirm with a respective link.
6. A check should be done to confirm the email was sent to the desired email address.

Authenticatication  

1.	Login link displays the  "Sign In".
2.	Displays "If you have not created an account yet, then please sign up first". "Sign up"  is a link directing to the register page.
3.	"Login" and "Password" should be displayed
4.	An error message is displayed if the user name is not registered and/or if the password is incorrect.
5.	An error message displays if any of the input fields are not completed or are not in the correct format.
6.	There is checkbox displaing "Remember Me". In case if it is chosen, User’s data should be saved (in this case login is not required).
7.	There are “Home” and “Sign in” buttons displayed and redirect User to the needed pages.
8.	"Forgot password" link  displays below buttons redirecting to the pages in order to reset the password.
9.	User receives the reset password email.
10.	Email provides a link to return to the website. The User must be able to enter a new password.
11.	The user should be able to see a message on the page "Password reset". 
12.	If the new password works properly when logged in, success message must appear.
13.	Logout Page displays as "Sign Out" . After selecting the button "Sign Out" Users must be redirected to the home page. A success message "You have signed out" should be displayed.  

-	Profile Page  

1.	Displays as "My Account".
2.	A prefilled form with the title Default delivery information“ must be displayed.
3.	Form contains phone number, street address 1, street address 2, town or city, county, postal code, country to choose from dropdown menu (if not prefilled).
4.	A "Update Information" button should be displayed.
5.	To check if the “’Update” workes properly, a User fills selected fields with the new information, hits the “Update” button. A success toast message should appear. 
6.	The “Order history” should be displayed on the right side of the Delivery infromation Form. Order Number, Date, Items and Order Total with the respective amout should be displayed.
7.	The new order should appear in the Order history.  

-	Sessions Page  

1.	Displays as "All sessions" on the Navbar.
2.	Sessions must be sorted by Price and Category from the Navbar.
3.	Sessions are diaplayed by 3 in each row on medium/large devices and 1 item in the row on small mobile devices.
4.	All sessions should be presented in the database.
6.	Each session must be presented with the Coach image, session title, price, category, rating.
7.	For the Admin buttons edit/delete are available.
8.	When clicked on the image User should be redirected to the session details page.
9.	A scroll up arrow button should be displayed on the right side of the page to redirect User t the top of the page.  


-	Session details page
1.	A header in the center should be presented.
2.	The Coach image on the right side of the page should be presented.
3.	On the right side from the image the Session information is displayed: title, price, category, rating,  (for Admin only) edit(leads to the form with the product information, at the same time an alert message appears)/delete options, Session description, brief information about Coach.
4.	Below the description option for increasing/decreasing Sessions quantity should be displayed. Increasing/decreasing option should be tested in order to add or remove specific quantity of Sessions. 
5.	“Add to bag” button should be presented, after hitting it a success-toast appears with the Session title, quantity, total price and “Secure checkout” button, which should lead to the “Shopping Bag”.
6.	Below the “Add to bag” button a “Keep shopping” button should appear, which leads to the “All sessions” page.
7.	The "Keep Shopping" button should direct to the all products page.  


-	Shopping Bag page  

1.	Displayed as "Shopping Bag"
2.	Displays Session title, Coach image, quantity, price, total, bag total
3.	Sessions quantity can be Edited or Removed by User. To test it press minus/plus icons and “edit”/”remove” accordingly. After “edit” hitting a succes toast with new product quantityt should appear. After hitting “remove” a page with the message “This bag is empty” should be displayed with “Keep shopping” button as well as the success toast-message.
4.	Two buttons should be displayed on the page buttom: “Keep shopping”(redirects to “All sessions page”)/”Secure checkout”(redirects to the order/delivery form and displayed chosen Session)
5.	If the User logs out on this stage and after that loggs in again, the Shopping bag should be empty.  

-	Checkout  

1.	The checkout page appears after User selected Sessions to the Shopping Bag.
2.	Ithe page is displayed as "Checkout".
3.	Logged out users can reach only selecting the items to their Shopping Bag and before Secure checkout they will be offered to "login / register now to save your delivery information and order history". This is achieved with the "Register" and "Login" functionality. 
4.	Order summary is displayed with the Coach image, Session title, quantity, Order total and Bag total.
5.	Delivery information must be presented in "Details", "Delivery" and Payment".
6.	The delivery information form should full name, email address, phone number, country (dropdown), postal code, town or city, street address 1, street address 2, and should be prefilled for logged in users.
7.	For logged in users "Save this delivery information to my profile" with a checkbox must display below the form. 
8.	The payment should be complete by using the stripe test card number  and by  selecting "Complete order". A loadin overlay should be shown it should direct to the checkout success page with a toast message to confirm. 
9.	The Stripe test card details are:
•	Card: 4242 4242 4242 4242
•	MM/YY, CVC and ZIP: 04/24 242 42424.
12.	To check if the order has succeded, login to the Django Admin database.
13.	Near to the “Complete order” button "Edit Bag" button is displayed, which redirects  to the shopping bag page, where User can change needed data.
14.	Below the buttons "You will be charged $(amount)". This amount should match the bag total.  

- Checkout Success  

1. Should be displayed as "Thank you".
2. A success-toast message sould appear with the confirmation.
3. The "Order summary" with order number, order date, delivery details, order total and grand total shpuld appear.  
The order total and grand total should match.
4. A link to "All Sessions" page should be displayed below the order details.  

- Edit Product Page  

1. It is only accessible for logged in Admin.
2. Displayed as "Product Administration".
3. Displayed with the subtitle "Update Product".
4. Contains a pre-filled form with the information with the categories option (dropdown), sku, name, description, price, delivery cost, rating, image url, current image.
6. "Cancel" should direct to "All Sessions" page.
7. Selecting checkbox with "Remove" and after that hitting the "Update product" button should update product without image.
8. When "Select image" hitted, Admin can upload the image, hit the "Update product" button and new Coach image should appear.
9. Check functionality by updating all fields and selecting "Update product". This will redirect to the updated session detail page.
10. An alert message on the right top should appear about the current editing process.  


- Add Product Page  

1. It is only accessible for logged in Admin  
2. Displayed as "Product Administration" in the "My Account" on the Navbar.
3. On the separate page displayed as "Add Product".
4. Contains an empty form with the Category(dropdown), sku, name, description, price, rating, image url, select image option.
5. "Cancel" should direct to "All sessions" page.
6. Functionality can be chacked by adding information to all fields and selecting "Add product". This should direct to the new product detail page. The new Session shpuld be displayed on "All Sessions" page.  

- Blog Page

1. Blog page is accessible for logged-in/non-logged in Users by hitting the "Blog" link on the navbar.
2. It is displayed with the title "Check out our latest articles" and the subtitle "Leave your comments".
3. Several posts should be displayed by Admin from the database.
4. Users see: the post title, date, year, time when it was posted, intro and "Read more" link.
5. Only logged-in Users can go to the full article and leave comments.
6. When logged-in User hits the  "Read more" link they see the full article, month, date, year. tiemwhen it was posted. They also see below the other users' comments as well as the "Add Comment" form with name, email, body input fields.
7. The form should be filled in and the "Submit" button should be hit. That will post the new comment above the form.
8. Admin can add/edit/delete Posts as well as Comments from the database (the frontend management will be applied later)  







## Further Testing
- The website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 8, Xiaomi Mi Note 10, Xiaomi Note 10 Pro.
- A large amount of testing was done to ensure that all internal/external links work correctly.
- Friends and family members were asked to review the website to point out any bugs and/or user experience issues.  

















# Acknowledgements
- To my husband and other members of my family as well as friends for helping me in testing the website.
- To my mentor Medale Oluwafemi for patience and helping me through the process.
- To tutors (especially, to Igor_CI) and peers from Slack community, for support and prompt reactions during the process.













