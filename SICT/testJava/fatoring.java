import java.math.BigInteger;
import java.security.SecureRandom;

public class fatoring {

    public static void main(String[] args) {
        SecureRandom secureRandom = new SecureRandom();
        byte[] chaveBytes = new byte[16]; // 16 bytes é um tamanho comum para chaves
        secureRandom.nextBytes(chaveBytes);

        String chaveBase64 = new String(java.util.Base64.getEncoder().encode(chaveBytes));

        System.out.println("Chave gerada: " + chaveBase64);

        secureRandom = new SecureRandom(chaveBytes);

        BigInteger p = generateRandomPrime(secureRandom, 32);
        BigInteger q = generateRandomPrime(secureRandom, 32);

        BigInteger numeroComposto = p.multiply(q);

        System.out.println("Numero Primo p: " + p);
        System.out.println("Numero Primo q: " + q);
        System.out.println("Numero Composto: " + numeroComposto);

        long startTime = System.currentTimeMillis(); // Registra o tempo inicial

        System.out.print("Fatores primos do numero composto: ");
        BigInteger[] fatores = fatorarFermat(numeroComposto);
        for (BigInteger fator : fatores) {
            System.out.print(fator + " ");
        }

        long endTime = System.currentTimeMillis(); // Registra o tempo final

        long duration = endTime - startTime; // Calcula a duração da fatoração em milissegundos

        System.out.println("\nTempo de fatoracao (milissegundos): " + duration);
    }

    public static BigInteger generateRandomPrime(SecureRandom secureRandom, int bitLength) {
        return BigInteger.probablePrime(bitLength, secureRandom);
    }

    public static BigInteger[] fatorarFermat(BigInteger numeroComposto) {
        // Implemente o Algoritmo de Fermat para fatoração
        BigInteger a = numeroComposto.sqrt().add(BigInteger.ONE);
        BigInteger bSquare = a.multiply(a).subtract(numeroComposto);
        while (!isSquare(bSquare)) {
            a = a.add(BigInteger.ONE);
            bSquare = a.multiply(a).subtract(numeroComposto);
        }
        BigInteger b = bSquare.sqrt();
        return new BigInteger[] { a.subtract(b), a.add(b) };
    }

    public static boolean isSquare(BigInteger number) {
        BigInteger sqrt = number.sqrt();
        return sqrt.multiply(sqrt).equals(number);
    }
}
