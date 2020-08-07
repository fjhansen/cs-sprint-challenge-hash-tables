def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    arr = []

    for x in a:
        #print(x)
        # this checks the cache for the absolute of x
        # if it finds a match it will append the absolute of x to the cache
        if cache.get(abs(x)):
            arr.append(abs(x))
            #print('arr: \n',arr)
        # if the absolute of x does not have a match it is put into the cache
        # it may then be accessed again as we traverse the list
        else:
            cache[abs(x)] = x
            #print('cache: \n',cache)
    return arr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))



# for this we have to figure out which positive numbers have negative number counterparts
# we have to solve this problem with a hash table
# there happens to be an alsolute value function for python so maybe we can use that to our advantage
# absolute value of negative numbers are the positive number counterpart.
# we could loop through all the numbers in the list and check for negative numbers. i will start with that.
# since cache is a dictionary we can use a get method to check for the existing absolute value of x
#
