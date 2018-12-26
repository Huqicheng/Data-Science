'''
dependencies:
    npm install Flask
'''
import datetime
import hashlib
import json
from flask import Flask, jsonify

# building a Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [] # containing different blocks
        self.create_block(proof = 1, previous_hash = '0') # first block of the Blockchain
    
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1] # get last block in the chain

    # define a problem: easy to verify, hard to solve
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() # non-symmetric operation
            if hash_operation[:4] == '0000':
                # miner win
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    # hashing encode a block
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index] # current block
            if (self.hash(previous_block) != block['previous_hash']):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest() # non-symmetric operation
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True


# mining the Blockchain

# 1. web app
app = Flask(__name__)

# 2. create a blockchain
blockchain = Blockchain()

# 3. APIs
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'congratulations, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain) 
    }
    return jsonify(response), 200



app.run(host='0.0.0.0', port=5000)