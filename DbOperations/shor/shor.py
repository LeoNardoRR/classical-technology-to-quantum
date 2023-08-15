from qsharp.interop import *

# Create a Q# session.
session = Session()

# Load the Q# program.
session.load("factorize.qs")

# Execute the Q# program.
result = session.run(main, ["12"])

# Convert the result to a list of Python integers.
python_result = ToPythonList(result)

# Print the result to the console.
print(python_result)
