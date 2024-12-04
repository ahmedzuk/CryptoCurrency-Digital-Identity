import hashlib
from datetime import datetime

class Block:
    def __init__(self, coin_identifier, blockchain_of_origin, timestamp, status, order_number):
        self.validate_coin_identifier(coin_identifier)
        self.validate_blockchain_of_origin(blockchain_of_origin)
        self.validate_timestamp(timestamp)
        self.validate_status(status)
        self.validate_order_number(order_number)

        self.coin_identifier = coin_identifier
        self.blockchain_of_origin = blockchain_of_origin
        self.timestamp = timestamp
        self.status = status
        self.order_number = order_number
        self.hash = self.calculate_hash()

    def validate_coin_identifier(self, coin_identifier):
        if not self.is_valid_identifier(coin_identifier):
            raise ValueError("Invalid coin identifier")

    def validate_blockchain_of_origin(self, blockchain_of_origin):
        if not blockchain_of_origin.isalpha():
            raise ValueError("Blockchain of origin must be a string of letters")

    def validate_timestamp(self, timestamp):
        try:
            datetime.strptime(timestamp, "%H:%M:%S, %d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid timestamp format. Use HH:MM:SS, DD/MM/YYYY")

    def validate_status(self, status):
        if status not in ['a', 'b', 'f']:  # Add more statuses if needed
            raise ValueError("Invalid status. Use 'a' for active, 'b' for burned, 'f' for frozen")

    def validate_order_number(self, order_number):
        if not isinstance(order_number, int) or order_number <= 0:
            raise ValueError("Order number must be a positive integer")

    def is_valid_identifier(self, identifier):
        """
        Validates the coin identifier format.
        The identifier must be 20 characters long and start with 'to'.
        """
        return len(identifier) == 20 and identifier[0:2] == 'to'

    def calculate_hash(self):
        """
        Create a SHA-256 hash of the block content.
        """
        block_string = f"{self.coin_identifier}{self.blockchain_of_origin}{self.timestamp}{self.status}{self.order_number}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block({self.coin_identifier}, {self.blockchain_of_origin}, {self.timestamp}, {self.status}, {self.order_number}, {self.hash})"

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block)

    def get_blocks(self):
        return self.chain

# Example usage
blockchain = Blockchain()

try:
    # Adding blocks
    block1 = Block(
        coin_identifier="tonxton134232161224066a",  # Example identifier: 'to' + blockchain + timestamp + order number + status
        blockchain_of_origin="ton",
        timestamp="13:42:32, 16/16/2024",
        status="a",
        order_number=66
    )

    blockchain.add_block(block1)

    # Add another block
    block2 = Block(
        coin_identifier="ethxeth154532161224099b",  # Example identifier: 'to' + blockchain + timestamp + order number + status
        blockchain_of_origin="eth",
        timestamp="15:45:32, 16/16/2024",
        status="b",
        order_number=99
 )

    blockchain.add_block(block2)

    # Print blocks
    for block in blockchain.get_blocks():
        print(block)

except ValueError as e:
    print(f"Error: {e}")
