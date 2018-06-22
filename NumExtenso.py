def numExte(num:str):
  dic = {0:{0:'',1:'um',2:'dois',3:'tres',4:'quatro',5:'cinco',6:'seis',7:'sete',8:'oito',9:'nove'},
       1:{0:'',1:'dez',2:'vinte',3:'trinta',4:'quarenta',5:'cinquenta',6:'sessenta',7:'setenta',
       8:'oitenta',9:'noventa',11:'onze',21:'doze',31:'treze',41:'quatorze',51:'quinze',61:'dezesseis',
       71:'dezesete',81:'dezoito',91:'dezenove'},2:{0:'',1:'cento',2:'duzentos',3:'trezentos',4:'quatrocentos',
       5:'quinhentos',6:'seiscentos',7:'setecentos',8:'oitocentos',9:'novecentos'}
       }
  num = num[::-1]
  li = []
  l = len(num)
  n = ''
  if num[1] == '1' :
    li.append(dic[1][int(num[0:2])])
    for i in range(2,l):
      li.append(dic[i][int(num[i])])
      
    li = li[::-1]
    l = len(li)
    for i in range(l):
      if i != l - 1:
        n += li[i] + " e "
      else:
       n += li[i]
       
  else:
    for i in range(l):
      li.append(dic[i][int(num[i])])
      
    li = li[::-1]
    l = len(li)
    for i in range(l):
      if i != l - 1:
        n += li[i] + ' e '
      else:
        n += li[i]
  return n 

#Test
print(numExte('919'))

