import crypt
from random import SystemRandom, shuffle
from passlib.hash import grub_pbkdf2_sha512
import string
try:
    import passlib.hash
    HAS_PASSLIB = True
except:
    HAS_PASSLIB = False

def grub2_hash(password, salt=None, iterations=10000):

    if salt is None:
        r = SystemRandom()
        salt = ''.join([r.choice(string.ascii_letters + string.digits) for _ in range(64)])

    if not HAS_PASSLIB:
        if sys.platform.startswith('darwin'):
            raise errors.AnsibleFilterError('|password_hash requires the passlib python module to generate password hashes on Mac OS X/Darwin')
        saltstring =  "$%s$%s" % (cryptmethod[hashtype],salt)
        encrypted = grub_pbkdf2_sha512.encrypt(password, salt=salt, rounds=iterations)
    else:
        encrypted = grub_pbkdf2_sha512.encrypt(password, salt=salt, rounds=iterations)

    return encrypted


class FilterModule(object):

    def filters(self):
        return {
            'grub2_hash': grub2_hash
        }




