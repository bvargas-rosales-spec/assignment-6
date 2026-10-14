class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        is_top_level = current_node is None

        if is_top_level:
            current_node = self.root
            if current_node is None:
                print("Error: The tree is empty. Set a root before inserting employees.")
                return False

        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                else:
                    print(f"Error:{manager_name}'s left side is already taken by {current_node.left}.")
            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                else:
                    print(f"Error:{manager_name}'s right side is already taken by {current_node.right}.")
            else:
                print(f"Error: '{side}' is not a valid side. Use 'left' or 'right'.")
            return True
        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True
        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True
        
        if is_top_level:
            print(f"Error: Manager '{manager_name}' not found in the tree.")
        return False
    
    def print_tree(self, node=None, level=0):
        if node is None and level == 0:
            node = self.root

        if  node is None:
            return

        print(" " * level + "- " + node.name)

        level += 1 
        self.print_tree(node.left, level)
        self.print_tree(node.right, level)



# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    company_directory()



#Recursive insertion worked by treating every employee as the root of a subtree. When insert is called without a node, it starts at the team lead. It checks whether the current employee is the target manager. If it is, it adds the new employee to the left or right side. If not, it recurses into the left and right children of the current employee. This continues until the target manager is found or all employees have been checked.

#Something challenging was keeping the search from going wrong. Since current_node=None means starting at the root, passing a missing child into a recursive call would restart the search and loop forever. I was able to fix this by only recursing into children that exist. I also had to keep the manager not found error from printing at every dead end, so I tracked whether a call was top level one and returned true or false to indicate whether the manager was found. Having to handle three different errors and capitalization of left and right was also a challenge. I solved this by making the side input lowercase and checking for both left and right in the error messages.

#Trees are helpful when information has layers, such as a company chart, folders inside folders on a computer, or a family tree. A list wouldn't be able to show who belongs under whom but a tree has the ability to show relationships between different levels of information. Trees are also helpful and used in large databases because they let computers find information quickly, even when there is a lot of it.