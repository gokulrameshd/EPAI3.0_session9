# EPAI3.0_session9

## Project Description:
    This project contains the session 9 assignment on named tuples .
    This assignment consist of the named tuples examples and the test cases for the  respective examples .

## Named Tuples:
    Python supports a type of container like dictionaries called “namedtuple()” present in module, “collections“. Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.

## Table of Contents
- session-9-assignment-gokulrameshd  
    - .github 
        - workflow    
            - ci.yml
    - .gitignore
    - requirements.txt
    - session9.py
    - test_session9.py
    - session9_named-tuples.ipynb


## Installation

**$ git clone https://github.com/gokulrameshd/EPAI3.0_session9.git**

**$ cd EPAI3.0_session9**

**$ pip3 install -r requirements.txt**

### Running the Program
*To test the test cases* 
**$ python3 py.test** 

## Functions:

### get_named_tuple
    This function generates list of fake person details for the given population in named tuples .
    Attributes : 'name','blood_type','current_location','DOB'

### calculateAge:
    This functions helps to calculate the age from given date to present date.

### get_dict_list
    This function generates list of fake person details for the given population in dictionaries .
    Attributes : 'name','blood_type','current_location','DOB'

### named_tuple_cal
    This function calculates and returns the largest blood type, mean-current_location,
     oldest_person_age ,average age and time taken for calculation using named tuple.
   
### dict_cal
    This function calculates and returns the
    largest blood type, mean-current_location,
    oldest_person_age ,average age and time taken for calculation using Dictionary.
  
### get_symbol
    This function returns the symbol for given company name

### get_random_weights
    To create dummy weights

### get_weight
    This function return weights calculated based on the market capital 
 
### get_weights_list
    This function returns list of weights calculated based on the market capital and total market capital
   
### get_random_market_capital
    This function return random market_capital in range of 500,10000.

### update_weight
     This function update the weight in the named tuple with the calculated weights

 ### get_random_open
    This function return the random open values 

### get_high
    This function calculates the high value

### get_close
    This is function returns the close value

### create_fake_companies_list
    This function generates list of fake companies with following attributes,
    'com_name', "symbol", 'open_value', 'high_value', 'close_value','weight'
   
### get_stockmarket_points
     This function calculates the stock markets opening point , highest point , closing point.
    The points are calculated by multiplying the values with the normalized weights and summing up all the values.
   