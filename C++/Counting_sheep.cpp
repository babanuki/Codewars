using namespace std; 

int count_sheep(vector<bool> arr) 
{
  int ans=0;
  for(const auto& i : arr)
    if(i==true) ans++;
  return ans;
}




/*
#include <algorithm>
#include <vector>

int count_sheep(std::vector<bool> v) {
  return std::count(v.cbegin(), v.cend(), true);
}
*/