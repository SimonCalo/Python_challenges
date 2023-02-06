
def restoreIpAddresses(s):
    def backtrack(s, start, segments, res):
        if start == len(s) and len(segments) == 4:
            res.append('.'.join(segments))
            return
        if start == len(s) or len(segments) == 4:
            return
        for i in range(start, start+3):
            if i < len(s) and is_valid(s[start:i+1]):
                segments.append(s[start:i+1])
                backtrack(s, i+1, segments, res)
                segments.pop()
    
    def is_valid(s):
        if len(s) == 0 or (s[0] == '0' and len(s) > 1) or int(s) > 255:
            return False
        return True
    
    res = []
    backtrack(s, 0, [], res)
    return res