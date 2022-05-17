
# CMPE131 Project - Team 12
This project simulates an ecommerce app such as Amazon or Alibaba.
# Team Members
- Pranav Pandey(@pranv11) **Team Leader**
- Ece Gulden (@ecegulden)
- Logan Dang (@Logan-Dang)


# Table of contents
* [Setup/Run](#setup/run)
* [Important Libraries to Download](#important-libraries-to-download)
* [How to Run](#how-to-run)
* [Website info](#website-info)
* [Home](#home)
* [Navigation bar](#navigation-bar)
* [User profile](#user-profile)
* [Search items](#search-items)
* [Manage items](#manage-items)
* [Listing Items](#Listing-items)
* [Technologies](#technologies)
* [Contributors](#contributors)

## Setup/Run
In the project root directory, do <code>python -m pip install -r requirements.txt</code> (python3 for mac). Then run using <code>python run.py</code>

# BTW Marketplace
# Important Libraries to Download
* Make sure you have latest python and pip installed if not download it from: https://www.python.org/downloads/ OR go to terminal and type:
    * Linux: sudo apt-get install python3
    * Mac OS: brew install python (install brew form https://brew.sh/)
* Get pip by going to terminal and type: 
    * Linux/Mac OS: $ python -m ensurepip --upgrade
    * Windows: C:> py -m ensurepip --upgrade
* After doing above steps install flask and its libraries by typing in terminal following:
    * pip install flask
    * pip install flask-wtf flask-sqlalchemy flask-login flask-bcrypt email_validator Flask-Testing

# How To Run
* To run the project: (Terminal)
    * clone the repository from: https://github.com/Team12CMPE131/CMPE131Project.git
    * from terminal navigate into project folder 
    * type in terminal : python3 run.py
    * click on http://127.0.0.1:5000/ (while pressing ctrl or cmd)
* To run the project: (IDE)
    * on your ide open the project repository 
    * navigate to project
    * run run.py
    * click on http://127.0.0.1:5000/ (while pressing ctrl or cmd)




# Website info
Crazy market place is a facebook market place like website that can be used to buy, sell and auction items.


## Instructions



### Home
When you start the website, you will be prompted to the home page of the website with get started button and login and register option to the top right of the website. If you already have an account, click on get started and login with the existing account, if not then register a new account.

### Navigation bar
Before accessing the marketpage and other features of the website, you'll have to create an account, if you're new, or sign in, if you already have an account. 
Once you log in, you will be able to see the profile( Welcome, username), cart and logout option to top right on the navigation bar and list item, market and home page option on the top left of the navigation bar.


### User profile
To view your profile, click on "Welcome, user_name" located on the navigation bar. In your profile page you can delete your profile.


### Search items
To search for an item, click in the "Search" bar located on the center of the screen and input the name of the item. 
Click enter on the keyboard or click "Search" to find items available on the market. If no items show up, the item is either not-in-stock. 

### Manage items
To buy items from the market, click on "Add to Cart" on the specific item you want to buy. Then go to "My Cart" located on the navigation bar. 
Your can see all the items that you have selected from the market on your cart page. You can either buy the product or remove it from the cart.

### Listing items
There is a listing option on the top left of the navbar. When you go on the listing page, you can either sell or list the items you want to add on the market page.



## Technologies Used
Front End:
* Bootstrap
* HTML & CSS
* JavaScript

Back End:
* Python
* Flask
* SQLite (SQLalchemy)


