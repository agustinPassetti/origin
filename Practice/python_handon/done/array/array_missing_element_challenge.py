# Consider an array of non-negative integers.\n",
# A second array is formed by shuffling the elements of the first array and deleting a random element. \n",
# Given these two arrays, find which element is missing in the second array.\n",
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.\n",
# Input:\n",
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])\n",
# Output:\n",
# 5 is the missing number"

org = [1,2,3,4,5,6,7]

sub = [3,7,2,1,4,6]

def finder (original, subarray) :

    missing_elem = sum(original) - sum (subarray)
    print ( "missing element is " + str(missing_elem))
    return missing_elem
    
finder( org, sub)