# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool
import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def my_python_tool(input1: str) -> int:

    data = json.loads(input1)
    classes = ['Geology', 'Botany', 'Zoology', 'None']

    try:
        index = classes.index(data['result'])

    except ValueError:
        index = 3 # default to 'None' if answer is not neatly parsable into one of the classes

    return index
