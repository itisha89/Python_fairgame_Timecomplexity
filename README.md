# **Fair Money Distribution Using Minimum Difference Partitioning**  

## **Problem Statement**  
Ramya has two children and gives them a jigsaw puzzle to solve together. As a reward, she allows them to split the money from the piggy bank to buy their favorite snacks. To be fair, Ramya distributes the money in such a way that the difference between the amounts each child receives is minimized.  

This project provides a solution to a general version of this problem—finding two groups of people who will split a given amount of money such that the difference between the amounts each group receives is the least.  

## **Approach & Key Functions**  

This problem is solved using **dynamic programming** and **combinatorial subset generation**. The main functions involved are:  

- **`DynamicPartition`**: Iterates over the given list of money values and builds a solution array, adding new elements to sublists to find optimal partitions.  
- **`possible`**: Recursively checks the size and sum of subsets and updates the dynamic programming (DP) array with `True/False` values to indicate feasible splits.  
- **`getAllCombinations`**: Generates all possible combinations of subsets of a given size for the given list.  
- **`findMin`**: Computes the total sum of the array and determines whether the sum is odd or even to guide the partitioning process.  
- **`findSubsetWithMinDiff`**: Extracts subsets from the generated combinations that match the minimum possible difference, ensuring the fairest split.  

## **Time Complexity Analysis**  

- **Overall Time Complexity**: \(O(n^3)\)  
- **Generating combination sets**: \(O(n^2)\)  
- **Finding subsets with the minimum difference**: \(O(n)\)  

## **Implementation Summary**  

- The program reads input data from a file (`inputPS08.txt`), where each line contains a list of integers representing the given set of coins/money values.  
- It generates all possible subsets and determines two sets with the minimum difference in sum.  
- The results are written to an output file (`outputPS08.txt`).  

### **Sample Inputs & Expected Outputs**  

#### **Input (from `inputPS08.txt`)**  
```
[1, 1, 1, 2, 2, 3, 4, 5, 10, 15, 18]
[1, 2, 3, 5, 8, 9, 11, 14, 15, 22, 25]
```

#### **Output (from `outputPS08.txt`)**  
```
Subset 1: [1, 1, 2, 4, 10, 15] 
Subset 2: [1, 2, 3, 5, 18] 
Minimum Difference: 0

Subset 1: [1, 2, 5, 9, 14, 22] 
Subset 2: [3, 8, 11, 15, 25] 
Minimum Difference: 1
```

## **Alternative Algorithm (Recursive Approach)**  

An alternate way to solve this problem is through recursion:  

1. Define a function `min_diff(i, total_amount, puzzles)`, where:  
   - `i` is the index of the current puzzle  
   - `total_amount` is the total money in the piggy bank  
   - `puzzles` is the list of integers representing different values  
2. Base Case: If `i == 0`, return `abs(total_amount/2 - puzzles[0])` since only one item is left.  
3. Recursive Case: Consider two possibilities:  
   - Assign the `i`-th element to the first child and compute `min_diff(i-1, total_amount - puzzles[i], puzzles)`.  
   - Assign it to the second child and compute `min_diff(i-1, total_amount - puzzles[i], puzzles)`.  
4. Return the minimum of both choices to get the optimal split.  

## **Conclusion**  

This project implements a **dynamic programming-based solution** to fairly split money between two groups while minimizing the difference. The approach ensures an optimal and computationally efficient solution for practical applications in **resource allocation, budgeting, and fair distribution problems**.  

---

## 🌍 Explore More Projects  
For more exciting machine learning and AI projects, visit **[The iVision](https://theivision.wordpress.com/)** and stay updated with the latest innovations and research! 🚀  

---
