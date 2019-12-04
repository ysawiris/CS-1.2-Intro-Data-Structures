#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Both cases are O(b(n/b)) for you have to go through each bucket and add each key 
        #in the linkedlist. 
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Both cases are O(b(n/b)) for you have to go through each bucket and add each value
        #in the linkedlist. 
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)

        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # The running time for both cases is O(n), for you have to traverse 
        # through each bucket and get all the nodes.
        
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Running time will be O(n) for both best and worst case. We have to 
        # go through each bucket and count how many nodes are in each linkedlist 

        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        
        
        count = 0 

        for bucket in self.buckets:
            for key, value in bucket.items():
                count += 1 

        return count 

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Best case is O(1) this happens when your only have 1 node in your linkedlist 
        #Average case is O(n/b) this happens when you have multiple nodes in your linkedlist 
        #and you have to traverse each node to see if the keys match 
        
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        specific_bucket = self.buckets[self._bucket_index(key)]

        specific_node = specific_bucket.find(lambda item: item[0] == key)

        return specific_node is not None 
        

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Best case is O(1) this happens when your only have 1 node in your linkedlist 
        #Average case is O(n/b) this happens when you have multiple nodes in your linkedlist 
        #and you have to traverse each node to see if the keys matches then return the value
        
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        #get the linked-list in the bucket 
        #_bucket_index returns the bucket index where the key would be stored 
        specific_bucket = self.buckets[self._bucket_index(key)]

        #traverse through the linked-list
        #check each node if it is equal to the key we are looking for 
        #else raise KeyError
        specific_node = specific_bucket.find(lambda item: item[0] == key)

        if specific_node is not None:
            return specific_node[1]
        raise KeyError('Key not found: {}'.format(key))
            

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Best case is O(1) this happens when your only have 1 node in your linkedlist 
        #Average case is O(n/b) this happens when you have multiple nodes in your linkedlist 
        #and you have to traverse each node to see if the key exists, update its value if it does
        #or just add new node to the linkedlist 

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        specific_bucket = self.buckets[self._bucket_index(key)]

        specific_node = specific_bucket.find(lambda item: item[0] == key)
        
        if specific_node is not None:
            specific_bucket.replace(specific_node, (key, value))
            return None
    
        specific_bucket.append((key,value))



    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Best case is O(1) this happens when your only have 1 node in your linkedlist 
        #Average case is O(n/b) this happens when you have multiple nodes in your linkedlist 
        #and you have to traverse each node to see if the keys match then delete
        
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        
        #get the linked-list in the bucket 
        #_bucket_index returns the bucket index where the key would be stored 
        specific_bucket = self.buckets[self._bucket_index(key)]

        specific_node = specific_bucket.find(lambda item: item[0] == key)

        #traverse through the linked-list
        #check each node if it is equal to the key we are looking for then delete
        #else raise KeyError
        if specific_node is not None:
                specific_bucket.delete(specific_node)
                return None
        raise KeyError('Key not found: {}'.format(key))

        


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
