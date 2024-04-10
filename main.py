import sys
import random
import json

# Create Dictionary
value = {
    "inferenceValue": str(random.randint(1, 100)), 
    "forecastValue":  str(random.randint(1, 100))
}

print(json.dumps(value))
