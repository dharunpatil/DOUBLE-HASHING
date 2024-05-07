class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def hash_function2(self, key):
        # A secondary hash function used for double hashing
        # Should be relatively prime to the size of the hash table
        return 7 - (hash(key) % 7)

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.keys[index] is None:
            # If the slot is empty, insert the key and value
            self.keys[index] = key
            self.values[index] = value
        else:
            # Collision occurred, use double hashing
            index2 = self.hash_function2(key)
            while self.keys[index] is not None:
                index = (index + index2) % self.size
            # Found an empty slot, insert the key and value
            self.keys[index] = key
            self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)
        index2 = self.hash_function2(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key found, return the corresponding value
                return self.values[index]
            # Use double hashing to search for the key
            index = (index + index2) % self.size
        # Key not found
        return None

# Example usage
if __name__ == "__main__":
    phone_book = HashTable(10)  # Create a hash table of size 10

    # Inserting clients into the phone book
    phone_book.insert("Alice", "123-456-7890")
    phone_book.insert("Bob", "234-567-8901")
    phone_book.insert("Charlie", "345-678-9012")

    # Looking up telephone numbers
    print(phone_book.get("Alice"))  # Output: 123-456-7890
    print(phone_book.get("Bob"))    # Output: 234-567-8901
    print(phone_book.get("David"))  # Output: None (David is not in the phone book)
