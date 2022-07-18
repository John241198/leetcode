nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

#initial solution
while 0 in nums1:
    nums1.remove(0)
    if len(nums1) == m and len(nums2) == n:
        for i in nums2:
            nums1.append(i)

nums1.sort()
print(nums1)


#improved solution
result = 0
while n > 0:
    nums1[m] = nums2[result]
    m+=1
    n-=1
    result +=1
nums1.sort()
print(nums1)
