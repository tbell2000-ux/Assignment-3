# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next
        return removed.value

    def peek(self):
        return None if self.top is None else self.top.value

    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty.")
            return
        while current:
            print(current.value)   # ✅ uses .value
            current = current.next


def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo stack
            print(f"Action performed: {action}")

        elif choice == "2":
            undone = undo_stack.pop()
            if undone:
                redo_stack.push(undone)
                print(f"Action undone: {undone}")
            else:
                print("No actions to undo.")

        elif choice == "3":
            redone = redo_stack.pop()
            if redone:
                undo_stack.push(redone)
                print(f"Action redone: {redone}")
            else:
                print("No actions to redo.")

        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()
