from .block import Block

class File:
    def __init__(self, name, size, block_size, blocks_pool):
        self.name = name
        self.size = size
        self.blocks = self.allocate_blocks(size, block_size, blocks_pool)

    def allocate_blocks(self, size, block_size, blocks_pool):
        num_blocks_needed = -(-size // block_size)
        allocated_blocks = []

        for _ in range(num_blocks_needed):
            if blocks_pool:
                block = blocks_pool.pop(0)
                allocated_blocks.append(block)
                if len(allocated_blocks) > 1:
                    allocated_blocks[-2].next_block = block

        return allocated_blocks

    def __str__(self):
        blocks_info = ", ".join(f"Block(ID: {b.block_id})" for b in self.blocks)
        return f"File(Name: {self.name}, Size: {self.size}, Blocks: [{blocks_info}])"
