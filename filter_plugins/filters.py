import crypt
import sys
from random import SystemRandom, shuffle
import string
try:
    import passlib.hash
    from passlib.hash import grub_pbkdf2_sha512
    HAS_PASSLIB = True
except:
    HAS_PASSLIB = False

def grub2_hash(password, hashtype='sha512', salt=None):

    cryptmethod = {
        'md5': '1',
        'blowfish': '2a',
        'sha256': '5',
        'sha512': '6',
    }

    if salt is None:
        r = SystemRandom()
        salt = ''.join([r.choice(string.ascii_letters + string.digits) for _ in range(64)])

    if not HAS_PASSLIB:
        if sys.platform.startswith('darwin'):
            raise errors.AnsibleFilterError('|password_hash requires the passlib python module to generate password hashes on Mac OS X/Darwin')
        saltstring =  "$%s$%s" % (cryptmethod[hashtype],salt)
        encrypted = crypt.crypt(password, salt=salt)
    else:
        encrypted = grub_pbkdf2_sha512.hash(password)

    return encrypted


class FilterModule(object):

    def filters(self):
        return {
            'grub2_hash': grub2_hash
        }




