import java.util.Random;

public class shor {

    public static long gcd(long a, long b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    public static long shorFactor(long N) {
        Random rand = new Random();
        long x = rand.nextLong() % (N - 2) + 2;
        long y = 1;
        int count = 0;

        for (long r = 1; count < 20; r++) {
            y = x;
            for (long j = 0; j < r; j++) {
                x = (x * x) % N;
                long d = gcd(x - y, N);
                if (d > 1)
                    return d;
            }
            count++;
        }

        return -1; // Não foi possível encontrar um fator
    }

    public static void main(String[] args) {
        long N = 3417476927L; // O número a ser testado
        long factor = shorFactor(N);

        if (factor != -1) {
            long otherFactor = N / factor;
            System.out.println("Um fator de " + N + " é " + factor);
            System.out.println("O outro fator é " + otherFactor);
        } else {
            System.out.println("Não foi possível fatorar " + N);
        }
    }
}
