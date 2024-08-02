#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.data)}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "0", str(datetime.now()), {"message": "Genesis Block"})

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class CrimeBlockchain:
    def __init__(self):
        self.blockchain = Blockchain()

    def add_crime(self, crime_id, description, location):
        crime_data = {
            'crime_id': crime_id,
            'description': description,
            'location': location,
            'timestamp': str(datetime.now())
        }
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, str(datetime.now()), crime_data)
        self.blockchain.add_block(new_block)

    def display_chain(self):
        for block in self.blockchain.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print("----------")

def main():
    crime_chain = CrimeBlockchain()

    while True:
        print("1. Record Crime")
        print("2. Display Blockchain")
        print("3. Verify Blockchain")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            crime_id = input("Enter crime ID: ")
            description = input("Enter crime description: ")
            location = input("Enter crime location: ")
            crime_chain.add_crime(crime_id, description, location)
            print("Crime recorded successfully!")

        elif choice == "2":
            crime_chain.display_chain()

        elif choice == "3":
            print("Is blockchain valid?", crime_chain.blockchain.is_chain_valid())

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:


import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.data)}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "0", str(datetime.now()), {"message": "Genesis Block"})

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class CrimeBlockchain:
    def __init__(self):
        self.blockchain = Blockchain()

    def add_crime(self, crime_id, description, location):
        crime_data = {
            'crime_id': crime_id,
            'description': description,
            'location': location,
            'timestamp': str(datetime.now())
        }
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, str(datetime.now()), crime_data)
        self.blockchain.add_block(new_block)

    def display_chain(self):
        for block in self.blockchain.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print("----------")

def main():
    crime_chain = CrimeBlockchain()

    while True:
        print("1. Record Crime")
        print("2. Display Blockchain")
        print("3. Verify Blockchain")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            crime_id = input("Enter crime ID: ")
            description = input("Enter crime description: ")
            location = input("Enter crime location: ")
            crime_chain.add_crime(crime_id, description, location)
            print("Crime recorded successfully!")

        elif choice == "2":
            crime_chain.display_chain()

        elif choice == "3":
            print("Is blockchain valid?", crime_chain.blockchain.is_chain_valid())

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

