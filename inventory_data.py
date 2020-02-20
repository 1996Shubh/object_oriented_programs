"""Create the JSON from Inventory Object and output the JSON String"""

import json


def main():
    file = open("inventory.json", 'r')
    data = json.load(file)
    file.close()

    for key, value in data.items():
        print(f"The {key} details are as follows: ")
        for dictionary in value:
            for keys, values in dictionary.items():
                print(f"{keys} : {values}")
        print()


main()