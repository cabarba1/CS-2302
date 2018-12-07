# -*- coding: utf-8 -*-
########################
#Course: CS2302
#Author: Cezar Barba
#Assignment: Lab 3 Option A
#Instructor: Diego Aguirre TA: Manoj Saha
#Date of Last Modification: 12/06/2018
#The purpose of this program is to read words and their embeddings and with given pairs of words
#from a file, it displays the similarity of the paired words. The program gives the user the option
#of either using an avl tree or a Red-Black tree to store the words and embeddings.
#This program also computes the number of nodes in the tree and the height of the tree.
#It can also generate all of the words stored in a tree in ascending order and
#also generate the words in a given depth in to a file.
########################
import time
import math
from avl_tree import AVLTree, Node
from redblack_tree import RBTNode, RedBlackTree
 
#This method is used for separating the word and embedings from a given line. It is used in the read_from_file method
def extract_word_and_embedding(line):
    
        line_tokens = line.split(' ')
                
        word = line_tokens[0]
        
        embedding = []
        
        for j in range(1, 51):
            embedding.append(float(line_tokens[j]))
            
        return word, embedding
        
    
        
#This method reads a text file with a word and 50 floating point numbers in each line seperated by spaces
#and returns two list arrays one containing the words and the other the 50 numbers for each word.
#calls extract_word_and_embedding for each line
def read_from_file():
    words = open('glove.6B.50d.txt', encoding='utf-8', errors='ignore' ).readlines()
    
    all_words = []
    all_embeddings = []
    
    for i in range(len(words)):
        line = words[i].replace("\n", "")
        
        word, embedding = extract_word_and_embedding(line)
        all_words.append(word)
        all_embeddings.append(embedding)
        
        #print(word)
        #print(embedding)
    return all_words, all_embeddings

#This method takes the user's input and constructs either an AVL or Red-Black Tree and returns it.
#calls read_from_file() to recieve the embeddings
def user_choice():
    x =input("Do you want to use an AVL tree or a Red-Black tree?(1 for AVL or 2 for Red-Black) ")
    valid_choice = False
    
    tree = None
    while valid_choice == False:
        if x == '1':
            #AVL
            tree = AVLTree()
            valid_choice = True
            
            all_words, all_embeddings = read_from_file()
    
            for i in range(len(all_words)):
                tree.insert(Node(all_words[i], all_embeddings[i]))
                
            #search_node = tree.search("hello")
            #print(search_node.embedding)
            
        elif x == '2':
            #Red-Black
            tree = RedBlackTree()
            valid_choice = True
            
            all_words, all_embeddings = read_from_file()
    
            for i in range(len(all_words)):
                tree.insert(all_words[i],all_embeddings[i])
                
            #search_node = tree.search("hello")
            #print(search_node.embedding)
       
        else:
            x=input("That is not a valid choice. Choose 1 for AVL or 2 for Red-Black ")
        
    return tree


#This method reads a .txt file containing a pair of words each line seperated by a space
#and returns two arrays representing the first and second word of the pairs.
def read_word_pairs():
    pairs= open('word_pairs.txt', encoding = 'utf-8', errors='ignore').readlines()
    
    first_word_list = []
    second_word_list = []
    
    for i in range(len(pairs)):
        line = pairs[i].replace("\n", "").split(" ")
        first_word_list.append(line[0])
        second_word_list.append(line[1])
        #print(first_word)
        #print(second_word)
    return first_word_list, second_word_list

    
#compares the similarity of two words using the embeddings that were read by
#using the equation: (e0 dotproduct e1)/(|e0| dotproduct |e1|)
# calls compute_dot_product since
def compare_word_pairs(tree):
    first_word_list, second_word_list = read_word_pairs()
    comparisons = []
    
    for i in range(len(first_word_list)):
        search_first_word= tree.search(first_word_list[i])
        search_second_word = tree.search(second_word_list[i])
        
        #print(search_first_word.embedding)
        #print(search_second_word.embedding)
        
        
        top = compute_dot_product(search_first_word.embedding, search_second_word.embedding)

        mag1 = compute_dot_product(search_first_word.embedding, search_first_word.embedding)
        mag2 = compute_dot_product(search_second_word.embedding, search_second_word.embedding)
        
        comparisons.append(compute_embedding_comparison(top,mag1,mag2))
        print(search_first_word.key, end = " ")
        print(search_second_word.key, end = " ")
        print(comparisons[i])
        
