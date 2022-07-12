# User function Template for python3

class Solution:
    def select(self, arr, i):
        # code here
        smallest_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_ind]:
                smallest_ind = j
        return smallest_ind

    def selectionSort(self, arr, n):
        for i in range(n):
            small_num_ind = self.select(arr, i)
            arr[i], arr[small_num_ind] = arr[small_num_ind], arr[i]
