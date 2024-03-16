# Container with most water - 11
This is a leetcode, medium level problem

# Question
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

# Approach
1) we can solve this by brute force i.e.,
   a) Iterate over the array(heights) from i=0 to len(height)
   b) Iterate j from i+1 to len(height)
   c) Store area as
     - area = width * height i.e.,
     - area = (i-j) * min(height[i],height[j])
   d) Update the area using "max" function

By using this approach the time complexity will be O(n^2)

2) 2-pointer approach
   a) Take two pointers left =0 and right = len(height)-1
   b) While left is less than right calculate area as discussed to brute force approach
   c) Now we need to update the left and right pointers based on the condition i.e.,
    - if height[left] < height[right], update left = left + 1
    - else we can update the right = right - 1
  
With this approach the time complexity will be O(n)

Leetcode Profile - [https://leetcode.com/j-lokesh/](Tap me)



