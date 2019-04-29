A = int(input('Fala A: '))
B = int(input('Fala B: '))
C = int(input('Fala C: '))

if (abs(B-C)<A<B+C) and (abs(A-C)<B<A+C) and (abs(A-B)<C<A+B):
  print("É UM TRIANGULO ", end='')
  
  if A == ((B**2)+(C**2))**(1/2) or B == ((A**2)+(C**2))**(1/2) or C == ((B**2)+(A**2))**(1/2):
    print("RETANGULO ", end='')
    
  if A != B :
    
    if B != C:
      print("ESCALENO")
      
    else: print("ISOSCELES")
    
  elif A == C:
    print("EQUILATERO")
    
  else:
    print("ISOSCELES")
  
else:
  print("NÂO É UM TRIANGULO")

