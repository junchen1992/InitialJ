"""
Tags:
    - Trie
    - Recursion
"""
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for ch in key:
            node = node.setdefault(ch, {})
        node['$'] = val
        
    def sum(self, prefix: str) -> int:
        # Find the final node down the trie than corresponds to prefix[-1]
        node = self.trie
        for ch in prefix:
            node = node.get(ch, {})
            if not node:
                return 0
            
        return self.tree_sum(node)
    
    def tree_sum(self, root) -> int:
        if type(root) == int:
            return root
        
        else:
            return sum([self.tree_sum(child) for child in root.values()])


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
