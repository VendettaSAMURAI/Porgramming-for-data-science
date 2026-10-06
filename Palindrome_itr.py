def palindrome(string):
    i = 0
    j = -1

    i = 0
    while i < j:
      if string[i] != string[j]:
        return False
       
    i += 1
    j -=1
    return True
