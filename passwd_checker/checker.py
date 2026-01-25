
from pkg_resources import resource_filename
package = 'passwd_checker'

def seclist(password, level):
    if not password:
        raise Exception('Password was not given')

    if not level:
        raise Exception('Level was not given')

    if level not in [1, 2, 3, 4]:
        raise Exception('Level has to be between 1-4')

    if (level == 1):
        with open(resource_filename(package, 'data/common-credentials-1k.txt')) as seclist: 
            for line in seclist:
                if (line.strip() == password):
                    return True
            return False

    if (level == 2):
        with open(resource_filename(package, 'data/common-credentials-10k.txt')) as seclist: 
            for line in seclist:
                if (line.strip() == password):
                    return True
            return False

    if (level == 3):
        with open(resource_filename(package, 'data/common-credentials-100k.txt')) as seclist: 
            for line in seclist:
                if (line.strip() == password):
                    return True
            return False

    if (level == 4):
        with open(resource_filename(package, 'data/common-credentials-1M.txt')) as seclist: 
            for line in seclist:
                if (line.strip() == password):
                    return True
            return False
