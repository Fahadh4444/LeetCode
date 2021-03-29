class Solution:
    def flipMatchVoyage(self, root: TreeNode, V: List[int]) -> List[int]:
        ans = [0]

        def dfs(node, V, ans):
            if not node or ans[0] == -1:
                return
            if node.val != V[ans[0]]:
                ans[0] = -1
            else:
                ans[0] += 1
                if node.left and node.left.val != V[ans[0]]:
                    ans.append(node.val)
                    dfs(node.right, V, ans)
                    dfs(node.left, V, ans)
                else:
                    dfs(node.left, V, ans)
                    dfs(node.right, V, ans)
        dfs(root, V, ans)
        return ans[:1] if ans[0] == -1 else ans[1:]
