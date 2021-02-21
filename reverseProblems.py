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
