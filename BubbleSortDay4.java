import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'countSwaps' function below.
     *
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static void countSwaps(List<Integer> a) {
        int counter = 0;
        int t = 0;
        // Write your code here
        if (a.size() == 0) {
            System.out.println("trying to sort empty array failure");
        }
        for (int i = 0; i < a.size(); i++) {
            for (int j = 0; j < a.size() - 1; j++) {
                if (a.get(j) > a.get(j + 1)) {
                    t = a.get(j);
                    a.set(j, a.get(j + 1));
                    a.set(j + 1, t);
                    counter++;
                }

            }
        }
        System.out.println("Array is sorted in " + counter + " swaps.");
        System.out.println("First Element: " + a.get(0));
        System.out.println("Last Element: " + a.get(a.size() - 1));

    }
}

public class BubbleSortDay4 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        Result.countSwaps(a);

        bufferedReader.close();
    }
}