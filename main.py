import sys
import random
import json

# An inference example as a random number.
random_number = random.randint(1, 100)

 # Create Dictionary
value = {
    "value": str(random_number)
}

print(json.dumps(value))
