import string

from random import SystemRandom

try:
    import passlib.hash
    HAS_PASSLIB = True
    PASSLIB_VERSION = float(passlib.__version__[:3])
except Exception as e:
    HAS_PASSLIB = False

from ansible import errors


def grub2_hash(password, salt=None, iterations=10000):
    if salt is None:
        r = SystemRandom()
        salt = ''.join([r.choice(string.ascii_letters + string.digits) for _ in range(64)])

    # Make sure we have passlib and the correct version
    if not HAS_PASSLIB:
        raise errors.AnsibleFilterError('grub2_hash requires the passlib python module to generate password hashes')

    if PASSLIB_VERSION < 1.7:
        raise errors.AnsibleFilterError('grub2_hash >= 1.7 is required and %s is installed' % passlib.__version__)

    encrypted = passlib.hash.grub_pbkdf2_sha512.hash(password, salt=salt, rounds=iterations)
    return encrypted


class FilterModule(object):

    def filters(self):
        return {
            'grub2_hash': grub2_hash
        }
