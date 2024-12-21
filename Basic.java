import java.util.Scanner;

public class Basic {
    public static void main(String[] args) {
        int n = 23;
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the value of m");
        int m = sc.nextInt();
        System.out.println("enter the value of s");
        int s = sc.nextInt();
        System.out.println("Hello world.." + n);
        System.out.println("i'm student");
        int a = 5;
        int b = 10;
        boolean c = (a < b) ? true : false;
        if (c) {
        System.out.println("a is greater");
        } else if (c) {
        System.out.println("hello");
        } else {
        System.out.println("b is greater");
        }
    }
}