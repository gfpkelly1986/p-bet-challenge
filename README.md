# p-bet-challenge

## Preperation for Udate Forwarder Challenge:

-   Set up a new repository in github for version control.
-   Create a gitpod workspace
-   Set up an API to connect to Google Sheets using Google cloud console
-   Share the 'client email' field with Google Sheets
-   Set up a .gitignore file and add creds.json and forwarder_updates so sensitive information is not public on github
-   Import json library to deserialise the json file
-   Deserialise the forwarder_updates.json file
-   Check the type is of type 'list'
-   Set up a python file in the workspace
-   Set up files for FunBet, CrazyBet and LuckyBet in the workspace
-   Import gspread library to interact with Google Sheets
-   Set up SCOPE variables for Google Sheets access
-   Set up a Customer Updates Google Sheet with 3 seperate worksheets for FunBet, CrazyBet and LuckyBet

## Logic for Update Forwarder Challenge:

-   A functional approach to completing this challenge:

    1.  Open and deserialise the forwarder updates json file. 
    2.  Store this value in a variable called data. Contents should be of type list if an array was passed in. A dict would be the result of an object passed in.
    3.  Create a function called fun_bet that takes the data variable as an argument.
    4.  Filter the data for this customer type by values that = 'Core' for keys of 'UpdateType'
    5.  This function should return a file using the json.dump method
    6.  Call this function and store the value in a variable named fun_bet
    7.  Test this value is correct by printing to the terminal
    8.  Write the contents of the fun_bet variable into the funbet.json file
    9.  Create a function called crazy_bet that takes the data variable as an argument.
    10. Filter the data for this customer type by values that = 'SerieA' for keys of 'Competition'
    11. This function should return a file using the json.dump method
    11. Call this function and store the value in a variable named crazy_bet
    12. Test this value is correct by printing to the terminal
    13. Write the contents of the crazy_bet variable into the crazy_bet.json file
    14. Create a function called lucky_bet that takes the data variable as an argument.
    15. Filter the data for this customer type by values that >'0.25' for keys of 'Probability'
    11. This function should return a file using the json.dump method
    16. Call this function and store the value in a variable named lucky_bet
    17. Test this value is correct by printing to the terminal
    18. Write the contents of the lucky_bet variable into the lucky_bet.json file
    19. If necessary, send all files to external storage like Google Drive or Google Sheets.

- An Object Oriented approach to this challenge

    1. Open and deserialise the forwarder updates json file.
    2. Store this value in a variable called data. Contents should be of type list if an array was passed in. A dict would be the result of an object passed in. 
    3. Create a Parent Class called Update_Customer that initialises the variables Fixture Id, Competition, UpdateType, SelectionId, and Probability
    4. Create a method in this class that takes a list as an argument and returns a json file
    5. Create 3 objects of this class called FunBet, CrazyBet and LuckyBet
    6. Override the Parent Class method to allow for filtering by 'Core', 'Competition', and 'Probability' in each of the 3 objects.
    7. The objects methods should return the filtered json using json.dump()
    8. Store the values returned from calling the objects methods in variables
    9. Test these values are correct by printing to the terminal
    10. Update each file with the filtered json
    11. If necessary, send all files to external storage like Google Drive or Google Sheets.

