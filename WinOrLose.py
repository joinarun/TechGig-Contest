''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(): 
 #Get total number of testcases
  TCS = int(input())
  
  #Initialize 2d array
  V=[0 for y in range(TCS)]
  P=[0 for y in range(TCS)]
  
  for i in range(TCS):
    #Get the size on array. This is actually not required.
    N = int(input()) 
    #Get Villan strength
    V[i] = list(map(int, input().split()))
    #Get Player energy
    P[i] = list(map(int, input().split()))
  
  #Iterate through each testcase  
  for i in range(TCS):
    V[i].sort()
    P[i].sort()
    flag=0
    #After sorting compare each value in Player and Villan array. If less lose else win
    for x in range(len(P[i])):
      if P[i][x] <= V[i][x]:
         flag=1
    if flag == 0:
      print("WIN")
    else:
      print("LOSE")  
main()
