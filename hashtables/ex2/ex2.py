#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
       return '{}({!r}, {!r})'.format(
           self.__class__.__name__,
           self.source, self.destination)
        


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # make enough buckets for all routes
    buckets = [None] * length

    cache = {}

    print(f'buckets: {buckets} \n cache: {cache} \n')

    

    for t in tickets:
        print(f'source: {t.source} \n dest: {t.destination} \n')
        # source becomes key destination becomes value. 
        cache[t.source] = t.destination
        print(cache)

        # if an ending ticket has a destination of none it must mean a starting ticket starts with none.
        # find this to start the chain

    next_dest = cache['NONE']
    print('next:',next_dest)

        # look for current tickets next destination and add to bucket
        # stop looking when next is NONE because the last destination be NONE

    for curr in range(0, length):
        buckets[curr] = next_dest
        print("buckets and next:",buckets, next_dest)

        next_dest = cache[next_dest]
        print("buckets and next:",cache, next_dest)

            
         

    return buckets


# so basically we need to find out how to determine which source links to the next source
# once we figure out what source links to the next we have to sort them based on an order that makes sense

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

##expected output = ["PDX", "DCA", "NONE"]
##result = reconstruct_trip(tickets, 3)

reconstruct_trip(tickets, 3)
