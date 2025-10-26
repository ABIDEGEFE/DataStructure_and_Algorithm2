## Valid Anagram (LeetCode #242)
- **Approach**: Single hash map approach.
- **Time Complexity**: O(n) to touch each item in the string at least once.
- **Space Complexity**: O(n) for single hash map.


## Reverse String (LeetCode #344)
- **Approach**: Used two-pointer technique to reverse the list in-place by swapping characters from both ends.
- **Time Complexity**: O(n) for a single pass through half the list.
- **Space Complexity**: O(1) for constant extra space.


## Palindrome Number (LeetCode #9)
- **Approach**: Convert integer to string, I have used a way of getting the module of each current x, then adding it with the reversed_sum variable. It helps me to secure O(1) space complexity..
- **Time Complexity**: O(n) to access each digit at least once..
- **Space Complexity**: O(1).

## First Unique Character in a String (LeetCode #387)
- **Approach**: Use a hash map to count character frequencies, then find the first character with frequency 1.
- **Time Complexity**: O(n) for two linear passes.
- **Space Complexity**: O(n) for hash map storage.


## String to Integer (atoi) (LeetCode #8) (MEDIUM LEVEL)
- **Approach**: Build numeric string from digits and sign, handle whitespace and overflow.
- **Time Complexity**: O(n) for accessing all values at worst case at least once.
- **Space Complexity** - O(1)

  ## Longest Common Prefix (LeetCode #14)
- **Approach**: Compare characters across strings using the shortest string’s length. O(n*m) time, O(m) space.
- **Time Complexity**: O(n*m), m is for the length of string with minimum value
- **Space Complexity**: O(m) 


## Valid Palindrome (LeetCode #125)
- **Approach**: In-place two-pointer approach for O(1) space
- **Time Complexity**: O(n) at worst case
- **Space Complexity**: O(1) for in-place string usage.


## Longest Substring Without Repeating Characters (LeetCode #3)
- **Approach**: Sliding window with hash map to track unique characters. O(n) time, O(n) space.
- **Time Complexity**: O(n), where n is the length of the input string, due to the amortized linear time (the inner loop can not dominate the outter loop time) of the sliding window and hash map operations.
- **Space Complexity**: O(n), due to the use of hash map to store the frequency of each items.


## Group Anagrams (LeetCode #49)
- **Approach**: using hashmap to store anagrams with their unique value
- **Time Complexity**: O(n*k), inner loop takes O(n) to access each strings once, and the inner loop takes O(k) where k is max(len(strs))
- **Space Complexity**: O(n), it uses hash map. And list and tuples take O(1) since their length is fixed for 26 items.








