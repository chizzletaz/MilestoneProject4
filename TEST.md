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
### First time users:
**1. As a first time user, I want to navigate easily across the website.**
- The user can navigate the website by using the links in the navbar.  
![navbar image](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/navbar.png) 

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
Because Flask Jinja template is used on all HTML pages, the source code is taken from the rendered pages to be tested.  
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
#### For index.html:
- 4 errors and 1 warning shown  
![html index error](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/html-index.png)
1. *Element `<h4>` not allowed as child of element `<ul>` in this context.*  
Fix:  
According to HTML5 spec, you can't have header tags as children within a `<ul></ul>`, you can only have `<li>` elements as children. So you should populate it with `<li></li>`, then insert your content within each list, so wrap the h4 in `<li></li>`  
Credit: [Mike Hanslo](https://stackoverflow.com/questions/29079953/element-h4-not-allowed-as-child-of-element-ul-in-this-context)
2. *Section lacks heading.*   
Fix:  
Change section into div.
3. *Start tag `<a>` seen but an element of the same type was already open.*  
I originally only had the 'go to recipe'-button acting as an anchor tag. Later I added an anchor tag to the whole card, but forgot to remove the anchor tag of the button. This resulted in an anchor tag inside another anchor tag.   
Fix:  
Change the the anchor tag of the button to a button tag and remove the href.  
This gives another error:  
4. *The element button must not appear as a descendant of the a element.*    
Fix:  
Change button tag to `<p>` tag with button class.
> Note: Since similar cards are used on the recipes and profile pages pages, these errors will be fixed there as well.

---
### CSS  
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) is used to check the CSS of the web document.
Running the code through the validator gives:
#### For style.css:
- No errors are found.  
![style.css validation](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/css-style.png)

---
### Javascript  
[JSHint](https://jshint.com/) is used to check the validity of the Javascript of the web document.  
It is recommended to add **```/* jshint esversion: 6 */```** at the top of the .js file to tell JSHint that your code uses ECMAScript 6 specific syntax.  

Running the code through the validator gives:
#### For style.js:
- No errors or warnings are shown. 
---
### Python  
[PEP8 online](http://pep8online.com/) is used to check the python code for PEP8 requirements.
#### For app.py:
Before checking the app.py file, I tried to remove as many mistakes beforehand, such as extra whitespaces, maximum
code line length of 72, correct line breaks, etc. Nevertheless, there were a lot of issues that I missed.  
- Several notifications  
![pep8 python notifications](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/python-pep8.png)  
After fixing the notifications, I get an All right message.
![All right message pep8](https://github.com/chizzletaz/BakeAndBinge/blob/master/README/images/validation/python-pep8-after.png)

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
