# Testing

+ [Code Validation](#code-validation)
+ [User Stories](#user-stories)
+ [Features](#features)
+ [Defensive Design](#defensive-design)
+ [Minor Issues](#minor-issues)
+ [Responsiveness](#responsiveness)
+ [Browser and OS](#browser-and-os)
+ [Performance](#performance)

## Code validation
+ Python passes in PEP8 validator with no errors
+ JavaScript passes in JShint with no errors
+ CSS passes in Jigsaw with no errors
+ HTML passes in W3 Validator with no errors

## User stories

#### Basic user

1. As a user, I want to be able to read reviews by other horror fans.

  - Users can access the Book Reviews page at any permission level. They can access featured and regular book reviews from unique dynamic pages built from the MongoDB data, found by Python, and rendered on the pages with Jinja & Flask. -tested

2. As a user, I want to create a personal account.

  - All users can access the Sign Up page. -tested
  - This page is a form that uses Regex in the inputs to require a secure username and password (using special characters). I tested these inputs before adding Regex and after adding it. The input is now limited to the Regex requirements. -tested
  - Flash messages successfully appear if the user's account is created or an error message appears if an account already exists. -tested
  - The link to the Login page works as expected when clicked. -tested
  - If user successfully creates an account, the Profile page renders. -tested

3. As a user, I want to be able to login to this account.
 - All users can access the Login page. -tested
  - This page is a form that uses Regex in the inputs to require a secure username and password (using special characters). I tested these inputs before adding Regex and after adding it. The input is now limited to the Regex requirements. -tested
  - Flash messages successfully appear if the user's account is created or an account already exists. -tested
  - The link to the Login page works as expected when clicked. -tested
  - If user successfully creates an account, the Profile page renders. -tested
  

4. As a user, I want to create a review with a book image and link to buy the book.

- Users can add a book review from a form on the Add Review page. -tested
- This page only appears for logged in users. -tested
- Regex is used in the input forms for basic validation. The form only submits when these validation requirements are met. An error appears on the form if they requirements aren't met. -tested
- Materialize tooltips were used to notify users of Regex requirements. -tested
- Users are required to add a bookseller link. This link is added to a button on the Individual Reviews page. The link opens in a new tab and includes a noopener tag
			
        rel="noopener"

  

5. As a user, I want to sort books by specific subgenres.

- To build this, I created a dynamic link for each category in the Categories collection of my database. I tried to pull the categories from the Book collection with a for loop, but this didn't work when I set:

        ind_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

- Ed_Alumni in Slack suggested that I pull the category_name field from the Books collection using an $in filter.
- This filter didn't work as expected, until I changed it to a list like this:

        books = list(mongo.db.books.find(
    
        {"category_name": {"$in": [category["category_name"]]}}
    
        ))

- I added the correct Jinja for loop inside the Splide slider and the books in each category now render on the page. -tested
- Note: the slider is set to have three cards on desktop, so this design looks best when categories have more than three books in them.  I plan to fix this in future releases.

  

6. As a user, I want to rate the book using a star rating 1-5.

  - The star rating is created with custom CSS styled over input buttons. 
  - JavaScript was added to make these buttons required. 
  - To pull the rating to the input from the database on the book review pages/edit review pages, I used a Jinja for loop like this:
  
        `{% if ind_book.rating == "1" %}`

- When pulled to the review pages, and not on any forms, the input buttons still displayed the CSS that allows users to hover on the stars. These stars should be static because they're created by another user. To fix this, I created a custom CSS class to disable the hover effect.
- The rating stars now only act as input options on the forms and cannot be updated on the review pages. -tested
- The rating stars update on the review pages when a change is made to the rating on the database through the review forms. -tested
7. As a user, I want a personal profile where I can update my password.
- This form is located on the profile page that appears after a user logs in.
- Only users with a password and username who are logged in can access this form.
- The session user must input the correct username and password, then supply a new password to update this in the database. -tested
- If the user supplies the wrong username or password the password will not update and a Flash message appears. -tested
- The new password is passed through Werkzeug and is salted in the database. -tested
  

9. As a user, I want a personal profile to update and delete reviews.
- Users can only access the profile page if they have an account and are logged in with the correct credentials. -tested
- To keep the site secure and easy to use, I placed the Edit/Delete review option on the user profile instead of the main book review page. This way, only a registered user can have the option to edit reviews. -tested
- This was done by limiting the reviews on the page to the session user:

        featured = list(mongo.db.featured_books.find({"created_by": username}))

 - The edit form gives the user the option to Update, Cancel changes, or Delete the review. Both the Cancel and Delete options have a Materialize warning model that will redirect to the profile page if the user chooses not to update or delete the form. This is to prevent users from clicking the wrong button and deleting the form or migrating away from the form while updating a review. -tested

10. As a user who is neurodivergent, I want the option to switch between light and dark modes.
- To build the Light/Dark Mode toggle, I used two CSS files and JavaScript query selectors:

        var lightMode = document.querySelector(".btn-toggle");
    
        var mode = document.querySelector("#mode-link");

- This worked without issues on the site until I built the dynamic pages with Flask & Jinja. 
- To allow this feature to work on Flask & Jinja, I set this information to be stored in local storage like this:

        var selected = localStorage.getItem("css");
    
 - The light/dark mode toggle now switches the CSS style sheets on all pages when clicked. -tested

#### Superuser

1. As a superuser, I want the option to add and edit featured reviews to only appear on my profile or the profile of another superuser.

- To create this feature, I limited a tab at the top of my profile page to only display Featured for two users. -tested
- Admin and cmk416 are the only users who can access the add, edit, and delete options for featured reviews. -tested
- I created a Jinja for loop to limit this tab by users:

        {% if session.user|lower == "admin"|lower %}
    
- To protect this page, I create if statements in Python to limit the featured CRUD functions to these two users.
- On testing, the Featured tab on the profile page is not visible if I'm not a specific user. -tested
- The Featured tab does appear if I'm logged in with one of these two accounts.
  

2. As a superuser, I want to add affiliate links from Amazon so that I can make money from my reviews.

  - To create fake affiliate links, I added Amazon links that end in this tag: &tag=faketag -tested

3. As a superuser, I want to limit all form links on a site to only allow links with image extensions in the field to add a book image.

- I've used Regex in the input field to require an image file with an .jpg or .png extension. The form will only submit if an image file is added to the image input field. Otherwise, an error appears
- I had a Python if statement to check the Regex expression, which was working when originally added to the site, but on clean up testing have found it's not working as expected. I added the Regex to the input to fix this for now. 
- I plan to fix this bug on a future version of the site and add the if statement back to my Python check for the form post method.
- The form now shows a warning and will not submit unless the url format is a .jpg or .png -tested

## Features 
+ Navigation Bar

  - Is designed to have the site logo as the link to the homepage. The logo image links to the homepage from all pages- Tested
  - Hides/shows links depending on user permissions works correctly. Logged out users see the expected links and logged in users see their profile and the option to add reviews. - Tested
  - I've added jQuery to add a background colour to the active link the user is currently accessing.
  - Fixed header was added but removed due to a known bug with Materialize code caused the mobile sidenav to be unresponsive that I didn't have time to fix myself.
  -  The mobile navbar opens as expected on smaller tablets and mobile devices. -Tested
	- The mobile navbar has a X Close toggle that's visible and works. -Tested


+ Parallax background
	+ I decided to keep the Parallax background as part of the base template of the site. To support this decision, I decided to limit the height of the top part of the page. To fix any overlap between the parallax section and the footer/lower page sections, I created an overflow scroll on all forms placed over this page section. 
	+ This page design was built into the Materialze template I used to build the site, so I was wary to remove the built-in JavaScript that initialised the parallax effect. However, this caused very slow loading speeds for the site. 
	+ I used the Materialize JavaScript CDN instead and removed the full JavaScript file. To keep the parallax effect, I used the jQuery initialisation from Materialize's documentation. -Tested


- The Contact Us button
	- To set up this button, I used JavaScript, Sweet Alert, and the EmailJS (this was a form from my MS2 repurposed). 
	- The pop-out button opens when clicked on and when tabbed to, it opens if you press enter. -Tested
	- I added an error to the Sweet Alert JS, which addresses an issue with my MS2 project.
	- The form sends to EmailJS, shows a success message, and sends an automation. -Tested
	- If the form has an error for any reason, an error message will appear. -Tested

- Social links are built with FontAwesome and go to each social site's homepage. -Tested
	- Social links open the link in a new tab, have a rel="no-opener" tag, and pass all accessibility checks. -Tested

+ Flash message with specific alerts related to the users' form validation.
	- Flash messages appear on all pages where they're added. They send the appropriate message for each user action. -Tested


+ The information card over the parallax image is a Materialize card.
	- The cards are loading on the site as expected, but style-wise, I may updated the border radius to appear better on smaller screens in future version of the site. -Tested
  
+ The call to action button over this parallax image 
	- Tested, this button opens the Review page
 
+ The icon section 
	- This section stacks appropriately across different devices -Tested
  
- Splide slider to display featured reviews
	- I used this third-party slider to save time on development.
	- The slider loops through all cards added to it by Jinja for loops as expected.
	- It displays 3 cards on wider screens and 1 card on small screens.
	- The slider works properly on each page that I've added it to. -Tested
  
- Category links: Materialize chips
	- The chips size and stack responsively on all device types. -Tested

- Materialize image cards 
	- Display the book content from the MongoDB database correctly. -Tested
	- The button links on each card  on the main book reviews page and categories page open the specific book reviews page. -Tested
	- The button links on the profile page open the Edit/Delete form. -Tested
	- Cards stack and size responsively on mobile view, based on the Materialize grid system. -Tested

- Materialize breadcrumb bar to easily navigate back to main reviews page.
	- The link to return to the main book review page works as expected -Tested
	- The link to the book name keeps the user on the specific book review page as expected. 
	- Font was resized to 1.1REM on mobile because overflow, ellipsis, and the built-in Materialize truncate class didn't work on the CSS for these links. This font size is small for accessibility purposes, but I think it's more important to have the full text to help navigate the page.

- Individual/Featured Review Pages use Python and Jinja to pull book review content added by users from MongoDB. Content is organized by Materialize grid system. 
	- The Python and accompanying Jinja/Flask templating is working as expected. Book review content is displaying from the database on these dynamic pages. -Tested

- Button that opens to external bookseller page.
	- This button opens an external link correctly in a new tab and with a rel="noopener" tag -Tested


-  Materialize form elements
	- Are showing vaildation colours as expected -Tested
	- Working and sizing responsively on desktop, mobile, and tablet -Tested
	- Set the form to send only if validation requirements are met. -Tested
 

- Materialize tabs to allow users to choose different profile options.
	- Tab links open a different mini navigation section the profile page -Tested
	- The first tab has general information and an avatar image. The second as the password reset form. The third only appears to admin and cmk416 session users. -Tested
  
- Materialize image card that displays books created by the specific session user from MongoDB.
	- All book reviews for the specific session user appear as expected on the Profile page. -Tested
	- If the user hasn't created a review yet, a button appears on the profile that successfully opens the Book Reviews page -Tested

- Button to Cancel editing the review with Materialize modal warning.
	- On the add and edit review forms, the Cancel or Delete buttons open a modal when clicked. 
	- This modal displays a messages asking the user to confirm that they want to cancel working on a review or delete it entirely. I added the modal to protect users from accidentally deleting their work. 
	- Modal appears when I click either button. -Tested

- Manage Featured tab in Materialize tabs should only appear for two superusers.
	- The third tab on the Profile page only appears for admin or cmk416 when these users are logged in. 
	- I tested this by logging into another user profile without these permission, and this tab doesn't appear on the page.
  
- Button to open form that creates featured reviews.
	- This button appears in the Featured tab of the profile page for specific users and opens the Add Featured reviews form. 
	- It works upon testing.

- Button on image card to open form to add/edit featured reviews.
	 - This button appears in the Featured tab of the profile page for specific users and opens the Add Featured reviews form. 
	- It works upon testing.

- Splide slider to display featured reviews.
	- When I navigated the Featured tab on the Profile page, this slider appears.
	- The slider scrolls through the book reviews and works upon testing.

- 404 and 500 pages
    - Display and show appropriate errors on live site. -tested

## Defensive design

- I've tested the validation on all site forms to make sure Regex requirements and required fields are met.
- I've tested that only a .png or .jpg can be added to the image field on a form.
- I've tested that an error message or warning appears if a user makes an invalid form input.
- I've tested login/sign up forms to confirm that only a session user with an account can access the Profile and Add Review pages.
- I've tested that only superusers can access the Featured tab on the profile page to add, edit, and delete these reviews.
- I've added warning modals that I've tested and confirmed work as expected to Cancel and Delete buttons. This is so a user can't accidentally delete their review.

 ## Minor issues
 1. The deployed Heroku app displays http:// Not Secure after a user signs into the site. My mentor and I went through my code to check for errors that could cause this, but could find none. I'm not sure if this is a Heroku issue, but I thought it was important to note.
 2. My Python Regex expressions stopped working correctly at the last minute. I added the Regex directly the form inputs and they work now on each form. I know this is less secure, and will fix this in future versions.

 ## Responsiveness

 My main aim when building a site is to design with mobile responsiveness and accessibility first. While developing, I regularly checked the site responsiveness on Chrome and Firefox dev tools, and built my media queries accordingly.

 To test the site responsive design further, I used [Responsive Design Checker](https://responsivedesignchecker.com/checker.php?url=https%3A%2F%2Fhorror-house-reviews.herokuapp.com%2F&width=1400&height=700). With this tool, I reviewed how my site will look on desktop screens from 10-24 inches in width. I also tested it on iPad and Kindle tablet views. The site was tested on all iPhone and Android mobile devices availble. 

 It tested well across all the sample devices.

 I regularly tested my site on desktop, my iPhoneSE2 and my Kindle Fire

 ## Browser and Os
 -  I used [Lambda test](https://www.lambdatest.com/) to test out the site on different browsers and Windows devices (I develop on a MacBook Air).
 - The main difference between how the site displays on Windows and Mac are the scrollbars. I used an overflow scrollbar on most cards. The scrollbar appears for all tabs on the Profile page on Windows (Chrome, Firefox, and Internet Explorer), but remains fixed to the specific tab on Mac. The scrollbars on all other pages are set to the card section properly, so the issue is only on the Profile page on Windows. In the future, I may borrow a Windows device for extensive testing on differences between OS. 
 - I tried CSS fixes like setting the scrollbar width to thin, but this left a thinner hanging scrollbar. 
 - In the future, I will borrow a Windows device for extensive testing on differences between OS.

 Here's the issue:

Mac

 ![Mac](/static/docs/mac-chrome-scrollbar.png) 

 Windows

![Windows](/static/docs/windows-explorer-scrollbar.png)




## Performance

- I've implemented SEO features--general site metadata metadata, unique page titles--on every page so that the site scores above 90% on Lighthouse's SEO rating. I'd like to add custon link names for pages created by Flask/Jinja/Python to improve SEO in future releases.
- The site scores above 95% on all pages for accessibility. I kept the text size large on small screens, created contrast between colours, included Aria labels and tab indexes where appropriate. I enabled built-in i18n accessibility tools for the splide slider. 

Accessibility is one of the key goals for this site and one of my interests as a junior developer.
