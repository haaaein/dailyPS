import java.util.Scanner;
import java.util.Arrays;

public class Main {
	public static void main(String args[]) {
        Scanner num = new Scanner(System.in);
        
        int N = num.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = num.nextInt();
        }

        Arrays.sort(arr);

        for (int val : arr) {
            System.out.println(val);
        }
	}
}