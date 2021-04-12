name,age,parent = input("Please enter name, age, parent\n>>>").split(",")
import json
N = 0
# openig the json file
with open('family.json',"r") as file:
    data = json.loads(file.read())
# making a recursive function
def assignfamily(name,age,parent,tdata):
    # if parent is not None the loop through the data and add the child to the data (RECURSIVELY)
    if parent.strip() != "None":
        for family in tdata:
            if family["name"] == parent.strip():
                if {"name": name, "age": int(age),"children" : []} not in family["children"]:
                    family["children"].append({"name": name, "age": int(age),"children" : []})
                    with open('./family.json' , 'w') as file:# finally writing the update data to json
                        json.dump(data,file,indent=4, sort_keys=False)  
                    exit()
            else:
                assignfamily(name,age,parent.strip(),family["children"])
    # if parent is None so create a new family tree   
    else:
        if {"name": name, "age": int(age),"children" : []} not in data:
            data.append({"name": name, "age": int(age),"children" : []})
        with open('./family.json' , 'w') as file:# writing the update data to json
            json.dump(data,file,indent=4, sort_keys=False)  
if data == []:
    assignfamily(name,age,parent,data)
else:
    for family in data[N:]:
        assignfamily(name,age,parent,data)
        N += 1
print("Added to the JSON")

