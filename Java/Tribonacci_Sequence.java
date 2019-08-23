public class Xbonacci {

  public double[] tribonacci(double[] s, int n) {
      double[] ret=new double[n];
      
      for(int i=0; i<3; i++){
        if(i==n)
          return ret;
          
        ret[i]=s[i];  
      }
      
      for(int i=0; i<n-3; i++)
        ret[i+3]=ret[i]+ret[i+1]+ret[i+2];
      
      return ret;
  }
}



/*
import java.util.Arrays;

public class Xbonacci {
  public double[] tribonacci(double[] s, int n) {

      double[] tritab=Arrays.copyOf(s, n);
      for(int i=3;i<n;i++){
        tritab[i]=tritab[i-1]+tritab[i-2]+tritab[i-3];
      }
      return tritab;

    }
}
*/