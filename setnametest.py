import json
from setname import setname

#####Tady zkousim, jestli to bude fungovat na main strance
bestiar = { "nick" : "lala",
            "class" : "",
            "sila"  : "",
            "dex"   : "",
            "int"   : ""
         }

with open("bestiar.json", 'w') as file:
    json.dump(bestiar, file)

setname()
