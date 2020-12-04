# Custom Authentication With a Python Plugin
This repository provides a sample Python plugin for Tyk.

This plugin implements a custom authentication middleware, check our tutorial for more details.

## Modify request body and respone body with a Python Plugin

Go to Tyk Dashboard -> APIs -> Advanced Options,
- In Plugin Options, add your plugin ID 
- In Config Data, add the following JSON:

```JSON
{
    "data": {
        "field_for_request": {
            "request-key-1": "request-value-1",
            "request-key-2": "request-value-2"
        },
        "field_for_response": {
            "response-key-1": "response-value-1",
            "response-key-2": "response-value-2"
    }
}
```