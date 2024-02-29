import sys
import random
import json

random_number = random.randint(1, 100)

 # Create Dictionary
value = {
    "number": random_number,
    "arguments": sys.argv,
}
 

print(json.dumps(value))
