def main(): 
 #Get total number of testcases
  TCS = int(input())
  
  #Initialize 2d array to store each list
  V=[0 for y in range(TCS)]
  
  for i in range(TCS):
    #Get the size on array. This is actually not required.
    N = int(input()) 
    
    #Get the numbers. The array is accessed as V[0], V[1] etc..
    V[i] = list(map(int, input().split()))

  #Iterate through each testcase  
  for i in range(TCS):  
    my_map=[]
    #algorithm to find max sum
    def find_max_sum(arr): 
        incl = 0
        excl = 0
        n=0
        for i in arr:    
            if excl>incl:
              new_excl = excl
            else: 
              new_excl =incl            
            # Current max including i 
            incl = excl + i 
            excl = new_excl
            #store the values in array to trace back
            my_map.append([incl,excl])        
            n=n+1
        # return max of incl and excl 
        return (excl if excl>incl else incl) 
        
    #copy the array to a temp and do trace back to find elements  
    arr = V[i]
    my_sum = find_max_sum(arr)
    #print(my_map)
    
    
    my_dict={}
    for j  in reversed(range(0,len(my_map))):
      if my_map[j][0] > my_map[j][1]:
        my_dict[my_map[j][0]]=j
      else:
        my_dict[my_map[j][1]]=j
    
    #algorithm to trace back the map
    final_ans=[]
    while my_sum > 0 :
          my_index = my_dict[my_sum]
          my_sum = my_sum - arr[my_index]
          final_ans.append(arr[my_index])
    answer=''.join(map(str, final_ans))
    print(answer)
main()
