This repository consists of three different Azure Prompt Flow patterns that can be used as a foundation to implement binary, multiclass, or multilabel classification using an LLM as an intelligent classifier.

Each flow consists of
- an LLM node, which is connected to a .jinja2 file containing a prompt that contains instructions and examples for the classification task
- a Python node that parses the LLM's output into Python data types (boolean for `binary` and int for `multiclass`)
- a set of Python nodes downstream of the parser that are activated by outputs from the parser. In the binary and multiclass flows, these outputs are mutually exclusive; only one may be activated per run. The `multiclass` flow by default allows for a "None" option, but can be modified to force the model to apply one of the given classes. The `multilabel` flow (also known as multivalue classification) allows for multiple correct classes to be turned, as well as a "None" option.