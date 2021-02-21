class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, n in enumerate(nums):
            if target-n in dict:
                return(i,dict[target-n])
            else:
                dict[n]=i

    def findTarget(self, root: TreeNode, k: int) -> bool:
        diff_set = set()
        return Solution.treeSearch(root,diff_set,k)

    def treeSearch(node, diff_set,k):
        current_set = diff_set
        if node == None:
            return False
        elif node.val in current_set:
            return True
        else:
            current_set.add(k-node.val)
            return Solution.treeSearch(node.right, current_set,k) or Solution.treeSearch(node.left, current_set,k)
