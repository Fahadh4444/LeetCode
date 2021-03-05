class Solution:
    def createTreeDict(self, treeDict, i, node):
        if node:
            if i in treeDict:
                treeDict[i] = treeDict[i] + [node.val]
            else:
                treeDict[i] = [node.val]
            return self.createTreeDict(treeDict, i+1, node.left), self.createTreeDict(treeDict, i+1, node.right)
        else:
            return

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = list()
        treeDict = dict()
        self.createTreeDict(treeDict, 0, root)
        for l in range(len(treeDict)):
            result = result + [sum(treeDict[l]) / float(len(treeDict[l]))]
        return result
