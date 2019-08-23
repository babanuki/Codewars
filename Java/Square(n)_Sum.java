public class Kata
 {
  public static int squareSum(int[] n)
  { 
    int sum=0;
    
    for(int i : n)
      sum+=i*i;
      
    return sum;
  }
 }



/*
import java.util.Arrays;

public class Kata {
  public static int squareSum(int[] xs) {
    return Arrays.stream(xs).map(x -> x * x).sum();
  }
}
*/