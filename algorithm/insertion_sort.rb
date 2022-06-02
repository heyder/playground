#!/usr/bin/env ruby

# The worst-case (and average-case) complexity of the insertion sort algorithm is O(n²).
# Meaning that, in the worst case, the time taken to sort a list is proportional to the square of the number of elements in the list. 
# The best-case time complexity of insertion sort algorithm is O(n) time complexity.

input = [12, 11, 13, 5, 6]
 
def sort(input)
 
  j,k = nil,nil
  i = 1

  while i < input.length do
    k = input[i]
    j = i - 1

    while j>= 0 && input[j] > k do
      input[j + 1] = input[j]
      j = j -1
    end

    input[j+1] = k
    i += 1  

  end

  return input

end
 
# run test
puts sort(input).inspect