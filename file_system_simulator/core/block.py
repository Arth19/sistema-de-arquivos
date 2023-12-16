class Block:
    def __init__(self, block_size, block_id):
        self.block_size = block_size
        self.block_id = block_id
        self.next_block = None
