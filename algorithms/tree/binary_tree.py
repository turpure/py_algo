# coding:utf-8


class Node(object):
    """节点类"""
    def __init__(self, ele=-1,  left=None, right=None):
        self.ele = ele
        self.left = left
        self.right = right


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, ele):
        """为树添加节点"""
        node = Node(ele)
        if self.root.ele == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    def front_traverse(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print root.ele,
        self.front_traverse(root.left)
        self.front_traverse(root.right)

    def middle_traverse(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_traverse(root.left)
        print root.ele,
        self.middle_traverse(root.right)

    def later_traverse(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_traverse(root.left)
        self.later_traverse(root.right)
        print root.ele,

    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print node.ele,
                myStack.append(node)
                node = node.left
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right                  #开始查看它的右子树

    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.left
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print node.ele,
            node = node.right                  #开始查看它的右子树

    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print myStack2.pop().ele,

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.ele,
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)


if __name__ == '__main__':
    """主函数"""
    eles = range(10)           #生成十个数据作为树节点
    tree = Tree()          #新建一个树对象
    for ele in eles:
        tree.add(ele)           #逐个添加树的节点

    print '队列实现层次遍历:'
    tree.level_queue(tree.root)

    print '\n\n递归实现先序遍历:'
    tree.front_traverse(tree.root)
    print '\n递归实现中序遍历:'
    tree.middle_traverse(tree.root)
    print '\n递归实现后序遍历:'
    tree.later_traverse(tree.root)

    print '\n\n堆栈实现先序遍历:'
    tree.front_stack(tree.root)
    print '\n堆栈实现中序遍历:'
    tree.middle_stack(tree.root)
    print '\n堆栈实现后序遍历:'
    tree.later_stack(tree.root)