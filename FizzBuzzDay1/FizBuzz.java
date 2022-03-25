package FizzBuzzDay1;

import java.util.ArrayList;
import java.util.List;

class FizBuzz {
    public List<String> solution(int n) {
        List<String> answer = new ArrayList<String>();
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                answer.add("FizzBuzz");
            } else if (i % 3 == 0 || i % 5 == 0) {
                answer.add(i % 3 == 0 ? "Fizz" : "Buzz");

            } else {
                answer.add(Integer.toString(i));

            }

        }

        return answer;
    }

}