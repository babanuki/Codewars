public class Kata {
  public static int[] invert(int[] array) {
    for(int i=0; i<array.length; i++)
      array[i]*=-1;
      
    return array;
  }
}



/*
public class Kata {
  public static int[] invert(int[] array) {
    return java.util.Arrays.stream(array).map(i -> -i).toArray();
  }
}
*/