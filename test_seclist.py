
import passwd_checker.checker as checker

def test_seclist_1_is_common():
    isCommon = checker.seclist('freepass', 1)
    assert isCommon == True, 'Should be True'

def test_seclist_1_not_common():
    isCommon = checker.seclist('th1sPassw0rdIsN0tC0mm0n', 1)
    assert isCommon == False, 'Should be False'

def test_seclist_2_is_common():
    isCommon = checker.seclist('mutant', 2)
    assert isCommon == True, 'Should be True'

def test_seclist_2_not_common():
    isCommon = checker.seclist('th1sPassw0rdIsN0tC0mm0n', 2)
    assert isCommon == False, 'Should be False'

def test_seclist_3_is_common():
    isCommon = checker.seclist('tecum', 3)
    assert isCommon == True, 'Should be True'

def test_seclist_3_not_common():
    isCommon = checker.seclist('th1sPassw0rdIsN0tC0mm0n', 3)
    assert isCommon == False, 'Should be False'

def test_seclist_4_is_common():
    isCommon = checker.seclist('wh@tever0', 4)
    assert isCommon == True, 'Should be True'

def test_seclist_4_not_common():
    isCommon = checker.seclist('th1sPassw0rdIsN0tC0mm0n', 4)
    assert isCommon == False, 'Should be False'

if __name__ == '__main__':
    test_seclist_1_is_common()
    test_seclist_1_not_common()
    test_seclist_2_is_common()
    test_seclist_2_not_common()
    test_seclist_3_is_common()
    test_seclist_3_not_common()
    test_seclist_4_is_common()
    test_seclist_4_not_common()
    print('All tests passed')
