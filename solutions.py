class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val

         self.next = next
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

    # Number of Islands
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c) -> List[List[str]]:
            if (r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c]=="0"):
                return grid
            grid[r][c] = "0"
            dfs(grid, r, c-1)
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
        
        count = 0
        for i in range (0, len(grid)):
            for j in range (0, len(grid[0])):
                if (grid[i][j] == "1"):
                    count+=1
                    # trigger dfs - return new grid
                    dfs(grid, i, j)
        
    return count
    
    # reverse string O(1) extra space
    def reverseString(self, s: List[str]) -> None:
        """
            Do not return anything, modify s in-place instead.
            """
        for i in range (0, len(s)//2):
            s[i] , s[size-1-i] = s[size-1-i], s[i]
    
    # reverse Linked List
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while (head != None):
            new_head = ListNode(head.val, rev)
            rev = new_head
            head = head.next
        return rev
