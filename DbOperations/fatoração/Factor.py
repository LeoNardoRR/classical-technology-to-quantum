import qsharp

def factor(n):
  """Factors a number using the brute-force algorithm."""

  client = qsharp.start_client()
  factors = client.simulate("""
    operation Factor(n: Int64): IEnumerable<Int64> {
      let factors = new ResizeArray<Int64>();

      // Iterate from 2 to sqrt(n)
      for i in 2 .. n.Sqrt() {
        if (n % i == 0) {
          factors.Add(i);
        }
      }

      // Return the list of factors
      return factors;
    }
  """, {"n": n})
  return factors

if __name__ == "__main__":
  print(factor(12))