import hashlib
from datetime import datetime
from time import sleep

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        
        hash_index = str(self.index).encode('utf-8')
        hash_data = str(self.data).encode('utf-8')
        hash_timestamp = str(self.timestamp).encode('utf-8')
        hash_previous_hash = str(self.previous_hash).encode('utf-8')
    
        sha.update(hash_index)
        sha.update(hash_timestamp)
        sha.update(hash_data)
        sha.update(hash_previous_hash)

        return sha.hexdigest()
    
    def get_timestamp(self):
        return self.timestamp
    
    def get_hash(self):
        return self.hash
    
    def get_index(self):
        return self.index
    
    def get_previous_hash(self):
        return self.previous_hash

class BlockChain:
    def __init__(self):
        #Date: 1/13/2022, https://towardsdatascience.com/building-a-minimal-blockchain-in-python-4f2e9934101d
        self.block_list = []
        self.block_list.append(
            Block(
                0, 
                datetime.utcnow(), 
                'genesis_block', 
                0
            )
        ) #append the genesis block
    
    def add_block(self, data):
        #Date: 1/13/2022, https://towardsdatascience.com/building-a-minimal-blockchain-in-python-4f2e9934101d
        self.block_list.append(Block(
            len(self.block_list),
            datetime.utcnow(),
            data,
            self.block_list[len(self.block_list) - 1].get_hash()
        ))
    
    def is_valid_blockchain(self):
        #Date: 1/13/2022, https://towardsdatascience.com/building-a-minimal-blockchain-in-python-4f2e9934101d
        for i in range(1, len(self.block_list)): #dont verify genesis block
            current_block = self.block_list[i]
            if current_block.index != i:
                print('Block Index mismatch found')
                return False
            if current_block.get_hash() != current_block.calc_hash():
                print('Hash mismatch found')
                return False
            if i > 1 and self.block_list[i - 1].get_hash() != current_block.get_previous_hash():
                print('Previous Hash mismatch found')
                return False
            if i > 1 and self.block_list[i - 1].get_timestamp() >= current_block.get_timestamp():
                print('Previous blocks timestamp is greater than newer block')
                return False
        return True

    def get_block_chain(self):
        blocks_to_print = []
        if self.is_valid_blockchain():
            for i in range(1, len(self.block_list)):
                blocks_to_print.append((self.block_list[i].get_hash(), self.block_list[i].get_timestamp()))
        else:
            print('Blockchain is invalid')
            return 
        return blocks_to_print
    
    def print_block_chain(self):
        print(self.get_block_chain())

# Test One - Happy Path
print('Test One - Happy Path')
block_chain = BlockChain()
block_chain.add_block(1231231231)
sleep(5)
block_chain.add_block([1,2,3,4,5,6])
block_chain.print_block_chain()
# ----- Should print -----
# [('bcede5eb1d31dc76b8ad303898dd712210eee4b331e57419171752c012f9a65b', datetime.datetime(2022, 1, 14, 1, 42, 56, 19552)), 
#  ('6c8bf8499efa7a3936bd6dbfceab0a939cd059b5e75d41826a3434bcd5f2392d', datetime.datetime(2022, 1, 14, 1, 43, 1, 25090))]

print('\nTest Two - Invalid Blockchain')
# Test Two - Invalid Blockchain
sleep(5)
block_chain.add_block('Hello World')
block_chain.block_list[1].data = [2,3,45,6]
block_chain.block_list[1].calc_hash()
block_chain.print_block_chain()
# ----- Should print -----
# Hash mismatch found
# Blockchain is invalid
# None

print('\nTest Three - None Data for Block Data')
block_chain_null = BlockChain()
block_chain_null.add_block(None)
sleep(5)
block_chain_null.add_block(None)
sleep(5)
block_chain_null.add_block(None)
block_chain_null.print_block_chain()
# ----- Should print -----
# [('c4597e840ba40a3a494ffc4aedac1366891f2e5a23039b356433506260b0f368', datetime.datetime(2022, 1, 14, 1, 49, 0, 599972)), 
#  ('3dca8b42b555a68d6a8cb52881573af59196a111695a54bbf3424ea5a2075879', datetime.datetime(2022, 1, 14, 1, 49, 5, 610930)), 
#  ('b9afe26206cd7a04cad7ffa312108643baf70788f5ebb45661655c1c276b71f3', datetime.datetime(2022, 1, 14, 1, 49, 10, 615689))]

print('\nTest Four - Nest Blockchain')
block_chain_nested_0 = BlockChain()
block_chain_nested_0.add_block(0)
block_chain_nested_1 = BlockChain()
block_chain_nested_1.add_block(block_chain_nested_0)
block_chain_nested_2 = BlockChain()
block_chain_nested_2.add_block(block_chain_nested_1)
block_chain_nested_2.print_block_chain()
# ----- Should print -----
# [('e5d4cf7893fe91528f63f7adc8301c4ccb1f8ef22dfabedc23a39526a3ca434b', datetime.datetime(2022, 1, 14, 1, 53, 21, 535390))]
