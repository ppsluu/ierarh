from typing import Dict, List, Optional, Any
from collections import deque


class TreeNode:
    def __init__(self, v: Any, ch: Optional[List['TreeNode']] = None):
        self.v = v
        self.ch = ch if ch is not None else []
    
    def to_dict(self) -> Dict:
        return {'v': self.v, 'ch': [c.to_dict() for c in self.ch]}
    
    @classmethod
    def from_dict(cls, d: Dict) -> 'TreeNode':
        n = cls(d['v'])
        n.ch = [cls.from_dict(c) for c in d.get('ch', [])]
        return n
    
    def __repr__(self):
        return f"TN({self.v})"


class BinaryTreeNode:
    def __init__(self, v: Any, l: Optional['BinaryTreeNode'] = None, r: Optional['BinaryTreeNode'] = None):
        self.v = v
        self.l = l
        self.r = r
    
    def to_dict(self) -> Dict:
        res = {'v': self.v}
        if self.l: res['l'] = self.l.to_dict()
        if self.r: res['r'] = self.r.to_dict()
        return res
    
    @classmethod
    def from_dict(cls, d: Dict) -> 'BinaryTreeNode':
        n = cls(d['v'])
        if 'l' in d: n.l = cls.from_dict(d['l'])
        if 'r' in d: n.r = cls.from_dict(d['r'])
        return n
    
    def __repr__(self):
        return f"BTN({self.v})"


class Tree:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root
    
    def add_child(self, pv: Any, cv: Any) -> bool:
        if not self.root:
            self.root = TreeNode(pv)
            return True
        p = self._find(self.root, pv)
        if not p: return False
        p.ch.append(TreeNode(cv))
        return True
    
    def _find(self, n: TreeNode, v: Any) -> Optional[TreeNode]:
        if n.v == v: return n
        for c in n.ch:
            r = self._find(c, v)
            if r: return r
        return None
    
    def to_dict(self) -> Optional[Dict]:
        return self.root.to_dict() if self.root else None
    
    @classmethod
    def from_dict(cls, d: Optional[Dict]) -> 'Tree':
        return cls(TreeNode.from_dict(d)) if d else cls()
    
    def print_tree(self, n: Optional[TreeNode] = None, lvl: int = 0, pfx: str = ""):
        n = n or self.root
        if not n:
            print("пусто")
            return
        print(f"{pfx}{'└── ' if lvl > 0 else ''}{n.v}")
        for i, c in enumerate(n.ch):
            last = i == len(n.ch) - 1
            npfx = pfx + ("    " if lvl > 0 else "")
            self.print_tree(c, lvl + 1, npfx + ("    " if last else "│   "))


class BinaryTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None):
        self.root = root
    
    def insert(self, v: Any, pv: Optional[Any] = None, pos: str = 'l') -> bool:
        nn = BinaryTreeNode(v)
        if not self.root:
            self.root = nn
            return True
        if not pv:
            return self._ins_first(self.root, nn)
        p = self._find(self.root, pv)
        if not p: return False
        if pos == 'l' and not p.l:
            p.l = nn
            return True
        if pos == 'r' and not p.r:
            p.r = nn
            return True
        return False
    
    def _ins_first(self, n: BinaryTreeNode, nn: BinaryTreeNode) -> bool:
        q = deque([n])
        while q:
            cur = q.popleft()
            if not cur.l:
                cur.l = nn
                return True
            if not cur.r:
                cur.r = nn
                return True
            if cur.l: q.append(cur.l)
            if cur.r: q.append(cur.r)
        return False
    
    def _find(self, n: Optional[BinaryTreeNode], v: Any) -> Optional[BinaryTreeNode]:
        if not n: return None
        if n.v == v: return n
        r = self._find(n.l, v)
        return r if r else self._find(n.r, v)
    
    def to_dict(self) -> Optional[Dict]:
        return self.root.to_dict() if self.root else None
    
    @classmethod
    def from_dict(cls, d: Optional[Dict]) -> 'BinaryTree':
        return cls(BinaryTreeNode.from_dict(d)) if d else cls()
    
    def print_tree(self, n: Optional[BinaryTreeNode] = None, lvl: int = 0, pfx: str = ""):
        n = n or self.root
        if not n:
            print("пусто")
            return
        print(f"{pfx}{'└── ' if lvl > 0 else ''}{n.v}")
        ch = []
        if n.l: ch.append(n.l)
        if n.r: ch.append(n.r)
        for i, c in enumerate(ch):
            last = i == len(ch) - 1
            npfx = pfx + ("    " if lvl > 0 else "")
            self.print_tree(c, lvl + 1, npfx + ("    " if last else "│   "))


class TreeConverter:
    @staticmethod
    def tree_to_binary_tree(t: Tree) -> BinaryTree:
        if not t.root: return BinaryTree()
        
        def conv(n: TreeNode) -> Optional[BinaryTreeNode]:
            if not n: return None
            bn = BinaryTreeNode(n.v)
            if len(n.ch) > 0:
                bn.l = conv(n.ch[0])
            if len(n.ch) > 1:
                cur = bn.l
                for i in range(1, len(n.ch)):
                    if not cur:
                        cur = conv(n.ch[i])
                        bn.l = cur
                    else:
                        cur.r = conv(n.ch[i])
                        cur = cur.r
            return bn
        
        return BinaryTree(conv(t.root))
    
    @staticmethod
    def binary_tree_to_tree(bt: BinaryTree) -> Tree:
        if not bt.root: return Tree()
        
        def conv(bn: Optional[BinaryTreeNode]) -> Optional[TreeNode]:
            if not bn: return None
            tn = TreeNode(bn.v)
            ch = []
            if bn.l: ch.append(conv(bn.l))
            if bn.r: ch.append(conv(bn.r))
            tn.ch = [c for c in ch if c]
            return tn
        
        return Tree(conv(bt.root))
    
    @staticmethod
    def tree_to_dict(t: Tree) -> Optional[Dict]:
        return t.to_dict()
    
    @staticmethod
    def binary_tree_to_dict(bt: BinaryTree) -> Optional[Dict]:
        return bt.to_dict()


if __name__ == "__main__":

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

    print("КОНВЕРТАЦИЯ ОБРАТНО")
    t2 = c.binary_tree_to_tree(bt)
    
    print("\nОбщее дерево:")
    t2.print_tree()

    print("СЛОВАРИ")
    import json
    td = c.tree_to_dict(t)
    print("\nОбщее дерево:")
    print(json.dumps(td, indent=2, ensure_ascii=False))
    btd = c.binary_tree_to_dict(bt)
    print("\nБинарное дерево:")
    print(json.dumps(btd, indent=2, ensure_ascii=False))
