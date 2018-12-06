
########################
#Course: CS2302
#Author: Cezar Barba
#Assignment: Lab 5 Option B(Min-Heap Implementation)
#Instructor: Diego Aguirre TA: Manoj Saha
#Date of Last Modification: 12/05/2018
#The purpose of this program is to complete the implementation of Min-Heap 
#from the given code. The methods heap_sort, extract_min, and insert were implemented.
#This program also reads a file with a list of numbers separated with commas and
#prints them in a sorted sequence
########################

class Heap:
 def __init__(self):
     self.heap_array = []
 
#For the heap sort method I compare the child with its parent and switch if the 
#property of the min heap is broken.
 def heap_sort(self):
     if len(self.heap_array)<2:
         return
     property_broken = True
     while property_broken == True:
         property_broken = False
         for i in range(1,len(self.heap_array)):
             if int(self.heap_array[(i-1)//2]) > int(self.heap_array[i]):
                 property_broken = True
                 temp = self.heap_array[(i-1)//2]
                 self.heap_array[(i-1)//2] = self.heap_array[i]
                 self.heap_array[i] = temp
     
     return

#For insert an element is inserted and the heap array is sorted after every insert
 def insert(self, k):
     self.heap_array.append(k)
     # TODO: Complete implementation
     self.heap_sort()
 
#For extract_min the first element which would be the minimum element in
#a min heap is taken and replaced with the last element in the heap array
#the array is then popped so that there aren't any duplicates and then the
#heap array is sorted since the property of the min heap was broken.
 def extract_min(self):
     a = len(self.heap_array)
     if self.is_empty():
         return None
 
     min_elem = self.heap_array[0]
     # TODO: Complete implementation
     self.heap_array[0]=self.heap_array[a-1]
     self.heap_array.pop()
     
     self.heap_array.sort()
     
     print("Extracted min: "  + min_elem )
    
     return min_elem
 
 def is_empty(self):
     return len(self.heap_array) == 0
 
#iterates through the heap array and prints the elements   
 def print_heap(self):
    print("Printing heap:")
    for i in range(len(self.heap_array)):
        print(self.heap_array[i])

#reads from a file and initializes a min heap with the numbers given in a file
def read_from_file():
    file = open("numbers_for_min_heap.txt", "r")
    unsorted_num = file.readline().split(",")
    min_heap = Heap()
    for i in range(len(unsorted_num)):
        min_heap.insert(unsorted_num[i])
    return min_heap




#This is for testing the methods
new_heap = read_from_file()
new_heap.print_heap()
a = new_heap.extract_min()
new_heap.print_heap()
    
 
 
