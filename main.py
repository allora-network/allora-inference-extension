import sys
import random
import json

# Create Dictionary
value = {
    "infererValue": str(random.randint(1, 100)), 
    "forecasterValues":  [
		{
			"node":"allo1inf1",
			"value":str(random.randint(1, 100))
		},
		{
			"node":"allo1inf2",
			"value":str(random.randint(1, 100))
		},
		{
			"node":"allo1inf1111",
			"value":str(random.randint(1, 100))
		}
	]
}

print(json.dumps(value))
