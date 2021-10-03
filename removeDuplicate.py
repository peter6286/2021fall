def removeDuplicates(nums):
    len_ = 1
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]: #因为已经sorted好跟前一个比较就行
            nums[len_] = nums[i]
            len_ += 1
    return len_

a=[2,7,11,15,15] #sorted array
print(removeDuplicates(a))