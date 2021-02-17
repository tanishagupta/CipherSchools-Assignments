// Initially, wasn't able to understand the logic so took help and understood it.

#include<iostream>
#include<climits>
using namespace std;
 
int MaximumSum(int arr[],int n)
{
    int max_so_far = INT_MIN;
	int max_till_here = 0;
 
    for (int i = 0; i < n; i++)
    {
        max_till_here += arr[i];
        if (max_so_far < max_till_here)
        {
        	max_so_far = max_till_here;	
		}
 
        if (max_till_here < 0)
        {
        	max_till_here = 0;	
		}
    }
    return max_so_far;
}
 
int main()
{
    int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
    int n = sizeof(arr)/sizeof(arr[0]);
    int sum = MaximumSum(arr, n);
    cout << "Maximum sum for contiguous sub-array is " << sum;
    return 0;
}
