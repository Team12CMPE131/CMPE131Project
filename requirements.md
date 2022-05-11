## Functional Requirements
1. Login - Ece
2. Logout - Ece
3. Create new account - Pranav
4. Delete account - Pranav
5. Add to cart - Pranav
6. View cart - Pranav
7. Find item - Logan
8. Bid on item - Logan
9. Compare Items - Logan
10. Sort by options - Logan
11. User Rating and review - Ece
12. Seller page or See all items from all sellers - Ece


## Non-functional Requirements
1. UI interactive interface
2. scalability
3. usability
4. compatibility

## Use Cases
1. Use Case Name:  Add to cart
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer selects "add to cart" option.9om.
- **Primary Sequence:**
  1. Customer goes on the market page.
  2. Customer selects an item from the list.
  3. Customer clicks on the “add to cart” option.
  
- **Primary Postconditions:** <can be a list or short description> 
  1. System adds sellected item to the cart of the user.
  2. System adds sellected item's price to the total cost to puchase.
  3. System checks if cart limit is reached. 
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
  1. After adding items to the cart, user clicks the “view cart” option.
  2. The system navigates the user to the cart page.
  
- **Primary Postconditions:** <can be a list or short description> 
  1. System displays the list of items that customer added in the cart or an empty space if there is not any added item.
  2. System displays the total cost of the items in the cart.
  3. It gives you an option to purchase them.
- **Alternate Sequence:** <you can have more than one alternate sequence to 
describe multiple issues that may arise>  Customer selects view the cart option before adding any items in the cart.
  
  1. The system displays an empty cart list since no item is added.
  2. The system prompts the customer to select an item to the cart.
  
  
  
3. Use Case Name:  Bid on item
- **Pre-condition:** <can be a list or short description> Customer has logged in.

- **Trigger:** <can be a list or short description> Customer clicks on the bid button under the item.
- **Primary Sequence:**
  1. Customer goes on the item's page.
  2. Customer clicks the bid textbox and enters the bid.
  3. Customer clicks enter and bid is added.
  
  
- **Primary Postconditions:** <can be a list or short description>
  1. Bid now appears in the list of bids.
  
  

4. Use Case Name: User rating
- **Pre-condition:** <can be a list or short description>  
  1. Customer has logged in.
  2. Customer has already bought the product.
  
- **Trigger:** <can be a list or short description> Customer clicks on the rate product button.
- **Primary Sequence:**
  1. The rating dropdown appears.
  2. Customer selects a number from 1 to 5.
  3. Customer clicks post.
 
  
- **Primary Postconditions:** <can be a list or short description> 

  1. The rating is now added and included in the overall rating of the product.

  
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
