
public class DominoPillingDay3 {

    public int solution(int length, int width) {
        int totalDominos = 0;

        if (length == 0 || width == 0) {
            return totalDominos;
        } else {
            totalDominos = (length * width) / 2;
            return totalDominos;
        }

    }

    public static void main(String[] args) {

    }

}
