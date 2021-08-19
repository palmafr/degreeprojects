
#Much of the calculating code has been translated from the Java version of it, found at http://francis-palma.net/wp-content/uploads/2016/07/Project.zip

def get_pairs(list, eli_list):

   pairs = []
   max_size = len(list)
   num_req = len(list[0])
   eli_strings = []
   for ell in eli_list:
       if ell != [0, 0]:
         rr1 = ell[0].__str__()
         rr2 = ell[1].__str__()
         eli_strings.append([rr1, rr2])
   if eli_list[0] != [0, 0]:      
    flat_list = [item for sublist in eli_strings for item in sublist]
    flatta_list = []
    index = 0
    for i in range(3):
       flatta_list.append(flat_list[index] + " " + flat_list[index + 1])
       index = index + 1
       index += 1

   for i in range(max_size):
       for k in range(num_req-1):
           m = k + 1
           while m < num_req:
               r1 = list[i][k]
               index11 = k
               r2 = list[i][m]
               index12 = m
               index21 = 0
               index22 = 0
               m += 1
               j = i + 1
               
               while j < max_size:
                   for l in range(num_req):
                       if list[j][l] == r1:
                           index21 = l
                       if list[j][l] == r2:
                           index22 = l 
              
                   j += 1
                   
                   if index11 <= index12 and index21 <= index22:
                       continue
                   else:
                       pair = r1 + " " + r2
                       if r1+" "+r2 in pairs or r2+" "+r1 in pairs:
                           continue
                       if eli_list[0] != [0, 0]: 
                        if r1+" "+r2 in flatta_list or r2+" "+r1 in flatta_list:
                           continue
                       pairs.append(pair)
   return pairs         
