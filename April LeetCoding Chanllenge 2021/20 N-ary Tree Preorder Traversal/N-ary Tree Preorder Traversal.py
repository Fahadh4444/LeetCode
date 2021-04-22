class Solution:
    def preorder(self, root: 'Node', ans: list = None) -> List[int]:
        if not root:
            return ans
        if ans == None:
            ans = []
        ans.append(root.val)
        for child in root.children:
            self.preorder(child, ans)
        return ans
