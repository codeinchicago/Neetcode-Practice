"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
"""


#https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/#howtosortdatawiththesortedmethod
#Help with sorting the dictionary came from that link.

nums = [1,1,1,2,2,3,4,4,4,4,4]
k = 2

#Get the counts
counts = {}
for i in nums:
    if i in counts:
        counts[i] +=1
    if i not in counts:
        counts[i] = 1

#print(counts)

#Once numbers are counted, get the k largest.

#Need to sort the results
counts_sort = sorted(counts.items(), key = lambda x:x[1], reverse=True)
# print(counts_sort)
# print(counts_sort[0])
#List is fine, easier to manipulate.
#Can turn it back into a dictionary using the dict function.

counted = sorted(counts.items())
# print("Here is counted.")
# print(counted)

#Results are now sorted in descending value, just need to get the first k results.
answer = []
for i in range(k):
    answer.append(counts_sort[i][0])
print(answer)    

# footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
# print(sorted_footballers_by_goals)
# converted_dict = dict(sorted_footballers_by_goals)
# print(converted_dict)