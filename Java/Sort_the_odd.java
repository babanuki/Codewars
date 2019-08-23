import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.util.Comparator;

public class Kata {
  public static int[] sortArray(int[] array) {
    int j=0;
    List<Integer> idx=new ArrayList<Integer>();
    List<Integer> arr=new ArrayList<Integer>();
    
    for(int i=0; i<array.length; i++)
      if(array[i]%2==1){
        arr.add(array[i]);
        idx.add(i);
      }
    
    Collections.sort(arr);
    
    for(Integer i : idx)
      array[i]=arr.get(j++);
    
    return array;
  }
}



/*
import java.util.*;

public class Kata {

  public static int[] sortArray(final int[] array) {

    // Sort the odd numbers only
    final int[] sortedOdd = Arrays.stream(array).filter(e -> e % 2 == 1).sorted().toArray();
    
    // Then merge them back into original array
    for (int j = 0, s = 0; j < array.length; j++) {
      if (array[j] % 2 == 1) array[j] = sortedOdd[s++];
    }
    
    return array;
  }
  
}
*/