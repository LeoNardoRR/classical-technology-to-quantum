open Microsoft.Quantum.Intrinsic;

// This function factors a number into its prime factors.
// The input `n` is a non-negative integer.
// The output `factors` is a list of the prime factors of `n`.
//
// For example, the output of `Factorize(12)` would be `[2, 2, 3]`.

operation Factorize(n: Int) : IntList {
  // Initialize the list of factors to be empty.
  let factors = new IntList();

  // Iterate through all integers from 2 to `n`.
  for i in 2 .. n {
    // If `i` divides `n` evenly, add it to the list of factors.
    if (n % i) == 0 {
      factors.Add(i);
    }
  }

  // Return the list of factors.
  return factors;
}

// This function converts a list of integers from Q# to Python.
// The input `list` is a list of integers.
// The output `python_list` is a list of Python integers.

let ToPythonList(list: IntList) : IEnumerable<int> {
  // Iterate through the list of integers.
  for i in list {
    // Yield the integer to Python.
    yield return i;
  }
}

// This function prints the list of integers to the console.
// The input `list` is a list of integers.

let PrintList(list: IEnumerable<int>) : unit {
  // Iterate through the list of integers.
  for i in list {
    // Print the integer to the console.
    printfn "%d" i;
  }
}

// This is the main function.
// The input `args` is a list of command-line arguments.

let main(args: string[]) : unit {
  // Get the number to factor from the command-line arguments.
  let number = int.Parse(args[0]);

  // Factor the number.
  let factors = Factorize(number);

  // Convert the list of integers to Python.
  let python_factors = ToPythonList(factors);

  // Print the list of integers to the console.
  PrintList(python_factors);
}

let factors = Factorize(12);

// factors = [2, 2, 3]
