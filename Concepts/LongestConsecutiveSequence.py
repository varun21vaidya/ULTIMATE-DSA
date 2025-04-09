def longestConsecutiveSequence(nums):
    # nums.sort()
    # currmax,maxx=1,0
    # for curr in range(1,len(nums)):
    #     if nums[curr]-nums[curr-1]==0:
    #         continue
    #     if nums[curr]-nums[curr-1]!=1:
    #         maxx=max(currmax,maxx)
    #         currmax=1
    #     else:
    #         currmax+=1
    # return max(maxx,currmax)

    # hashmap={}
    # hashset=set(nums)
    # currmax, maxx=1,0
    # for curr in hashset:
    #     hashmap[curr]=1
    # for curr in hashset:
    #     if curr-1 in hashmap or hashmap[curr]>1:
    #         continue
    #     else:
    #         tempcurr=curr
    #         while tempcurr+1 in hashmap:
    #             hashmap[curr]+=1
    #             tempcurr+=1
    #         currmax=hashmap[curr]
    #     maxx=max(currmax,maxx)
    # return maxx

    # but we dont need hashmap just use hashset
    hashset=set(nums)
    currMax, maxx=1,0
    for curr in hashset:
        if curr-1 not in hashset:
            tempcurr=curr
            currMax=1
            while tempcurr+1 in hashset:
                currMax+=1
                tempcurr+=1
        maxx=max(currMax,maxx)
    return maxx

nums=[100,4,200,1,3,2]
# nums=[0,3,7,2,5,8,4,6,0,1]
# nums=[1,0,1,2]
# nums=[]
print(longestConsecutiveSequence(nums))