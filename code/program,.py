'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code
import json #importing json to work with the json files
from packaging import parse_packaging, calc_total_units, get_unit #importing our functions
packages = [] #initializing packages
with open('data/packaging.txt') as f: #opening the file
    for line in f.readlines(): #reading and iterating through the lines
        line = line.strip() #removing leading and trailing whitespaces
        package = parse_packaging(line) #using parse_packaging
        total_units = calc_total_units(package) #using calc_total_units
        unit = get_unit(package) #using get_unit
        print(f"{line} => total units: {total_units} {unit}") #printing output of the functions
        packages.append(package) #adding the output of parse_packaging to packages
        with open('data/packaging.json', 'w') as f: #opening the json file to write to
            json.dump(packages, f, indent=4) #writing the packages to the json file
if __name__ == "__main__":
    main()