#computes the dot product and returns it.
def compute_dot_product(e1,e2):
    dot_product = 0 
    for i in range(len(e1)):
        dot_product += e1[i]*e2[i]  
        
    return dot_product
#computes:  (e0 dotproduct e1)/(|e0| dotproduct |e1|)      
def compute_embedding_comparison(top,mag1,mag2):
    mag1=math.sqrt(mag1)
    mag2=math.sqrt(mag2)
    
    comp= top/(mag1*mag2)
    
    return comp

#computes the number of nodes in a tree by recursively counting the left and right sides.
def compute_number_of_nodes(tree):
    count = 0
    if tree == None:
        return count
    count+=1
    #print(count)
    if hasattr(tree, 'root'):
        return count + compute_number_of_nodes(tree.root.left)+compute_number_of_nodes(tree.root.right)
    else: return count + compute_number_of_nodes(tree.left)+compute_number_of_nodes(tree.right)



# computes the height of a tree by recursively getting the max height of the left and right sides.
def compute_height(tree):
    if tree == None:
        return 0
    if hasattr(tree,'root'):
        right_height = compute_height(tree.root.right)
        left_height = compute_height(tree.root.left)
    else:
        right_height = compute_height(tree.right)
        left_height = compute_height(tree.left)
    return max(right_height, left_height)+1
    

#writes elements of a tree to a file using inorder travesal
def generate_words_ascending_order(tree):
    f = open('words_ascending.txt', 'a')
    if tree == None:
        return
    if hasattr(tree, 'root'):
        generate_words_ascending_order(tree.root.left)
        #print(tree.key)
        try:
            f.write(tree.root.key +'\n')
        except:
            print("Ignoring key: " + tree.key)
            
        generate_words_ascending_order(tree.root.right)
        
    else:
        generate_words_ascending_order(tree.left)
       # print(tree.key)
        try:
            f.write(tree.key+ '\n')
        except:
            print("Ignoring key: " + tree.key)
        generate_words_ascending_order(tree.right)
    
    f.close()
 
#uses recursion to reach a given depth and writes all the elements of a tree at that depth
def generate_words_at_depth_ascending_order(tree,d,tree_height):
    if d > tree_height:
        print("Invalid tree height")
        return

    if tree == None:
        return
    f = open('words_ascending_at_depth.txt', 'a')
    if(d==0):
        if hasattr(tree,'root'):
            try:
                f.write(tree.root.key+ '\n')
            except:
                print("Ignoring key at depth: " + tree.key)
        else:
            try:    
                f.write(tree.key+ '\n')
            except:
                print("Ignoring key at depth: " + tree.key)
        return
    
    if hasattr(tree,'root'):
        generate_words_at_depth_ascending_order(tree.root.left, d-1, tree_height)
        generate_words_at_depth_ascending_order(tree.root.right, d-1, tree_height)
    else:
        generate_words_at_depth_ascending_order(tree.left, d-1, tree_height)
        generate_words_at_depth_ascending_order(tree.right, d-1, tree_height)
    
    f.close()
    
    
    
    
    
    
    
    
start_time = time.time()
tree = user_choice()   
print( "%s seconds for generating the tree"  % (time.time() - start_time))

start_time = time.time()
compare_word_pairs(tree)
print( "%s seconds for comparing the words"  % (time.time() - start_time) )

start_time = time.time()
generate_words_ascending_order(tree)
print("%s seconds for generating the words in ascending order"  % (time.time() - start_time) )

start_time = time.time()
generate_words_at_depth_ascending_order(tree,5,compute_height(tree))
print("%s seconds for generating the words in ascending order at a depth"  % (time.time() - start_time) )

start_time = time.time()
a=compute_number_of_nodes(tree)
print("%s seconds to compute the number of nodes"  % (time.time() - start_time) )

start_time = time.time()
b=compute_height(tree)
print("%s seconds to compute the height of the tree."  % (time.time() - start_time) )

print("Number of Nodes:", end = " ")
print(a)
print("Height of Tree: ", end = " ")
print(b)
