open Microsoft.Quantum.Intrinsic;

operation Factor(n: Int64): IEnumerable<Int64> {
  // Initialize the list of factors
  let factors = new ResizeArray<Int64>();

  // Iterate from 2 to sqrt(n)
  for i in 2 .. n.Sqrt() {
    // If i is a factor of n, add it to the list of factors
    if (n % i == 0) {
      factors.Add(i);
    }
  }

  // Return the list of factors
  return factors;
}

// This function converts a list of factors from Q# to a list of factors in Python.
let toPythonFactors(factors: IEnumerable<Int64>): List<int> =
  factors.Cast<int>().ToList();

// This function is the entry point for the program.
operation Main() {
  // Get the input number from the user.
  let inputNumber = 12;

  // Factor the number.
  let factors = Factor(inputNumber);

  // Convert the list of factors to Python.
  let pythonFactors = toPythonFactors(factors);

  // Return the list of factors to Python.
  return pythonFactors;
}