import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;

public class Factoring {
    public static void main(String[] args) {
        SecureRandom secureRandom = new SecureRandom();
        byte[] keyBytes = new byte[8]; // 8 bytes = 64 bits
        secureRandom.nextBytes(keyBytes);

        String keyHex = bytesToHex(keyBytes);
        System.out.println("-------------------------------------------------");
        System.out.println("Chave gerada (em hexadecimal): " + keyHex);
        System.out.println("-------------------------------------------------");

        BigInteger keyNumeric = new BigInteger(keyHex, 16);

        BigInteger q = generateRandomPrime(32); // Gerando um número primo pequeno (32 bits)
        BigInteger p = keyNumeric.divide(q);

        BigInteger compositeNumber = p.multiply(q);
        System.out.println("Numero composto correspondente: " + compositeNumber);
        System.out.println("-------------------------------------------------");

        long startTime = System.currentTimeMillis(); // Registra o tempo inicial
        List<BigInteger> factors = factorizeAll(compositeNumber);
        long endTime = System.currentTimeMillis(); // Registra o tempo final

        System.out.print("Fatores primos do numero composto: ");
        for (BigInteger factor : factors) {
            System.out.print(factor + " ");
        }
        System.out.println("\n-------------------------------------------------");

        long duration = endTime - startTime; // Calcula a duração da fatoração em milissegundos
        System.out.println("Tempo de fatoracao: " + duration + " milissegundos");
    }

    public static BigInteger generateRandomPrime(int bitLength) {
        SecureRandom secureRandom = new SecureRandom();
        return BigInteger.probablePrime(bitLength, secureRandom);
    }

    public static List<BigInteger> factorizeAll(BigInteger number) {
        List<BigInteger> factors = new ArrayList<>();
        BigInteger factor = new BigInteger("2");

        while (number.compareTo(BigInteger.ONE) > 0) {
            if (number.mod(factor).equals(BigInteger.ZERO)) {
                number = number.divide(factor);
                factors.add(factor);
            } else {
                factor = factor.add(BigInteger.ONE);
            }
        }
        return factors;
    }

    public static String bytesToHex(byte[] bytes) {
        StringBuilder hexStringBuilder = new StringBuilder(2 * bytes.length);
        for (byte b : bytes) {
            hexStringBuilder.append(String.format("%02x", b));
        }
        return hexStringBuilder.toString();
    }
}
