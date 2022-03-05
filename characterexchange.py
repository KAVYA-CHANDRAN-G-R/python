word_1=input("Enter any word:")
word=list(word_1)
word[0],word[-1]=word[-1],word[0]
word_2="".join([str(elem)for elem in word])
print("The string after exchange first end last position:",word_2)
