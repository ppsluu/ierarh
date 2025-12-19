from hierarchical_structures import Tree, BinaryTree, TreeNode, BinaryTreeNode, TreeConverter
import json

def main():
    print("СОЗДАНИЕ ОБЩЕГО ДЕРЕВА")

    
    t = Tree()
    t.root = TreeNode("A")
    t.root.ch = [TreeNode("B"), TreeNode("C"), TreeNode("D")]
    t.root.ch[0].ch = [TreeNode("E"), TreeNode("F")]
    t.root.ch[1].ch = [TreeNode("G")]
    t.root.ch[2].ch = [TreeNode("H"), TreeNode("I"), TreeNode("J")]
    
    print("\nОбщее дерево:")
    t.print_tree()
    

    print("КОНВЕРТАЦИЯ В БИНАРНОЕ ДЕРЕВО")

    
    c = TreeConverter()
    bt = c.tree_to_binary_tree(t)
    
    print("\nБинарное дерево:")
    bt.print_tree()
    
    print("\n" + "=" * 60)
    print("КОНВЕРТАЦИЯ ОБРАТНО")
    print("=" * 60)
    
    t2 = c.binary_tree_to_tree(bt)
    
    print("\nОбщее дерево:")
    t2.print_tree()
    
    print("\n" + "=" * 60)
    print("СЛОВАРИ")
    print("=" * 60)
    
    print("\nОбщее дерево:")
    td = c.tree_to_dict(t)
    print(json.dumps(td, indent=2, ensure_ascii=False))
    
    print("\nБинарное дерево:")
    btd = c.binary_tree_to_dict(bt)
    print(json.dumps(btd, indent=2, ensure_ascii=False))
    

    print("ДОП ПРИМЕР")

    
    bt2 = BinaryTree()
    bt2.root = BinaryTreeNode(1)
    bt2.root.l = BinaryTreeNode(2)
    bt2.root.r = BinaryTreeNode(3)
    bt2.root.l.l = BinaryTreeNode(4)
    bt2.root.l.r = BinaryTreeNode(5)
    bt2.root.r.l = BinaryTreeNode(6)
    
    print("\nБинарное дерево:")
    bt2.print_tree()
    
    print("\nВ общее:")
    t3 = c.binary_tree_to_tree(bt2)
    t3.print_tree()

if __name__ == "__main__":
    main()
