import json

with open("bestiar.json", 'r') as file:
    nactena_knihovna = json.load(file)


    
    bestiar = { "nick" : "lala",
            "class" : "",
            "sila"  : "",
            "dex"   : "",
            "int"   : ""
         }

with open("bestiar.json", 'w') as file:
    json.dump(bestiar, file)
