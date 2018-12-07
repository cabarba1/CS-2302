# -*- coding: utf-8 -*-
########################
#Course: CS2302
#Author: Cezar Barba
#Assignment: Lab 2 Option A
#Instructor: Diego Aguirre TA: Manoj Saha
#Date of Last Modification: 12/06/2018
#The purpose of this program is to implement a solution to
#find duplicate IDs in the files activision.txt and vivendi.txt
########################
class Node(object):
    def __init__(self, item, next):
         self.item = item
         self.next = next
  
    
#reads from two files and creates an unordered list
def employee_list():
    employees=None
    f2= open("activision.txt","r")
    #f2= open("activision_test.txt","r")
    activision = []
    for x in f2:
        activision.append(f2.readline())
    for i in range(len(activision)):
        employees = Node(int(activision[i]), employees)
    f1= open("vivendi.txt","r")
    #f1= open("vivendi_test.txt","r")
    vivendi = []
    for x in f1:
        vivendi.append(f1.readline())
    for i in range(len(vivendi)):
        employees = Node(int(vivendi[i]), employees)
    
    return employees

#uses nestedloops to compare an element in the list to the other elements in the list
#to find duplicates.
def compare_every_element(employees):
    duplicate_list = []
    temp1=employees
    while temp1 != None:
        temp2= temp1.next
        while temp2 != None:
                if temp1.item == temp2.item:
                    duplicate_list.append(temp1.item)
                temp2= temp2.next
        temp1= temp1.next
    print("These are the IDs with duplicates:")
    for i in duplicate_list:
        print(i)
        
                

             
#performs bubble sort to a linked list and prints the ordered list with duplicates being next to each other.                
                
def bubble_sort(employees):
    temp = employees
    swap_occurrence = "t"
    while swap_occurrence == "t":
        temp = employees
        swap_occurrence == "f"
        while temp.next.item != -1:
            if temp.item > temp.next.item:
                swap_occurrence == "t"
                num_switch = temp.item
                temp.item = temp.next.item
                temp.next.item = num_switch
            temp = temp.next
    temp = employees
    while temp.next.item != 1:
        print(temp.item)
        temp = temp.next
    return    

#Initiales an array with boolean values to check if an ID is duplicate by iterating through
#the whole unordered list. appends to another array the IDs that were duplicates and prints them.
def seen_before(employees):
    m=6000
    seen= [False]* (m+1)
    temp = employees
    duplicates=[]
    while temp != None:
        if seen[temp.item] == True:
            duplicates.append(temp.item)
        else:
            seen[temp.item]=True
        temp = temp.next
    print("These are the IDs with Duplicates")
    for i in range(len(duplicates)):
        print(duplicates[i])
        
#main method for testing the other methods
def main():
    employees = employee_list()
    compare_every_element(employees)
    bubble_sort(employees)
    seen_before(employees)
    
            
main()