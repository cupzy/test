class equation: 
def __init__(self,a,b,c): 
  self.a = a; 
  self.b = b; 
  self.c = c; 
def print(self): 
  print(self.a+'x^2 + '+self.b+'x + '+self.c+'=0'); 
def solve(self): 
  d = int(self.b)**2 - 4*int(self.a)self.c; 
  return [((-int(self.b)+d**(1/2))/2/int(self.a)),((-int(self.b)-d**(1/2))/2/int(self.a))]; 
inp = input('Enter a,b and c separated by whitespace\n'); 
inp = inp.split(' '); 
eq = equation(inp[0],inp[1],inp[2]); 
eq.print(); 
ans = eq.solve(); 
print('x = '+str(ans[0])+'\nx = '+str(ans[1]))
