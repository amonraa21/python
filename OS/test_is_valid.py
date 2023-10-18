from is_valid import is_valid

        
def test_is_valid():
    assert is_valid('()')
    assert is_valid('[]')
    assert is_valid('{}')
    assert is_valid('(text) [123] {___} ({[]})')    
    assert is_valid('({[(())]})')    
    assert is_valid('(sdfds{[sdf]sdfsd})')   
    
def test_is_not_valid():
    assert not is_valid('({[]}')    
    assert not is_valid('(]')    
    assert not is_valid('(')    
    assert not is_valid('{{{{ ))))')  