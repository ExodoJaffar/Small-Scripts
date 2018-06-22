class sw(object):
  def __init__(self, word:str,space) :
      self.word = word
      self.numbers = []
      self.numbers.append(0)
      self.space = space
      for n in range(len(self.word)) :
          if self.word[n] == self.space:
              self.numbers.append(n)
      self.numbers.append(len(self.word))
      return None
    
  def ch(self):
    lp = []
    for n in range(len(self.numbers)- 1):
      if self.word[self.numbers[n]] == self.space:
        lp.append(self.word[self.numbers[n]+1:self.numbers[n+1]])
      else:
        lp.append(self.word[self.numbers[n]:self.numbers[n+1]])
    return lp
  
#Tests
sw = sw('USD|12.4|DOLAR','|')
word = sw.ch()
for n in range(len(word)): print(word[n])


