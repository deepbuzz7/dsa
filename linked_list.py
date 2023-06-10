class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head
    #appending the node to the list
    def append(self, new_node):
        current=self.head
        if current:
            while current.next:
                current=current.next
            current.next=new_node
        else:
            self.head=new_node
    # deleting the node from the list
    def delete(self,value):
        current=self.head
        prev=self.head
        if current:
            # if the first value is to be deleted
            if current.value==value:
                self.head=current.next
            else:
                while current:
                    current=current.next
                    if current is None:
                        print("value not found")
                        break
                    if current.value==value:
                        prev.next=current.next
                        break
                    prev=prev.next
        else:
            print("list is empty")
            

def traverse_linked_list(ll):
    head=ll.head
    if head:
        current=head
        while current:
            print(current.value)
            current=current.next
    else:
        print("Linked list is empty")


n1=Node('a')
n2=Node('b')
n3=Node('c')

ll=LinkedList()
ll.append(n2)
ll.append(n3)
ll.delete('a')
traverse_linked_list(ll)