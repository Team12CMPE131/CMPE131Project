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
12. Changing Password - Ece
13. Extra: Budget for the purchasing


## Non-functional Requirements
1. UI interactive interface
2. scalability
3. usability
4. compatibility

## Use Cases
### 1. Use Case Name:  Add to cart
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> User clicks "add to cart" option.
- **Summary:** This feature can be used by user to add items to cart
- **Actors:** User and Server
- **Primary Sequence:**
  1. User Login.
  2. User is directed to Market Page.
  3. User clicks add to cart. 
  4. System adds sellected item to the cart of the user.
  
- **Primary Postconditions:** <can be a list or short description> 
  1. The item is added to cart

  
### 2. Use Case Name: View the cart
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> User clicks "view cart" option.
- **Actors:** User and Server
- **Primary Sequence:**
  1. User clicks view cart
  2. The system navigates the user to the cart page.
  
- **Primary Postconditions:** <can be a list or short description> 
  1. User sees the list of items that are added in the cart
  2. It gives you an option to purchase them  and remove from cart.
  
  
### 3. Use Case Name:  Bid on item
- **Pre-condition:** <can be a list or short description> Customer has logged in.
- **Trigger:** <can be a list or short description> Customer clicks on the bid button under the item.
- **Actors:** User and Server
- **Primary Sequence:**
  1. User clicks on market page.
  2. User clicks the bid textbox and enters the bid.
  3. User clicks enter and bid is added.
  
  
- **Primary Postconditions:** <can be a list or short description>
  1. Bid now appears in the list of bids.
  2. User gets the item after the bid timing finshes
  
### 4. Use Case Name: Changing Password
- **Pre-condition:** <can be a list or short description>  
  1. User has logged in.
  
- **Trigger:** <can be a list or short description> User clicks on the Change Password button.
- **Summary:** This feature allows buyer to change the passwort for his/her account.
- **Actors:** User and Server
- **Primary Sequence:**
  1. User clicks to change the password.
  2. User types the new password.
  3. User re-types the password for security.
  4. User clicks submit.
 
  
- **Primary Postconditions:** <can be a list or short description> 

  1. The system deletes the old password from the database.
  2. The system saved the new password sellected from the user.

  
### 5. Use Case Name: Find item
- **Pre-condition:** <can be a list or short description> User has logged in.
- **Trigger:** <can be a list or short description> User clicks on search icon. 
- **Summary:** This feature allows user to find item in the market.
- **Actors:** User and Server
- **Primary Sequence:**
  1. User goes to search page or dropdown search appears.
  2. User enters string
  3. User presses enter or clicks submit
  
  
- **Primary Postconditions:** <can be a list or short description> 
  1. Results of items display on the page
  
### 6. Use Case Name: Add item to seller store 
- **Pre-condition:** <can be a list or short description> Seller has logged in.
- **Trigger:** <can be a list or short description> On seller page (seller view), seller clicks button "List New Item".
- **Summary:** This feature allows user to see all the products by the seller.
- **Actors:** User and Server
- **Primary Sequence:**
  1. User is on Listing page.
  2. User enters the details of items
  3. User clicks on "Confirm List". 
  4. System adds the item to market.
  
  
- **Primary Postconditions:** <can be a list or short description>  
  1. User can see item on market
  2. Able to find item through search.
