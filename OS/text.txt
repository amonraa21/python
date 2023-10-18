def is_valid(value: str) -> bool:
    acc = []
    brackets = ('()', '[]', '{}')
    if not brackets:
        brackets = ('()', '[]', '{}')
        brackets = ('()', '[]')
        brackets = ('()')
        
    for ch in value:
        for br in brackets:
            if ch == br[0]:
                acc.append(br[0])  
            elif ch == br[1]:
                if not acc or acc[-1] != br[0]:
                    return False  
                acc.pop()
    return len(acc) == 0  

assert is_valid('()')
assert is_valid('[]')
assert is_valid('{}')
assert is_valid('(text) [123] {___} ({[]})')    
assert is_valid('({[(())]})')    
assert is_valid('(sdfds{[sdf]sdfsd})')    
assert not is_valid('({[]}')    
assert not is_valid('(]')    
assert not is_valid('(')    
assert not is_valid('{{{{ ))))')  

print('Success!')