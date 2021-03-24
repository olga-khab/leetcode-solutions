class Solution:
    def reverse(self, x: int) -> int:
      flag = 1 if (x >= 0) else -1
      rev = ""
      x=abs(x)
      for i in range(0,len(str(abs(x)))):
          rem = x % 10
          rev+=(str(rem))
          x = x // 10
      if flag*int(rev) > (2**31 - 1) or flag*int(rev) < -2**31:
          return 0
      else:
          return flag*int(rev)

  # reverse a binary unsigned integer (return decimal)
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]
        num = "0"*(32-len(num))+num
        num = num[::-1]
        return int(num,2)
 # counts number of 1s in a 32-bit binary integer
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(0,32):
            if n & mask :
                bits += 1
            mask <<= 1
        return bits
