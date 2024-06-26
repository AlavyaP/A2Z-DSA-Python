'''
LeetCode :> https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

# Recursive 

def combinationSum2(candidates,target):
    ans = [] 
    dp = []
    candidates.sort()
    
    def find_combi(ind,target):
        
        # This is the condition for no unique combination is found 
        if target == 0 :
            ans.append(dp[:])
            return
        for i in range (ind,len(candidates)):
            if i > ind and candidates[i] == candidates[i-1]:
                continue 
            if candidates[i] > target :
                break
            dp.append(candidates[i])
            find_combi(i+1,target - candidates[i])
            dp.pop()
            
    find_combi(0,target)
    return ans