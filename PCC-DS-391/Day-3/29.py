'''
     * 
    * * 
   *   * 
  *     * 
 *       * 
  *     * 
   *   * 
    * * 
     *
'''

print(" " * 4, "*")
for i in range(1,5):
    print(" " * (5 - i), "*", " " * (2*(i)-1), "*", sep= "")
for j in range(1,4):
    print(" " * (j+1), "*", " " * (2 * (4 - j) -1), "*", sep= "")
print(" " * 4, "*")