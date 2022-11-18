class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr)-1

        while(l<=r):
            m = (l + r)//2

            if(target == arr[m]):
                return m


            elif(arr[l]<=arr[m]):
                # left sorted arr
                if(arr[l]<=target<=arr[m]):
                    r = m-1
                else:
                    l = m+1


            else:
                #right sorted arr
                if(arr[m]<=target<=arr[r]):
                    l = m+1
                else:
                    r = m-1
        return -1
        