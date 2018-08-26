def answer(xs):
# given input [-2, -3, 4, -5] output max product possible... => 60
# Go through array, create a negs array of just neg numbers. if length is odd, remove the smallest abs value, or the largest number
# from the main array. 
# Edge case: all 0's and one neg number => 0
# Go through the now modified array and multiply all numbers that are not 0 and return that product.
