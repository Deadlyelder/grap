#!/usr/bin/env python

from .rc4.RC4 import CRYPTO_STREAM_RC4

# Tuple of stream ciphers
CRYPTO_STREAM = (
#    RC4 deactivated (too many false positives)
#    CRYPTO_STREAM_RC4,
)
