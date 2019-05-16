# jars - Handlebars for JSON
To install jars, run the following:
`pip install jars`

To run jars, run the following:
`jars file.json`

## Placeholders 
```json
# input 
{"source": "test", "target": "{{source}}"}

# results in 
{"source": "test", "target": "test"}
```

## Multipliers 
```json
# input
{"peoples": [{"name": "Joshua"}, {"name":  "Peter"}], "items":  [{"owner": "people.name" }]}

# results in 
{"peoples": [{"name": "Joshua"}, {"name":  "Peter"}], "items":  [{"owner": "Joshua" }, {"owner": "Peter" }]}
```
