## Longest Substring Without Repeating Characters (LeetCode #3)
- **Approach**: Sliding window with hash map to track unique characters. O(n) time, O(n) space.
- **Time Complexity**: O(n), where n is the length of the input string, due to the amortized linear time (the inner loop can not dominate the outter loop time) of the sliding window and hash map operations.
- **Space Complexity**: O(n), due to the use of hash map to store the frequency of each items.


## Group Anagrams (LeetCode #49)
- **Approach**: using hashmap to store anagrams with their unique value
- **Time Complexity**: O(n*k), inner loop takes O(n) to access each strings once, and the inner loop takes O(k) where k is max(len(strs))
- **Space Complexity**: O(n), it uses hash map. And list and tuples take O(1) since their length is fixed for 26 items.


## Longest Palindromic Substring (LeetCode #5)
- **Approach**: Expand around center, O(n²) time. 
- **Time Complexity**: O(n²)
- **Space Complexity**: O(n) 


## Reverse Words in a String (LeetCode #151)
**Approach**: using two pointers to reverse words after reducing all white spaces.
**Time Complexity**: O(n) where n is the length of words in a list.
**Space Complexity**: O(n) 

