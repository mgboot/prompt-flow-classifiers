# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool
import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def my_python_tool(input1: list) -> list:

    data = json.loads(input1)
    classes = ['Geology', 'Botany', 'Zoology']

    label_indices = []
    for c in classes:    
        if c in data['result']:
            label_indices.append(classes.index(c))

    return label_indices