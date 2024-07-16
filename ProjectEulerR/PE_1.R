# Written 15/07/2024 by Christina Mazilu
# Project Euler Question 1: https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6 and 9. Find the sum of all the multiples of 3 or 5 below 1000

# Initialize an empty vector to store multiples of 3 or 5
total <- c()

# Iterate through numbers 0 to 9
for (i in 0:999) {
  if (i %% 3 == 0 | i %% 5 == 0) {  # Check if i is divisible by 3 or 5
    total <- c(total, i)           # Add i to the total vector
  }
}

cat("Max:", max(total), "\n")      # Print the maximum value in total
cat("Sum:", sum(total), "\n")      # Print the sum of all values in total