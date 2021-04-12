import json
X = '{"Name":"Ram","Class":"IV", "Age":9 }'
y = json.loads(X)
print(y["Name"])