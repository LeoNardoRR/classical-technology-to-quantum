import java.math.BigInteger;
import java.security.SecureRandom;

public class Descriptografar {

    public static void main(String[] args) {
        // Gerar uma chave aleatória a partir da semente
        SecureRandom secureRandom = new SecureRandom();
        byte[] chaveBytes = new byte[16]; // 16 bytes é um tamanho comum para chaves
        secureRandom.nextBytes(chaveBytes);

        // Converter a chave em formato Base64
        String chaveBase64 = new String(java.util.Base64.getEncoder().encode(chaveBytes));

        // Exibir a chave gerada
        System.out.println("Chave gerada: " + chaveBase64);

        // Usar a chave como semente para gerar números primos aleatórios
        secureRandom = new SecureRandom(chaveBytes);

        // Gerar dois números primos aleatórios
        BigInteger p = generateRandomPrime(secureRandom, 32); // 128 bits é um tamanho comum
        BigInteger q = generateRandomPrime(secureRandom, 32);

        // Calcular o número composto (produto dos números primos)
        BigInteger numeroComposto = p.multiply(q);

        // Exibir os números primos e o número composto
        System.out.println("Numero Primo p: " + p);
        System.out.println("Numero Primo q: " + q);
        System.out.println("Numero Composto: " + numeroComposto);

        // Fatorar o número composto usando o Algoritmo de Fermat
        System.out.print("Fatores primos do numero composto: ");
        BigInteger[] fatores = fatorarFermat(numeroComposto);
        for (BigInteger fator : fatores) {
            System.out.print(fator + " ");
        }
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
