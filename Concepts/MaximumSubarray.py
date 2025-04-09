def maxSubArray(nums):

    # this is kadanes algorithm
    # check for maximum between current and currentMax + curr
    # then check global maxx
    currMax, maxx =0,0
    for curr in nums:
        currMax = max(currMax+ curr, curr)
        maxx = max( maxx, currMax)
    return maxx