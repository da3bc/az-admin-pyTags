# Azure Admin Script for Backup Tags
This Script uses a .csv File to Add Tags to Virtual Machines in your Azure Tennant


## How To

- Run Azure Resource Graph Query from .txt
- Download unformatted .csv
- Copy .csv into the same directory as the.py script
- edit the name in the script -> "with Open('csvNameHere.csv', 'r')"
- In pwsh/bash log into the tennant "az login"
- execute script
- WIN!
## Scope
At the moment you can define the scope by ediitng the KQL Query to only get the desired resources. The Script currently uses the name of the RSV and of the Policy as Tag Values. 

## What if I want to Tag another Resource Type? For Example a Storage Account?
In order to use the Script for different Resourcetypes you have to change the 2nd argument in the resource variable to the current API Version of said resourcetype
Please refere to the Microsoft documentation for said information. 

## Changelog
Current v0.1 - Basic functionality 
