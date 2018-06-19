import json
from setname import setname

#####Tady zkousim, jestli to bude fungovat na main strance
with open("bestiar.json", 'r') as file:
    test = json.load(file)

setname()
