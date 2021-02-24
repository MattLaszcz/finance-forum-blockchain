blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction = [1]): 
    blockchain.append([last_transaction, transaction_amount])
    

add_value(4)
add_value(last_transaction=get_last_blockchain_value(),transaction_amount=.8
)
add_value(6,get_last_blockchain_value())

print(blockchain)