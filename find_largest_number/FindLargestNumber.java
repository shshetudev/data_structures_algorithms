package find_largest_number;

import java.util.Scanner;

public class FindLargestNumber {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        int largestNumber = 0;

        if (a > b) {
            if (a > c) {
                largestNumber = a;
            } else {
                largestNumber = c;
            }
        } else {
            if (b > c) {
                largestNumber = b;
            } else {
                largestNumber = c;
            }
        }
        System.out.println("Largest number is: " + largestNumber);
    }
}
