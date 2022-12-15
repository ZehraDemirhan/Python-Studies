class BinaryTree:
    def __init__(self,root):
        self.key = root;
        self.right = None;
        self.left = None;

    def get_left_child(self):
        return self.left;
    
    def get_right_child(self):
        return self.right;

    def get_root(self):
        return self.key;

    def set_root(self,obj):
        self.key = obj;

    def insertNode(self, newNode):
        if self.get_root() == None:
            self.set_root(newNode)

        else:
            if self.get_root() > newNode:
                if self.get_left_child() == None:
                    self.left = BinaryTree(newNode)
                    print("left child", self.get_left_child())

                else:
                    self.get_left_child().insertNode(newNode)
                    print("Left tree", self.get_left_child)

            else:
                if self.get_right_child() == None:
                    self.right = BinaryTree(newNode)
                    print("right child", self.get_right_child())

                else:
                    self.get_right_child().insertNode(newNode)
                    print("right tree", self.get_right_child())


    def preorder(self):
        print(self.key)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
           
            if self.left is not None:
                self.left.inorder()
            print(self.key)
            if self.right is not None:
                self.right.inorder()

    def postorder(self):
           
            if self.left is not None:
                self.left.postorder()
        
            if self.right is not None:
                self.right.postorder()

            print(self.key)

#main

print("Enter 10 number to create tree:")

r = BinaryTree(None)

for i in range(1,11):
    num = int(input("Enter a number:"))
    r.insertNode(num)   

print("PreOrder")
r.preorder()

print("inorder")
r.inorder()

print("postorder")
r.postorder()
