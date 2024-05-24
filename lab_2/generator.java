import java.util.Random;

/**
* This class provides a method to generate a random sequence of bits.
*/
public class Main
{

/**
 * Generates a random sequence of bits.
 *
 * @param rand Creates a new object of class Random.
 * @param randNum The number generated at random.
 * @param binaryNum Defines what value will be output to the console: "1" or "0".
 * @return A string representing the random bit sequence.
 */
  public static void main(String[] args) {

        Random rand = new Random(System.currentTimeMillis());

        for (int i = 0; i < 128; i++) {
            long randNum = rand.nextInt(32767);
            boolean binaryNum = randNum % 2 == 1;
            System.out.print(binaryNum ? "1" : "0");
        }
    }
}