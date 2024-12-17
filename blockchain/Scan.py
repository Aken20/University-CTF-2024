from web3 import Web3

RPC_URL = "http://94.237.59.180:57177"

def investigate_blocks():
    # Connect to the network
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    
    try:
        # Ensure connection is successful
        if not w3.is_connected():
            print("Failed to connect to Ethereum network")
            return None
        # Get the block details
        for i in range(0, 90):
            block = w3.eth.get_block(i)
            
            print("Block ",i," Details:")
            print(f"Block Number: {block.number}")
            print(f"Block Hash: {block.hash.hex()}")
            print(f"Parent Hash: {block.parentHash.hex()}")
            print(f"Timestamp: {block.timestamp}")
            
            # Check transactions in the block
            if block.transactions:
                print("\nTransactions in Block ",i,":")
                for tx_hash in block.transactions:
                    tx = w3.eth.get_transaction(tx_hash)
                    print(f"Transaction Hash: {tx_hash.hex()}")
                    print(f"From: {tx['from']}")
                    print(f"To: {tx['to']}")
                    print(f"Input Data: {tx['input']}")
                    print("---")
            else:
                print("\nNo transactions in Block ", i)
            
    except Exception as e:
        print(f"Error investigating Block ",i, e)

investigate_blocks()
