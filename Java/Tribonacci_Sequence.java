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