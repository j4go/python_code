# coding: utf-8
# 二叉树的实现与遍历


class Node:
    """节点 树由N个节点组成"""
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def append_node(tree, node):
    """将节点node添加到一棵树上 用于生成树时调用。

    构建策略是：值越大越是在右下角，越小越在左下角   策略1
    """
    if node.data < tree.data:
        if tree.left_child:
            append_node(tree.left_child, node)
        else:
            tree.left_child = node
    else:
        if tree.right_child:
            append_node(tree.right_child, node)
        else:
            tree.right_child = node


def build_tree(sequence):
    """利用序列生成一棵树 策略1"""
    # 初始化树
    tree = Node(sequence[0])
    for i in sequence[1:]:
        append_node(tree, Node(i))
    return tree


def preorder_traversal(tree):
    """递归实现 先序遍历"""
    if tree:
        print(tree.data)
        preorder_traversal(tree.left_child)
        preorder_traversal(tree.right_child)


def inorder_traversal(tree):
    """递归实现 中序遍历"""
    if tree:
        inorder_traversal(tree.left_child)
        print(tree.data)
        inorder_traversal(tree.right_child)


def postorder_traversal(tree):
    """递归实现 后序遍历"""
    if tree:
        postorder_traversal(tree.left_child)
        postorder_traversal(tree.right_child)
        print(tree.data)


def level_traversal(tree, length):
    """递归实现 层次遍历 广度优先

    可以优化成一个参数 去掉第二个长度参数
    """
    q = [tree]  # 用列表模拟先进先出的队列
    # length = len(tree) # tree并没实现 __len__
    # 遍历一次就打印一个节点上的值，共遍历length次
    for i in range(length):
        print(q[i].data)
        # 将当前节点的左右子节点分别入队 如此实现广度优先
        if q[i].left_child:
            q.append(q[i].left_child)
        if q[i].right_child:
            q.append(q[i].right_child)


def reconstruct_tree(preorder, inorder):
    """已知先序遍历和中序遍历 重建二叉树 用递归实现"""
    if not preorder or not inorder:
        return None
    data = preorder[0]
    i = inorder.index(data)
    left_child = reconstruct_tree(preorder[1:i+1], inorder[:i])
    right_child = reconstruct_tree(preorder[i+1:], inorder[i+1:])
    return Node(data, left_child, right_child)


if __name__ == '__main__':
    # 序列构建树  策略1
    sequence = [3, 4, 2, 6, 7, 1, 8, 5]
    tree1 = build_tree(sequence)

    print('tree1先序遍历如下：')
    preorder_traversal(tree1)
    print('tree1中序遍历如下：')
    inorder_traversal(tree1)
    print('tree1后序遍历如下：')
    postorder_traversal(tree1)
    print('tree1层次遍历如下：')
    level_traversal(tree1, len(sequence))

    # 直接Node节点构建树 策略2
    tree2 = Node(3, Node(2, Node(1)), Node(4, right_child=Node(6, Node(5),
        Node(7, right_child=Node(8))))) # flake8: noqa

    print('tree2先序遍历如下：')
    preorder_traversal(tree2)
    print('tree2中序遍历如下：')
    inorder_traversal(tree2)
    print('tree2后序遍历如下：')
    postorder_traversal(tree2)
    print('tree2层次遍历如下：')
    level_traversal(tree2, len(sequence))

    # 已知先序遍历和中序遍历 重建二叉树
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    tree3 = reconstruct_tree(preorder, inorder)
    print('tree3先序遍历如下：')
    preorder_traversal(tree3)
    print('tree3中序遍历如下：')
    inorder_traversal(tree3)
    print('tree3后序遍历如下：')
    postorder_traversal(tree3)
    print('tree3层次遍历如下：')
    level_traversal(tree3, len(preorder))
