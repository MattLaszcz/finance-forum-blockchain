

# Initializing our (empty) blockchain list
blockchain = []
open_transactions = []
genesis_block = {
        'previous_hash': 'XYZ', 
        'index': len(blockchain), 
        'transactions': open_transactions
    }
blockchain = [genesis_block]
owner = 'Matt'
participants = {'Max'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participants):
    """Gets the balance and blocks that the sender has sent/ added to the chain and adds them up as well """
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx_sender == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    amount_received = 0
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx_recipient == participant] for block in blockchain]
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(recipient, sender=owner,  amount = 1.0): #optional arguments must come second in the funtion
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    # if last_transaction == None:
    #     last_transaction = [1]
    # blockchain.append([last_transaction, transaction_amount])

    transaction = {'sender': sender, 'recipient':recipient, 'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)

def mine_block():
    #open transactions are taken and added to a block this is a core feature of the blockchain
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    for keys in last_block:
        value = last_block[keys]
        hashed_block = hashed_block + str(value)
    block = {
        'previous_hash': 'XYZ', 
        'index': len(blockchain), 
        'transactions': open_transactions
    }
    blockchain.append(block)

    print(hashed_block)
    return True

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input('Enter the sender of the transaction')
    user_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """ Output all blocks of the blockchain. """
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    for (index, block) in enumerate(blockchain): # enumerate() returns a tuple with the index of the element and the element itself
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True
#     # block_index = 0
#     is_valid = True
#     for block_index in range(len(blockchain)):
#         if block_index == 0:
#             # If we're checking the first block, we should skip the iteration (since there's no previous block)
#             continue
#         # Check the previous block (the entire one) vs the first element of the current block
#         elif blockchain[block_index][0] == blockchain[block_index - 1]:
#             is_valid = True
#         else:
#             is_valid = False
#     #         break
#     # for block in blockchain:
#     #     if block_index == 0:
#     #         block_index += 1
#     #         continue
#     #     elif block[0] == blockchain[block_index - 1]:
#     #         is_valid = True
#     #     else:
#     #         is_valid = False
#     #         break
#     #     block_index += 1
#     return is_valid


waiting_for_input = True

# A while loop for the user input interface
# It's a loop that exits once waiting_for_input becomes False or when break is called
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a New Block')
    print('3: Output the blockchain blocks')
    print('4: Add Participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data #pulls out the data from the tuple from get_transaction_value()
        # Add the transaction amount to the blockchain
        add_transaction(recipient, amount=amount) #values that were extracted from the tuple above
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': 'XYZ', 
                'index': len(blockchain), 
                'transactions': [{'sender': 'Chris', 'recipient': 'Matt', 'amount': 100}]
            }
    elif user_choice == 'q':
        # This will lead to the loop to exist because it's running condition becomes False
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        # Break out of the loop
        break
    print(get_balance('Max'))
else:
    print('User left!')


print('Done!')
