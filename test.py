import json

with open("bestiar.json", 'r') as file:
    nactena_knihovna = json.load(file)

if nactena_knihovna["nick"] == "fgh":
    print("Shoduje se.")
elif nactena_knihovna["nick"] != "fgh":
    print("Neshoduje se.")
pass

    
    bestiar = { "nick" : "lala",
            "class" : "",
            "sila"  : "",
            "dex"   : "",
            "int"   : ""
         }

with open("bestiar.json", 'w') as file:
    json.dump(bestiar, file)
