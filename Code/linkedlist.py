#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self): #0(1) is the best case and worst case for every condition for we just check if self.head has a value
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None  

    def length(self): #0(n) is the best and worst case 
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
            Running time will always be 0(n). You have iterate over the 
            whole linked list in how we calculated length."""
        # TODO: Loop through all nodes and count one for each
        #Start at head node 
        node = self.head 
        #start count at 0
        count = 0 
        #loop untill node is None, this is how you traverse through the whole linked list 
        while node is not None: 
            #keep adding 1 untill node is None 
            count += 1 
            #Skip to next node to advance forward in linked list 
            node = node.next
        #now return the count 
        return count 

    def append(self, item): #0(1) is the best and worst case 
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
            Running time will be 0(1) for we can add an item at the 
            tail of a linked list. This is true for every condition."""
        # TODO: Create new node to hold given item
        node = Node(item)

        # TODO: Append node after tail, if it exists
        if self.tail is not None:
            #set tail pointer to new node 
            self.tail.next = node
            #point tail to new node 
            self.tail = node 
        else: 
            self.head = node
            self.tail = node

    def prepend(self, item): #0(1) is the best case and worst case
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
            Running time will be 0(1) for we can add an item at the 
            head of a linked list. This is true for every condition."""
        
        # TODO: Create new node to hold given item
        node = Node(item)
        
        # TODO: Prepend node before head, if it exists
        if self.head is not None: 
            node.next = self.head
            self.head = node
        else:
            self.tail = node 
            self.head = node 

    def find(self, quality): #0(1) is the best case, in which self.head points to what we are trying to find, 0(n) is worst case
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
            Best case is O(1), only when what we are trying to find is the first node.
        
        TODO: Worst case running time: O(???) Why and under what conditions?
            Worst case is 0(n), when the item is not in the list or if the item
            is in the end of list, causing it to take a longer time.        """

        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        while self.head is not None:
            if quality(self.head.data) is True:
                return self.head.data
            else:
                return None

    def delete(self, item): 
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
            Best case is O(1), only when what we are trying to delete is the first node.

        TODO: Worst case running time: O(???) Why and under what conditions?
            Worst case is 0(n), when the item is not in the list or if the item
            is in the end of list, causing it to take a longer time. """

        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))




        

        


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))




if __name__ == '__main__':
    test_linked_list()
