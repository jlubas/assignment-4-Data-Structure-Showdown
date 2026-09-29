# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

#5. Unique Word Count
#Count how many distinct words are in the collection.
#Input: "one fish two fish red fish blue fish"
#Output: 5

text = "one fish two fish red fish blue fish"

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)
    
# Test the example
print(count_unique_words(text)) # Expected: 5

# Test an empty string
print(count_unique_words(""))  # Expected: 0

# Test repeated words
print(count_unique_words("cat cat cat"))  # Expected: 1

# Test all unique words
print(count_unique_words("red blue green"))  # Expected: 3

# What structure I chose and why?

  # For the timed challenge, I chose the Unique Word Count problem.
  # I decided to use a set because I learned that sets are useful for storing unique values and avoiding duplicates.
  # I used split() to separate the sentence into words, set() to keep each word only once, and len() to get the final count. 
  # This approach made sense to me because the question was asking for distinct words, not the total number of words.

# How the time limit shaped my decision?

  # I set my timer for the required 30 minutes and started by drawing the three
  # steps on a piece of paper. Since I am more of a visual learner, I wrote
  # split(), set(), and len() in order so I could see what needed to happen first.
  # Before starting the timed challenge, I had spent a few hours practicing
  # different problems that were similar to the ones in this assignment.
  # That practice made it easier for me to recognize the pattern and decide
  # what to do next. I noticed that I completed this problem in less time
  # than some of the problems I practiced earlier.

# What trade-offs or compromises I made under time pressure?

  # Under the time pressure, I decided to stay with the solution I understood
  # instead of trying a more complicated way.
  # So, I stayed with the approach that I understood and focused on making sure each part worked. 
  # I had to remind myself that split() only separates the words and that set() is what removes the duplicates.
  # Once I remembered that difference, I was able to finish the code and test it with the example from the assignment.
  # My program returned 5, which matched the expected result.
