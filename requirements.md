## Functional Requirements
1. Login
2. Logout
3. Create new account 
4. Delete account
5. Add to cart
6. View cart
7. Find item
8. Bid on item 
9. Add item to seller store
10. Sort by options
11. Rate item
12. Seller page

## Non-functional Requirements
1. UI interactive interface
2. non-functional
3. non-functional
4. non-functional

## Use Cases
1. Use Case Name:  Add to cart
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer selects "add to cart" option.9om.
- **Primary Sequence:**
  1. System propts user to
  2.
  
- **Primary Postconditions:** <can be a list or short description> 
  1. Customer adds an item to the cart.
  2. Item's price gets added to the total cost to puchase.
  3. It gets closer to the cart limit every time customer adds an item.
- **Alternate Sequence:** <you can have more than one alternate sequence to 
describe multiple issues that may arise>  Customer adds more items to the cart and reaches the limit of the cart.
  
  1. The system displays an error message to customer
  2. The sysyem tells the user that it reached the limit and it cannot add more items to the cart.

  - **Alternate Sequence <optional>:** <you can have more than one alternate sequence
to describe multiple issues that may arise> Customer tries to add an item which is not avalible to the cart
  
  1. The system displays an error message to the customer.
  2. It tells the user that the item is not in stock to add it to the list.
  3. The system prompts user to select an avalible item to add the cart.

  
2. Use Case Name:  View the cart
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer selects "view cart" option.
- **Primary Sequence:**
  1.
  2.
  3. 
  
- **Primary Postconditions:** <can be a list or short description> After sellecting view cart option, system displays the list of items that customer added in the cart.
- **Alternate Sequence:** <you can have more than one alternate sequence to 
describe multiple issues that may arise>  Customer selects view the cart option before adding any items in the cart.
  
  1. The system displays an empty cart list since no item is added.
  2. The system prompts the customer to select an item to the cart.
  
  
  
3. Use Case Name:  Bid on item
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer selects “Bid on item” option
- **Primary Sequence:**
  1.
  2.
  3. 
  
  
- **Primary Postconditions:** <can be a list or short description> 
- **Alternate Sequence:** <you can have more than one alternate sequence to 
describe multiple issues that may arise>
  
  1. 
  2. 
  
  
4. Use Case Name:  Find item
- **Pre-condition:** <can be a list or short description>  Customer has logged in and on the main page which has the search bar.
- **Trigger:** <can be a list or short description> Customer types the name of the item and selects the "search" option.
- **Primary Sequence:**
  1.
  2.
  3. 
 
  
- **Primary Postconditions:** <can be a list or short description> 
  1. The system displays the list of results after the customer selects the search option.
  2. Customer finds the item that is searched for. 
- **Alternate Sequence:** <you can have more than one alternate sequence to 
describe multiple issues that may arise>  Customer inputs unacceptable input to search.
  
  1. The system displays an error message if the input is not found.
  2. It tells the user that the input is not available in the system.
  3. The system prompts the customer to input a valid search item.
  

  
5. Use Case Name:  Find item
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer clicks on search icon. 
- **Primary Sequence:**
  1. Customer goes to search page or dropdown search appears.
  2. Customer enters string
  3. Customer presses enter or clicks submit
  
  
- **Primary Postconditions:** <can be a list or short description> 
  1. Results of items display on the page
  
6. Use Case Name: Add item to seller store 
- **Pre-condition:** <can be a list or short description> Seller has logged in.
- **Trigger:** <can be a list or short description> On seller page (seller view), seller clicks button "List New Item".
- **Primary Sequence:**
  1. Route to new page or modal view pops up.
  2. Seller enters item info such as name and price. Uploads a picture of the item.
  3. Click on "Confirm List". 
  
- **Primary Postconditions:** <can be a list or short description>  
  1. Item is now displayed on seller page/profile.
  2. Able to find item through search.
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence
to describe multiple issues that may arise>
  1. Route to new page or modal view pops up.
  2. Seller clicks cancel.
  3. Route back to seller page or close modal view.
  
