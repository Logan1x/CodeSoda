class Solution:
    def findMin(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        curr_min = arr[0]

        while(l <=r):

            m = (l + r)//2


            # print(arr[l],arr[r],arr[m])

            curr_min = min(curr_min, arr[m])

            if(arr[m]>arr[r]):
                l = m +1
            else:
                r = m -1

        return curr_min
        