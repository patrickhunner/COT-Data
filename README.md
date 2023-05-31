# COT-Data

## Project Description

This is a way to extract data on Commodities and Financial futures from the Commitment of Traders Report released weekly by the CFTC. It accesses local XLSX files and populates them with historical data as well as an index calculated to provide a relative metric to look at big money buying with. There is flexibility in changing which futures items you're getting information on though calculating different datapoints would be a bit more work.

## How To Run By Cloning:

### Cloning

This is an overview of how to run the program by cloning the repository and running locally:

  ```bash
  # Go to the project directory
  cd /path/to/project
  
  # Clone the repository
  git clone https://github.com/patrickhunner/COT-Data.git
  
  # Move to app directory
  cd app
  
  # Run the program
  python analyzer.py
  ```
  
The above code will only work if you have python installed as well as the necessary dependencies. To install Python, go here. https://www.python.org/downloads/. 

Once you've done that, use pip to install the necessary dependencies as shown below:

  ```bash
  # Install dependencies
  pip install openpyxl pandas sodapy
  ```
  
### Docker

This is an overview of how to run the program with a docker container:

First, move to the directory you want to run the program in and create a directory called 'app'. Within the app directory, create 2 empty files called "Financials.xlsx" and "Commodities.xlsx".

Next, copy the files "Financials_Look_At.xlsx" and "Commodities_Look_At.xlsx" from this repo into that directory. To analyze different commodities, you can edit the first two columns, leave the rest as is.

Once this is complete, all you need to do is run the following command

  ```bash
  # Run the docker container
  docker run -v /path/to/directory/app:/app phunner/cot_compiler
  ```
  
From that, you should get the message, 

  ```bash
  WARNING:root:Requests made without an app_token will be subject to strict throttling limits.
  ```
  
Don't worry about that message, there should be no performance impact. You now will have to wait for the program to run, depending on the number of entities you want analyzed it could take a few seconds or around a minute.
