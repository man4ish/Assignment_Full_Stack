from collections import defaultdict
from random import choice, shuffle
import urllib
import urllib.parse
import sys

class fragaseemble:
      def overlap(self,frag1, frag2):
          """ get the maximum overlap between frag1 & frag2 and overlap start position """

          overlaps = []

          for i in range(len(frag2)):
              for j in range(len(frag1)):
                  if frag1.endswith(frag2[:i + 1], j):
                     if i >= 3:
                        overlaps.append((i, j))

          return max(overlaps) if overlaps else (0, -1)


      def get_output_string(self,fraglst):
          overlaps = defaultdict(list)
          while len(fraglst) > 1:
                overlaps.clear()

                for frag1 in fraglst:
                    for frag2 in fraglst:
                        if frag1 == frag2:
                           continue

                        amount, start = self.overlap(frag1, frag2)
                        overlaps[amount].append((start, frag1, frag2))  # add key (amount of overlap) and value (start position between a and b)
                  

                maximum = max(overlaps)                         # pick maximum overlaps 
 

                if maximum == 0:                                # if maximum =0  then break
                   break

                start, frag1, frag2 = overlaps[maximum][0]        

                fraglst.remove(frag1)
                fraglst.remove(frag2)
                fraglst.append(frag1[:start] + frag2)    
          merged_str = ''.join(fraglst)
          return (urllib.parse.unquote_plus(urllib.parse.unquote_plus(merged_str)))

if __name__ == "__main__":
   ''' reading input file'''
   fobj=fragaseemble()
   filename=''
   if (len(sys.argv) == 1):
      fragments = input("Enter fragments: ")
      assert (fragments), 'Entered input is null!'
      lst = fragments.rstrip().split(" ")
      #print(fobj.get_output_string(lst))    
   else: 
      filename=sys.argv[1]
      file = open(filename, "r")
      lines= file.readlines()
      file.close()
      lst = []
      for i in lines:
          lst.append(i.strip())

   print(fobj.get_output_string(lst))
