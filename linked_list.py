class LinkedList:
    __count = None

    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head:Item = None

    

    @property
    def count(self):
        index = -1
        current = self.head
        while current:
            current = current.next
            index +=1
        self.__count = index
        return self.__count
    
    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            return
        
        while current.next:
            current = current.next
        item = LinkedList.Item(value)
        current.next = item

    def append_by_index(self, value, index): 
        current=self.head 
        if index==0: 
            item = LinkedList.Item(value) 
            item.next = self.head 
            self.head = item 
        else: 
            for i in range(index-1): 
                current=current.next 
                 
            item = LinkedList.Item(value) 
            item.next=current.next 
            current.next=item

    def remove_first(self):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_first_value(self, value):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        if self.head.value == value:
            self.head = self.head.next
            return
        current=self.head
        while current.next.value!=value:
                if current.next.next is None:
                    raise ValueError("Ошибка!")
                current = current.next
        current.next = current.next.next

    

    def remove_last_value(self, value):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")

        current=self.head
        current1=None

        while current.next:
            if current.next.value==value:
                current1=current
            current=current.next

        if current1 is not None:
            current1.next=current1.next.next

        else:
            if self.head.value == value:
                self.head = self.head.next
                return
            else:
                raise ValueError("Ошибка!")
            
    def remove_at(self, index):
        if self.head is None:
            raise ValueError("Элементов нет, удалять нечего!")
        if index==0:
            self.head=self.head.next
        else:
            current=self.head
            for i in range(index-1):
                current=current.next
            if current.next is None:
                raise ValueError("Ошибка!")
            current.next=current.next.next



   



my_list = LinkedList()
my_list.append_end(3)
my_list.append_end(4)
my_list.append_end(8)
my_list.append_end(1)
my_list.append_end(7)
my_list.append_end(9)
#my_list.remove_at(0)
my_list.remove_first()
#my_list.remove_first_value(9)
#my_list.remove_last()
#my_list.remove_last_value(1)

