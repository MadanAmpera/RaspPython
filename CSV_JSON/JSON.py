import json

## reading json data

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,
"felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue

## writing json data

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData
