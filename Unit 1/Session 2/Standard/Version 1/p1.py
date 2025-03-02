# Problem 1: Reverse Sentence
# Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.

# def reverse_sentence(sentence):
#     pass
# Example Usage:

# sentence = "tubby little cubby all stuffed with fluff"
# reverse_sentence(sentence)

# sentence = "Pooh"
# reverse_sentence(sentence)
# Example Output:

# "fluff with stuffed all cubby little tubby"
# "Pooh"



def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))