class Node:
    def __init__(self, value=None):
        self.value = value  # Valor armazenado no nó
        self.next = None  # Referência para o próximo nó (inicialmente None)

class LinkedList:
    def __init__(self):
        self.head = None  # Cabeça da lista (inicialmente None)

    def insert(self, value):
        new_node = Node(value)  # Cria um novo nó
        new_node.next = self.head  # Aponta o novo nó para a cabeça atual
        self.head = new_node  # Atualiza a cabeça para o novo nó

    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:  # Se o nó a ser removido não é o primeiro
                    previous.next = current.next
                else:  # Se o nó a ser removido é o primeiro
                    self.head = current.next
                return
            previous = current
            current = current.next
        print(f"Valor {value} não encontrado.")

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def update(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                current.value = new_value
                return
            current = current.next
        print(f"Valor {value} não encontrado.")
        
    def sort(self):
        # If list is empty or has only one element, return
        if not self.head or not self.head.next:
            return
        
        # Helper function to get last node
        def get_last(start):
            while start and start.next:
                start = start.next
            return start
        
        # Helper function for partition
        def partition(start, end):
            if start == end or start == None:
                return start
                
            pivot = start.value
            curr = start
            tail = start
            
            while curr != end.next:
                if curr.value < pivot:
                    # Swap values
                    tail.value, curr.value = curr.value, tail.value
                    tail = tail.next
                curr = curr.next
                
            # Put pivot in correct position
            start.value, tail.value = tail.value, start.value
            return tail
            
        # Quick sort implementation
        def quick_sort(start, end):
            if start == None or start == end or start == end.next:
                return
                
            # Partition and get pivot
            pivot = partition(start, end)
            
            # Recursively sort before and after pivot
            if pivot != None and pivot != start:
                quick_sort(start, pivot)
            if pivot != None and pivot.next != None:
                quick_sort(pivot.next, end)
                
        # Get last node and start quick sort
        last = get_last(self.head)
        quick_sort(self.head, last)

    def reverse(self):
        previous = None
        current = self.head 
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous    
        
    def clear(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
        
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count