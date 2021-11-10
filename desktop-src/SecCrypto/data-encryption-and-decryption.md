---
title: Data encryption and decryption
description: Encryption is the process of translating plain text data (plaintext) into something that appears to be random and meaningless (ciphertext). Decryption is the process of converting ciphertext back to plaintext.
ms.assetid: 6a4b5c82-f74c-4cc8-b824-690f165453bd
ms.topic: article
ms.date: 11/09/2021
---

# Data encryption and decryption

Encryption is the process of translating plain text data ([*plaintext*](../secgloss/p-gly.md)) into something that appears to be random and meaningless ([*ciphertext*](../secgloss/c-gly.md)). Decryption is the process of converting ciphertext back to plaintext.

To encrypt more than a small amount of data, [*symmetric encryption*](../secgloss/s-gly.md) is used. A [*symmetric key*](../secgloss/s-gly.md) is used during both the encryption and decryption processes. To decrypt a particular piece of ciphertext, the key that was used to encrypt the data must be used.

The goal of every encryption algorithm is to make it as difficult as possible to decrypt the generated ciphertext without using the key. If a really good encryption algorithm is used, then there's no technique significantly better than methodically trying every possible key. For such an algorithm, the longer the key, the more difficult it is to decrypt a piece of ciphertext without possessing the key.

It's difficult to determine the quality of an encryption algorithm. Algorithms that look promising sometimes turn out to be very easy to break, given the proper attack. When selecting an encryption algorithm, it's a good idea to choose one that's been in use for several years, and has successfully resisted all attacks.

For more information, see [Data encryption and decryption functions](cryptography-functions.md).
