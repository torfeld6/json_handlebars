# jars - Handlebars for JSON
To install jars, run the following:
`pip install jars`

To run jars, run the following:
`jars file.json`

## Placeholders 
```json
# input 
{"source": "test", "target": "{{source}}"}

# output
{"source": "test", "target": "test"}
```

## Multipliers 
```json
# input
{"sources": [{"name": "Joshua"}, {"name":  "Peter"}], "targets":  [{"owner": "{{source.name}}" }]}

# output
{"sources": [{"name": "Joshua"}, {"name":  "Peter"}], "targets":  [{"owner": "Joshua" }, {"owner": "Peter" }]}
```
