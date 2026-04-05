class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        
        num = False      # digit seen
        dot = False      # '.' seen
        exp = False      # 'e' or 'E' seen
        
        for i, c in enumerate(s):
            
            if c.isdigit():
                num = True

            elif c in ['+', '-']:
                # sign only valid at start OR just after exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False

            elif c == '.':
                # dot not allowed after exponent OR twice
                if dot or exp:
                    return False
                dot = True

            elif c in ['e', 'E']:
                # exponent must appear once and after a number
                if exp or not num:
                    return False
                exp = True
                num = False   # reset (need number after e)

            else:
                return False
        
        return num
        