#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Jessica Woods'


class Node:
    """ Container to store key values in hashtable """

    def __init__(self, key, value=None):
        """ Takes the key required, value which is not """
        self.key = key
        self.hash = hash(self.key)
        self.value = value

    def __repr__(self):
        """ Returns string representation """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """ Dunder method that allows keys values to be compared"""
        return self.key == other.key


class NoDict:
    """ Creates python dictionary, without using python methods """

    def __init__(self, num_buckets=10):
        """ Takes option number of buckets, if not default 10 """
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """ Return a string representing the NoDict contents """
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """ Accepts key and value and creates a new node stores in bucket """
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for kv in bucket:
            if kv == new_node:
                bucket.remove(kv)
                break
        bucket.append(new_node)

    def get(self, key):
        """ Accepts one parametor, if key doesnt exist
        will raise key error """
        key_val = Node(key)
        bucket = self.buckets[key_val.hash % self.size]
        for kv in bucket:
            if kv == key_val:
                return kv.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """ Method that allows you to use square bracket notation
        to look up a value """
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """ Method all you to use square bracket notation
        to set the value of a key """
        self.add(key, value)
