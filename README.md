This repository consists of two different Azure Prompt Flow patterns that can be used as a foundation to implement binary or multiclass classification using an LLM as an intelligent classifier. Each flow consists of
- an LLM node, which is connected to a .jinja2 file containing a prompt that contains instructions and examples for the classification task
- a Python node that parses the LLM's output into Python data types (boolean for `binary` and int for `multiclass`)
- a set of Python nodes downstream of the parser that are activated by mutually exclusive outputs from the parser.

*Note: the `multiclass` flow is coded such that only one class at at time (or otherwise 'None') can be triggered; but it is possible to create a multilabel (or multivalue) classifier instead, where the parser outputs a list of found classes rather than a string indicating only one.*