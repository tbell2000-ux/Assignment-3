# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None: 
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:  # empty queue
            return None
        removed = self.front
        self.front = self.front.next
        if self.front is None:  # queue became empty
            self.rear = None
        return removed.value

    def peek(self):
        return None if self.front is None else self.front.value

    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty.")
            return
        while current:
            print(current.value)   
            current = current.next


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            helped = queue.dequeue()
            if helped:
                print(f"{helped} has been helped.")
            else:
                print("No customers to help.")

        elif choice == "3":
            next_customer = queue.peek()
            if next_customer:
                print(f"Next customer: {next_customer}")
            else:
                print("No customers in the queue.")

        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()


# Why is a stack the right choice for undo/redo?
# A stack is convient for implementing an undo/redo system.
# Actions that are peformed most recently need to be the first to be undone.
# By pushing each action onto the undo stack as it occurs, we can easily remove the last action when the user chooses to undo, restoring the program to its previous state.
# When an action is undone, it can be added to a redo stack, allowing the user to redo it if needed.
# Reversing and reapplying user actions makes stacks straightfowarad and efficient to code in.

# Why is a queue better suited for the help desk?
# Customers should be assisted in the order they arrive to ensure fairness.
# When a new customer enters the queue, they are added to the end, and the next customer to be helped is always taken from the front.
# This prevents any customer from being skipped or unfairly delayed so the help desk can mantain an organized workflow.

# How do your implementations differ from Python’s built-in lists?
# While Python’s built-in lists can be used to implement stacks and queues, custom implementations often include additional logic to manage the data structure.
# An undo/redo system may clear the redo stack whenever a new action is performed.
# This is something not automatically handled by a list.
# Similarly, a queue for a help desk may include helper methods like viewing the next customer or removing a customer.
# These customizations make the data structures easier to use and understand in the context of their intended purpose.