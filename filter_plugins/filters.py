import string

from random import SystemRandom

try:
    import passlib.hash
    HAS_PASSLIB = True
except Exception as e:
    HAS_PASSLIB = False

from ansible import errors


def grub2_hash(password, salt=None, iterations=10000):
    if salt is None:
        r = SystemRandom()
        salt = ''.join([r.choice(string.ascii_letters + string.digits) for _ in range(64)])

    if not HAS_PASSLIB:
        raise errors.AnsibleFilterError('grub2_hash requires the passlib python module to generate password hashes')
    else:
        encrypted = passlib.hash.grub_pbkdf2_sha512.hash(password, salt=salt, rounds=iterations)

    return encrypted


class FilterModule(object):

    def filters(self):
        return {
            'grub2_hash': grub2_hash
        }




