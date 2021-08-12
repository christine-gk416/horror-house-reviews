# Horror House Reviews: Milestone 2

## About this project

## Live Site
***

View live deployed site [HERE](https://horror-house-reviews.herokuapp.com/)

![Responsive demo](static/images/dark-responsive.png)

From [Am I Responsive?](http://ami.responsivedesign.is/)
***
## About this project

Horror House reviews is a book review site for fans of horror novels, short stories, plays, 
or any form of literature. Fans of horror books can read reviews, sort the reviews by category, and
access featured reviews created by superusers. Members can write their own reviews, rate the book, add
categories to sort the books by subgenre, and add an external link to buy the book from a bookseller.
Members can also edit and update their reviews directly from their personal profile. Superusers can 
create featured reviews that link to affialiate links from Amazon so that these users get a commission
for book referrals.

## Table of Contents

+ [Ux](#ux)
    - User Stories
+ [Features](#features)
+ [Technologies used](#technologies)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)

***

<a name="ux"></a>

## UX Planning

### Project Goals:
<br />

+ Create a place for users to read reviews of books in the horror genre.
+ Allow uers to add and update the reviews they've created.
+ Sort books by subgenre categories for users to find books on a specific topic.
+ Allow superusers to create and edit featured reviews with affiliate links for Amazon.

### Research:
<br />

To research this project, I created accounts on book review sites so that I could test out the specific features I wanted to apply on my site. Here are the larger review sites:

[SF Book Reviews](https://sfbook.com/)

[Love Reading](https://www.lovereading.co.uk/)

[Good Reads](https://www.goodreads.com/)

The functionality and design of the site are also inspired by current sites that are specifically for horror book reviews:

[This is Horror](https://www.thisishorror.co.uk/category/reviews/)

[Sublime Horror](https://www.sublimehorror.com/)

[Horror Novel Reviews](https://horrornovelreviews.com/)
***
### User stories:
<br />

#### Basic user

1.	As a user, I want to be able to read reviews by other horror fans. 
2.	As a user, I want to create a personal account.
3.	As a user, I want to be able to login to this account. 
4.	As a user, I want to create a review with a book image and link to buy the book.
5.	As a user, I want to sort books by specific subgenres.
6.	As a user, I want to rate the book using a star rating 1-5.
7.	As a user, I want a personal profile where I can update my password.
8.	As a user, I want a personal profile to update and delete reviews.
9. As a user who is neurodivergent, I want the option to switch between light and dark modes.

<br />

#### Superuser
1.	As a superuser, I want the option to add and edit featured review to only appear on my profile or the profile of another superuser.
2.	As a superuser, I want to add affiliate links from Amazon so that I can make money from my reviews.
3.	As a superuser, I want to limit all form links on a site to only allow links with image extensions in the field to add a book image.


### Scope 

+ Create an accessible site that's easy to navigate and intuitive for all users, especially neurodivergenct users.
+ Create a site that works on all devices and sizes responsively.
+ Provide a platform for users to easily read reviews, sort them, create their own account, and write/edit/delete their book reviews.
+ Allow superusers to add, edit, and delete featured reviews from their profile.

### Structure

This website allows users to access different parts of the site depending on if they're logged in/have an account. Users are also limited to parts of the site based on their permission status.

+ Guest users: can access the homepage, the main book review page, reviews of individual and featured books, and book category links. They can also create an account and see the option to login. Guest users can only login once they've created an account.
+ Registered users: can login to the site. Once logged in, these users can add a book review from a link in the main navigation. They can also access the profile page where they can edit and delete reviews. 
+ Superusers: can create and edit featured reviews from a tab on their user profile. 

### Wireframes

### Databse structure

### Surface/Design Choices

#### Colours

Horror House reviews was designed to put accessibiity first. I'm interested in building and maintaining sites that have robust accessibility features. As a neurodiverse person with ADHD, I wanted to add dark mode as a feature on the site. 

Users with ADHD and austim may have light sensitivty that can effect their vision, especially if they're staring at a screen for a long time. 

There's some information on neurodiversity and light sensitivity in [this article](https://www.theraspecs.com/blog/adhd-light-sensitivity-hypersensitivity-sensory-processing/).

Users with autism respond best to 'soft, mild colors', according to [this article](https://livingautism.com/autism-friendly-digital-world/). In this case, I focused on soft purples and greens for main site areas and accents. 

The dark mode primary theme colour is a deep blue/grey instead of black. This is to mitigate eye-strain that can be caused by the contrast with light font colours.

Note: For future versions of this site, I plan to switch the greens over to blue/blue-grey. Accessibility can be tricky to balance, and I know that green is not accessible for users with red/green colour blindness.

Dark Mode palette:

![Dark Mode](static/images/horrorhouse-darkmode.png)

On the other hand, neurodiverse users with dyslexia prefer 'dark coloured text on a light (not white) background', following the tips from [this dyslexia group](https://www.bdadyslexia.org.uk/advice/employers/creating-a-dyslexia-friendly-workplace/dyslexia-friendly-style-guide).

In this case, I created a light mode palette that can be toggled on/off. This toggle is fixed to the right on every page.

To build light mode styles, I used the dark mode colours as accents and applied lighter versions of these colours in most of the main site sections.

![Light Mode](static/images/horrorhouse-lightmode.png)

### Fonts 


