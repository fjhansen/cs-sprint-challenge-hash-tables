def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i, value in enumerate(weights):
        print(f'index_{i}: {value}')
        match = limit - value
        print(f'match: {match}')
        print(f'limit: {0.5 * limit}')
        # checks if match is half of the limit to put it
        if match == 0.5 * limit:
            print('',[i+1,weights.index(match)])
            return [i+1,weights.index(match)]
        # checks if mache is in the cache and puts it in the first index
        if match in cache:
            return [i, weights.index(match)]
        # puts in cache for faster
        else:
            cache[value] = True
    return None
        
    

    #return None

weights_1 = [4,4]
get_indices_of_item_weights(weights_1,2,8)


# So we have a package. it has a weight limit(limit) and a a list of weights
# our goal is to get the indices of the item weights in the list
# get these weights by finding two items whos sum of weight equals the weight limit
# the function will finally return a tuple (zero,one) named Answer

# ----

# I ended up finding the difference between weight limit and value of current weight to find the possible sums of the weight limit
# the cache makes finding matches faster so we can recheck the values as match changes with the iteration
