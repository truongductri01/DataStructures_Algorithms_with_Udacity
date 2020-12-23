'''
Hash function
Value -------------> Hash value
      Hash function
Hash value will become an array index
And accessing array's element using index consume constant time


Collisions:
When two value be transformed into the same hash value create the collision
=> Solution:
    1. Change the hash function to create different hash values
    2. Change the structure of the storage -> maybe store the values with same hash values into a list under the same index

Time Complexity:
1. If changing the hash function every time collision appears,
    the needs of storing all data into new arrays will create more complexity in time and space
2. If storing the same values into a list under the same hash value,
    the best case will be O(1) - constant time
    and the worst case will be O(n) - when all element is stored in the same list
3. Create space for every different values will consume more space than (2) options

Normal array: each element is value
Bucket: each element is a list


Load factor: how full a hash Table is
Load factor = Number of entries / Number of buckets

If we store 10 values only into a 100 buckets space then the load factor is only 0.1 and we waste a lot of space.
The closer the Load factor approaches 0, the more likely we need to rehash - come up with new hash function

Hash maps:
    Input values are items in the maps (<key, value> item) => hash values are (<hash key, value>)
'''

if __name__ == '__main__':
    print()

