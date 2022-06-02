#!/usr/bin/env ruby

# Binary search runs in logarithmic time in the worst case, making O(log ⁡ n) comparisons,
# where n is the number of elements in the array.
 
input = [1, 2, 3, 4, 5, 6, 7, 8, 11, 20]
 
def search(target, arr)
 
  left  = 0
  right = arr.size - 1

  while (left <= right) do

    mid = left + ((right - left) / 2)

    return true if arr[mid] == target

    if target < arr[mid]
      right = mid - 1
    else
      left = mid + 1
    end

  end

  return false

end
 
puts search(11, input)