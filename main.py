from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER 
    pair = [0,0]
    for i in range(0,len(List)-1):
        j = i+1
        if(List[i] + List[j] == target):
            pair[0] = i
            pair[1] = j
    return pair
