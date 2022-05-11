## Functional Requirements
1. Login - Ece
2. Logout - Ece
3. Create new account - Pranav
4. Delete account - Pranav
5. See all items from all users
6. Add Items
7. Add to cart - Pranav
8. User Rating - Ece
9. Find items - Logan
10. Bid on Item - Logan
11. Sort Items by options - Logan
12. Compare Items or Adding Picture to Item or something else

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
  1. Customer goes on the main page.
  2. Customer selects an item from the list.
  3. Customer gets into the item’s page and clicks on the “add to cart” option to purchase it later on.
  
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

  
2. Use Case Name:  See all Items available from all of the sellers
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer selects "market page" option.
- **Primary Sequence:**
  1. 
  2. 
  3. 
  
- **Primary Postconditions:** <can be a list or short description> 
- **Alternate Sequence:** <you can have more than one alternate sequence to 
describe multiple issues that may arise>  
  
  1. 
  2. 
  
  
  
3. Use Case Name:  Bid on item
- **Pre-condition:** <can be a list or short description> Customer has logged in.

- **Trigger:** <can be a list or short description> Customer clicks on the bid button under the item.
- **Primary Sequence:**
  1. Customer goes on the item's page.
  2. Customer clicks the bid textbox and enters the bid.
  3. Customer clicks enter and bid is added.
  
  
- **Primary Postconditions:** <can be a list or short description>
  1. Bid now appears in the list of bids.
  
  

4. Use Case Name: User Rating
- **Pre-condition:** <can be a list or short description>  
  1. Customer has logged in.
  2. Customer has already bought the product.
  
- **Trigger:** <can be a list or short description> Customer clicks on the rate product button.
- **Primary Sequence:**
  1. The rating dropdown appears.
  2. Customer selects a number from 1 to 5.
  3. customer clicks post.
 
  
- **Primary Postconditions:** <can be a list or short description> 

  1. The rating is now added and included in the overall rating of the product.

  
5. Use Case Name:  Find Item
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer clicks on search icon. 
- **Primary Sequence:**
  1. Customer goes to search page or dropdown search appears.
  2. Customer enters string
  3. Customer presses enter or clicks submit
  
  
- **Primary Postconditions:** <can be a list or short description> 
  1. Results of items display on the page
  
6. Use Case Name: Add Items 
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
  
