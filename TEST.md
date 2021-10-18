Go to the [README file](https://github.com/chizzletaz/BakeAndBinge/blob/master/README.md)

# **Testing**
## Table of Contents
- [Testing User stories](#testing-user-stories)  
    * [First time users](#first-time-users)
    * [General users](#general-users)
    * [Regular users](#regular-users)
- [Testing Developer stories](#developer-stories)
    * [Admin/site owner](#adminsite-owner)
- [Manual testing features](#manual-testing-features)
- [Code Validation](#code-validation)  
    * [HTML](#html)
    * [CSS](#css)
    * [Javascript](#javascript)
    * [Python](#python)
- [Testing browser compatibility](#testing-browser-compatibility)  
- [Testing Responsiveness](#testing-responsiveness)  
- [Bugs and Problems](#bugs-and-problems)  
***

## Testing user stories
### Viewing and navigation:
**1. As a traveler/shopper I want to be able to	view a list of destinations/products so that I can see what is available.**
- For trip destinations, the user can navigate to the trips page via the landing page:  
![go to trips page button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-1a.png)  
or via the navbar:  
![go to trips page button navbar](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-1b.png)   
- For products, the user can navigate to the products page via the landing page:  
![go to shop page button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-1c.png)  
or via the navbar:  
![go to shop page button navbar](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-1d.png)  
- For both trips and products, the user can navigation to the page by clicking the respective link in the footer:  
![footer links](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-1e.png)

**2. As a traveler/shopper I want to be able to	view individual destinations/products so that I can identify the price, description, product rating and other details.**  
- To view individual trips and get more information about them, the user can go to the individual page by clicking the 'Read more' button
on the trips page:  
![go to trips page button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-2a.png)  
or via the navbar:  
![go to trips page button navbar](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-2b.png)  
- There they can get more information about the trip, like description, price, rating, etc.:  
![trip info](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-2c.png)  
- To view indivual products, the user can click the respective image on the shop page:  
![go to product page button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-2d.png)  
- There they can get more information about the product, like description, price, rating, etc.:  
![product info](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-2e.png)   

**3. As a traveler/shopper I want to be able to	easily find deals so that I can take advantage of special savings on products I’d like to purchase and save money.**   
- The user can navigate to shop page and then go to the deals by clicking the 'Deals' button:  
![Deals button shop](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-3a.png)  
- The checkout success page (which is shown after succesfully completing a purchase) has a link that redirects the user to the deals category.  
![Deals button checkout](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-3b.png)
- A banner is shown at the top of the page with a free delivery promotion.  
![promotion banner](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-3c.png)
- If the user is warned when they don't meet the promotion limit:  
![promotion warning](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-3d.png)
![promotion warning](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-3e.png)  

**4. As a traveler/shopper I want to be able to	easily view my shopping cart total at any time so that I can avoid spending to much.**  
- The total amount is shown at the top of the page below the shopping bag icon:  
![shopping total](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-4a.png)

**5. As a traveler/shopper I want to be able to	find information about Space Travel Agency so that I can learn more about space travel and the company.**  
- The user can navigate to the about page by clicking the link in the navbar:  
![about page link](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-5a.png)
or click the link in the footer:  
![about page link footer](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-5b.png)  

**6. As a traveler/shopper I want to be able to	contact the site owner/company so that I can get answer to my questions or get more information about certain things.**  
- The user can navigate to the contact page by clicking the link in the navbar:  
![contact page link](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-6a.png)  
or click the link in the footer:  
![contact page link footer](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-6b.png)  
- There the user can fill in a contact form:  
![contact form](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-6c.png)

**7. As a traveler/shopper I want to be able to	see reviews on the travels/products so that I can make a better decision which travel/product to buy.**  
- On the individual trip or product page, the user can scroll down to view reviews:  
![product review](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-7a.png)   


### Viewing and navigation:
**8. As a traveler/shopper I want to be able to	add, edit and delete my own review so that I can let others/the site owner know my experience and help other users.**  
- When a user is logged in they can go to an product or trip page and click the 'Write Review' button. A form will appear where they can add their review.  
![add review form](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-8a.png)  
- When a user is logged in and the review is theirs, an edit button and a delete icon is shown on their review:  
![edit review button](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-8b.png)  
- If they click the edit button, they will be redirected to the edit review page and alter the form to edit their review:  
![edit review form](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-8c.png)  
- If they click the delete icon a modal pops up to confirm if they want to delete their review:  
![delete review confirmation](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-8d.png)  


**9. As a traveler/shopper I want to be able to	easily register for an account so that I can have a personal account and be able to view my profile.**  
- A user can click the 'MY ACCOUNT' navlink and then click 'SIGN UP' to register for an account (See #13 for the user profile page):  
![sign up link](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-9a.png)  
- There the user can fill in the sign up form:  
![sign up form](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-9b.png) 


**10. As a traveler/shopper I want to be able to easily login or logout so that I can access my account and personal account information.**  
- A user can click the 'MY ACCOUNT' navlink and then click 'SIGN IN' to sign in:  
![sign in link](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-10a.png)  
- When a user is logged in, they can click the 'MY ACCOUNT' navlink and click on 'LOG OUT':  
![sign out link](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-10b.png)  


**11. As a traveler/shopper I want to be able to easily reset my password in case I forget it so that I can recover access to my account when I forget my password.**  
- On the sign in page (see above) there is a 'Forgot Password?' link:  
![forgot password link](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-11a.png)  
- After clicking the link, the user will be redirected to a password recover page, where they can fill in the form to reset their password:  
![reset password form](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-11b.png) 

**12. As a traveler/shopper I want to be able to receive an email confirmation after registering so that I can confirm that my account registration was successful.**  
- After registration (and confirmation) the allauth of Django will send a confirmation email to the address that is given.  
![confirmation email](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/images/userstory-12a.png)  

**13. As a traveler/shopper I want to be able to	 so that I can .**
**14. As a traveler/shopper I want to be able to	 so that I can .**
**15. As a traveler/shopper I want to be able to	 so that I can .**
**16. As a traveler/shopper I want to be able to	 so that I can .**
**17. As a traveler/shopper I want to be able to	 so that I can .**
**18. As a traveler/shopper I want to be able to	 so that I can .**
**19. As a traveler/shopper I want to be able to	 so that I can .**
**20. As a traveler/shopper I want to be able to	 so that I can .**
**21. As a traveler/shopper I want to be able to	 so that I can .**
**22. As a traveler/shopper I want to be able to	 so that I can .**
**23. As a traveler/shopper I want to be able to	 so that I can .**
**24. As a traveler/shopper I want to be able to	 so that I can .**
**25. As a traveler/shopper I want to be able to	 so that I can .**
**26. As a traveler/shopper I want to be able to	 so that I can .**
**27. As a traveler/shopper I want to be able to	 so that I can .**
**28. As a traveler/shopper I want to be able to	 so that I can .**
**29. As a traveler/shopper I want to be able to	 so that I can .**
**30. As a traveler/shopper I want to be able to	 so that I can .**


## Manual testing features

**Subscription option**  
Expected:   
The user is subscribed to the newsletter when the user fills in the subscription form correctly.

Testing:
1. Go to the footer of any page (except register or login).
2. Don't fill in an email address and click 'Subscribe'.
3. Confirm that a warning message appears.  
   Result:  
        A 'Subcription successfull' message appears.  
   Fix:   
        Add 'required' to the input field.  
   Result:  
        A warning message appears.
4. Fill in an invalid email address.
5. Confirm that a warning message appears.
6. Fill in a valid email address.
7. Confirm that the message 'Subscription successful!' appears.
8. Fill in the same email address.
9. Confirm that the message 'Apparently you've subscribe already. This email already exists.' appears.

Result:  
The user is subscribed to the newsletter when the user fills in the subscription form correctly.

---
## Code validation
### HTML
[W3C Markup Validation Service](https://validator.w3.org/) is used to check for markup validity of the web document.  
Because Jinja template is used on all HTML pages, the source code is taken from the rendered pages to be tested.  
You can validate the rendered page by:  
- Use the source code of the rendered page
    - Right click on the page
    - Click 'show source code'
    - Copy all HTML
    - Paste it into the validator. 

Or  
- Enter the url of the Heroku live link.

However, when authentication is used, the live link can't be used to validate the page.
Furthermore, the live site of Heroku takes a while to update.   
Therefore I've opted to use the source code to render the pages.

Running the code through the validator gives: 
#### For about.html:
- 3 errors and 1 warning three times are shown.  
![html about page errors](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-about.png)
1. *Element `<hr>` not allowed as child of element `<ul>` in this context.*  
Fix:  
You can't have header tags as children within a `<ul></ul>`, you can only have `<li>` elements as children.  
So wrap the `<hr>` in `<li></li>`.  
2. *No `<li>` element in scope but a `<li>` end tag seen.*  
Fix:  
Remove the extra `<li>` element.  
3. *The aria-labelledby attribute must point to an element in the same document.*  
The aria-labelledby doesn't point to a matching id. Add `id="offcanvasNavbarLabel"` to the `<h3>` in the offcanvas 
component.  
4. *The type attribute is unnecessary for JavaScript resources.*  
Fix:  
Up until html5 type was needed for the browser to distinguish between js and other text. With html5 it is no longer needed.
The default type for `<script>` tags is JavaScript, so you don’t need to include the type for JS resources.    
Remove the `type="text/javascript"`.  
This will be done for all the other scripts on other pages as well.  

#### For bag.html:  
- No errors or warnings to show.  
    > Note: I've added a product to the bag first.  

#### For checkout.html:  
- No errors or warnings to show.  

#### For checkout_success.html:
- No errors or warnings to show.  

#### For contact.html:  
- No errors or warnings to show.  

#### For index.html:
- No errors or warnings to show.  

#### For add_product.html:  
- 2 errors are shown.  
1. *Duplicate attribute id*  
Fix:  
The include of `include "django/forms/widgets/attrs.html"` already has an id attribute in there.  
`Select Image <input id="new-image" type="{{ widget.type }}" name="{{ widget.name }}"{% include "django/forms/widgets/attrs.html" %}>`  
So remove the `id="new-image"` from the select image.  
2. *Element p not allowed as child of element strong in this context.*  
Fix:  
remove `<strong>`.  

#### For edit_product.html:  
- 2 errors are shown.  
![html edit product errors](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-edit.png)  
1. *Duplicate attribute class.*  
Fix:  
Remove the merge the 2 classes into 1 class.  
2. *An img element must have an alt attribute, except under certain conditions.*  
Fix:  
Add an alt to the img element in custom_clearable_file_input.html.   

#### For products.html:  
- 2 errors and 2 warnings are shown 5 times.  
![html product errors](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-products.png)  
1. *Duplicate ID confirmDelete.*  
Fix:  
Create unique id's by adding the product id to delete modals by use of Jinja notation:  
`id="confirmDelete{{ product.id }}"`  
2. *Duplicate ID exampleModalLabel.*  
Fix:  
Create unique id's by adding the product id to to `<h6>` by use of Jinja notation:  
`id="exampleModalLabel{{ product.id }}"`  
> This has been done on other pages with similar forms as well.  
#### For product_detail.html:  
- 1 error is shown.  
![html product details error](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-product-detail.html)  
1. *Attribute placeholder not allowed on element select at this point.*  
Fix:  
Remove the placeholder from the select element by deleting `self.fields['rating'].widget.attrs['placeholder'] = 'Add your rating'` from the review model.  

#### For trips.html:  
- No errors or warnings to show.  

#### For trip_detail.html:  
- 7 errors and 6 warning are shown.  
![html trip detail errors 1](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-trip-detail1.png)  
![html trip detail errors 2](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-trip-detail2.png)  
1. *Duplicate ID id_title*
Partial Fix:  
Crispy forms renders the title field with it's own id based on the input title.
According to the django crispy forms docs you can change the id of the fields (label and input/select) by changing the
attribute in the forms.py.  
So I decided to make a second class named EditReviewForm and change the id's in there:  
```
class EditReviewForm(forms.ModelForm):
    """ Create a form fro users to add a review """
    class Meta:
        model = Review
        fields = ('title', 'comment', 'rating')
        widgets = {
            'title': forms.TextInput(attrs={'id': 'edit_title'}),
            'comment': forms.Textarea(attrs={'id': 'edit_comment'}),
            'rating': forms.Select(attrs={'id': 'edit_rating'}),
        }
    ...
```  
I changed the form rendering on reviews.html:  
```
{% csrf_token %}
<div class="div">
    {{ review_edit_form.title|as_crispy_field }}
</div>
<div class="div">
    {{ review_edit_form.comment|as_crispy_field }}
</div>
<div class="div">
    {{ review_edit_form.rating|as_crispy_field }}
</div>
```  
This fixes the duplicate ID's for the input and select fields.  
However, the duplicate ID's for the `<div>`'s are still there.  
![html trip detail div errors](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-trip-detail-div.png) 
After a long session with Tutoring we still couldn't fix the error.  
To be on the safe side and make the page pass the W3C validation, I've decided to put the edit review option on a different page.    
After creating a separate edit review page no more errors or warnings are shown.  

#### For profile.html:  
- 1 error is shown.  
![html profile error](https://github.com/chizzletaz/SpaceTravelAgency/blob/main/README/validation/html-profile.png)  
1. *Attribute placeholder not allowed on element select at this point*  
Fix:  
The form is rendering a placeholder for the country select element. So the select element for country shouldn't get a placeholder. 
Upon inspecting the forms.py in profile. I noticed that all elements get a placeholder with respective name due to:  
```
for field in self.fields:
    if field != 'default_country':
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
    self.fields[field].widget.attrs['placeholder'] = placeholder
```
So the to not give the country element a placeholder, the last line should be inside the `if field != 'default_country':` statement.  
```
for field in self.fields:
    if field != 'default_country':
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
```
#### For edit_review.html:  
- No errors or warnings to show.  

#### For signup.html:  
- No errors or warnings to show.  

#### For signin.html:
- No errors or warnings to show.   

---
### CSS  
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) is used to check the CSS of the web document.
Running the code through the validator gives:
#### For base.css:
- No errors are found. 

#### For checkout.css:  
- No errors are found.  

#### For product.css:  
- No errors are found.  

#### For profile.css:  
- No errors are found.

---
### Javascript  
[JSHint](https://jshint.com/) is used to check the validity of the Javascript of the web document.  
It is recommended to add **`/* jshint esversion: 6 */`** at the top of the .js file to tell JSHint that your code uses ECMAScript 6 specific syntax.  

Running the code through the validator gives:
#### For stripe_elements.js:  
- No errors or warnings are shown.  

#### For countryfield.js:
- No errors or warnings are shown.  

---
### Python  
[PEP8 online](http://pep8online.com/) is used to check the python code for PEP8 requirements.
Due to the large amound of python files, I'll only mention the files with big errors or warnings, leaving out the 
whitespace or line to long errors.
Before checking the app.py file, I tried to remove as many mistakes beforehand, such as extra whitespaces, maximum
code line length of 72, correct line breaks, etc.  
- No large errors were found.

---
## Testing browser compatibility
I've tested the website on Safari, Chrome and Mozilla Firefox.  
The testing was done by:

- Visually checking the pages.
- Checking all links.
- Checking CRUD functionality.

No issues arose during testing.  

---
## Testing responsiveness
To test the responsiveness of the  website, I've used Chrome Dev Tools by:
- right clicking on the page
- click inspect 
- click toggle device toolbar  
![toggle device toolbar button](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/toggle-device-toolbar.png)  
- select the different devices.  
![responsive choices](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/responsive.png)

and [Responsinator](https://www.responsinator.com/) to test the site at different screen resolutions.   

The testing was done on widths down to a screen resolution of 280px.  
All the elements on each page were checked.  

No issues arrose.

## Bugs and problems
Issue: Solved  
When trying to set up the link to the trip_detail page from the trips page using:
```
    <a href="{% url 'trip_detail' product.id %}" 
```
It gives an error:
![trip detail page error](https://github.com/chizzletaz/MilestoneProject4/blob/master/README/images/T-trip-detail.png)

Try:  
I've tried to change the url path in urls.py to have a different path then the trip path:
So `path('trips/<int:product_id>/' --> path('detail/<int:product_id>/'`.
This didn't work.

Fix:  
In the all_trips and trip_detail functions in views.py I changed the parameters to products, product respectively.
`trips = Product.objects.all().filter(category__name='trip') --> products = Product.objects.all().filter(category__name='trip')`

---
Issue: Solved  
When using toasts with a dark background (bg-dark), the button-close icon remained dark.
![Button Close Toast Error Image](/close-btn-toast-error.png)
Try:
Applying css to the btn-close class:
```
    .btn-close {
        color: #f1f1f1 !important;
    }
```
This didn't work.

Fix:  
According to the Bootstrap docs, you have to add the btn-close-white class to button.
This works.
![Button Close Toast Fix Image](/close-btn-toast-fix.png)

---
Issue: Solved   
When creating the checkout bag inside the success toast, the checkout button does not take the full width of the toast.
![Checkout Button Toast Error](/checkout-btn-toast-error.png)

Fix:  
According to the Bootstrap documentation, you have to wrap the button in a div with class d-grid:
```
    <div class="d-grid">
        <a href="{% url 'view_bag' %}" class="btn btn-light rounded-0">
            <span class="text-uppercase text-center">Go To Secure Checkout</span>             
        </a>
    </div>
```
This works  
![Checkout Button Toast Error](/checkout-btn-toast-fix.png)

---
Issue: Solved  
In the dropdown menu in the topnav, the link to 'Sign Up' doesn't work. The link below (sign in) does.
![sign up dropdown error](/signup-error-dropdown.png)

Try:   
It could have something to do the lowernav having a higher z-index and therefore blocking the link.
Upon inspecting the lowernav, the div with class=offcanvas, has an attribute for visibility: visible !important.
Therefore changing the z-index of the topnav should work. 
However this doesn't work.

Fix:  
Target the dropdown menu itself and add a z-index to that.
I added an id of nav-drop to the dropdown menu:
![navdrop id](/nav-drop.png)
And added a css in base.css:
```
#nav-drop {
    z-index: 999999;
}
```
---
Issue: Solved  
When adding the profile functionality (saving/updating order and/or delivery details) to the webhookhandler, the webhookhandler didn't pick this up.  

Fix:  
After checking the code, I realized that in order for stripe webhookhandler to work, the IDE has to have access to it.
Since I'm working with VSCode, I have to be logged in to Stripe every time I want to be able to listen to messages from Stripe. (After deployment, this isn't necessary and will be done automatically, as was shown in the video with GitPod).

---  
Issue: Solved
When adding/editing a product, the standard redirect is to the products page. But since I have a different page for trips,
if the product is a trip. the redirect should be redirected to the individual trip page.  

Try:  
use condition on rendering in the products view. For instance: 
```
if product.category.friendly_name == 'Trip':
    return redirect(reverse('trip_detail', args=[product.id]))
else: 
    return redirect(reverse('product_detail', args=[product.id]))
```
This syntax doesn't work.
Fix:  
```
if product.category.name == 'trip':
    return redirect(reverse('trip_detail', args=[product.id]))
else: 
    return redirect(reverse('product_detail', args=[product.id]))
```
This works! The issue was using the correct name and watch case sensitivity.

---  
Issue: Solved. 
On the product page, adding a review gives an error message.  
Try:  
A print statement after `review_form = ReviewForm(request.POST)` in the add_review view 
returns the statement, so the POST method works.  
A print statement after `if review_form.is_valid():` doesn't return the statement.
A print statement after the `else:` block of the `if review_form.is_valid():` returns the 
statement.  
So the form isn't validated in some way. 
On stackoverflow [enigma](https://stackoverflow.com/questions/5516437/django-form-has-no-errors-but-form-is-valid-doesnt-validate) suggests to use `print(form.errors)` to 
print the error at the back end. 
Placing this statement after the `else:` block gives:
 `<ul class="errorlist"><li>rating<ul class="errorlist"><li>Select a valid choice. 5 is not one of the available choices.</li></ul></li></ul>`  
So the select box gives the error for not validating the form. 
Fix:  
After checking the model I saw that I accidentally adding the rating in the wrong syntax.
I wrote the key in '' as well:
```
RATING = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
```  
It should have been:  
```
RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
```
---
Issue: Solved  
I'm trying to download my local mysql database and upload it to postgres using these steps: 

1. Make sure your manage.py file is connected to your mysql database
2. Use this command to backup your current database and load it into a db.json file:
    `python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`
3. Connect your manage.py file to your postgres database
4. Then use this command to load your data from the db.json file into postgres:
    `python3 manage.py loaddata db.json`

After the last command I'm getting this error: 
```
UserProfile(pk=1): duplicate key value violates unique constraint "profiles_userprofile_user_id_key"
DETAIL: Key (user_id)=(1) already exists.
```
So there must be some duplicate files connected to user_id=1 in the database.
Try:  
removing users, reviews and orders from the database via the admin.  
This doesn't work.  
Try:  
Reset the postgres database.
Run python3 manage.py migrate
and then the steps from above.  
This also doesn't work.  
Try:  
After consulting a Tutor (John), we managed to solve the problem.
Looking at the Review model, the Reviews are dependent on both the Product and User models, so we won't want to transfer those.  
The Review has two fields populated by an object as a ForeignKey, meaning that the User who created the view, their userProfile must exist in the database.
Because I deleted the users, it gives an error now as those Users won't exists anymore.  
The user or users who created any reviews on the local database won't be present in the deployed database. 
It's easier to just dump the data for the specific models, Category and Product 
and then once you've loaded that data, just populate some reviews by creating a new user, and manually add some reviews.  
Fix:  
Use the steps from above:
1. Connect to local sqlite database:  
Comment out the database and use:
```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```  
2. Use the same dumpdata command, but target the specific app and model.
`python3 manage.py dumpdata products.Category > categories.json`  
`python3 manage.py dumpdata products.Product > products.json`  
3. Connect to Postgres database: 
Comment out the local database and use:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
You can add the DATABASE_URL to the env.py as well.  
4. use this command to load your data from the db.json file into postgres:  
`python3 manage.py loaddata categories.json`  
`python3 manage.py loaddata products.json`

Use the normal database again.  

---
Issue: Solved.  
After editing for adding the departure date, the update quantity functionality on bag.html didn't work anymore.  
The code is as follows:  
```
$('.update-link').click(function (e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })
```
adding a print statement before and after `var form=..` gives a print statement, so the script is being called.  
And the problem seems to be getting the `.update-form`.  
Fix:  
After checking the elements on the bag.html page, `.prev` is not giving the correct element.
You have to add `parent()`. So the code becomes:  
```
$('.update-link').click(function (e) {
        var form = $(this).parent().prev('.update-form');
        form.submit();
    })
```  
---
Issue: Solved 
After runserver the terminal sometimes gives the error:  
```
UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: 
<class 'products.models.Product'> QuerySet.
paginator = Paginator(products, 6)
```  
According to [KenWhitesell](https://forum.djangoproject.com/t/unorderedobjectlistwarning-pagination-may-yield-inconsistent-results-with-an-unordered-object-list-class-myapp-models-movies-queryset-this-is-the-code-snippets-https-github-com-coderbang1-movie-app1/4549):  
A database, by default, provides an unordered and theoretically indeterminate sequence of results. You can issue two of the same query and get a different order and they both be valid.
When you’re trying to do server-side pagination, that means that you might get some of the same rows on page 2 as you had seen on page 1. Those are the inconsistent results being referred to in the warning message.

The resolution to this is to ensure that some ordering is applied to your queryset. Either adding an order_by clause on the queryset or an ordering in the Meta for that model.

Fix:  
I've opted for adding an order_by clause to the queryset:  
`products = Product.objects.all().exclude(category__name='trip').order_by('id')`  
So far, the error hasn't returned.  

---