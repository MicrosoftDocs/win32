---
Description: Encryption is the process of translating plain text data (plaintext) into something that appears to be random and meaningless (ciphertext). Decryption is the process of converting ciphertext back to plaintext.
ms.assetid: 6a4b5c82-f74c-4cc8-b824-690f165453bd
title: Data Encryption and Decryption
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Data Encryption and Decryption

Encryption is the process of translating plain text data ([*plaintext*](security.p_gly#-security-plaintext-gly)) into something that appears to be random and meaningless ([*ciphertext*](security.c_gly#-security-ciphertext-gly)). Decryption is the process of converting ciphertext back to plaintext.

To encrypt more than a small amount of data, [*symmetric encryption*](security.s_gly#-security-symmetric-encryption-gly) is used. A [*symmetric key*](security.s_gly#-security-symmetric-key-gly) is used during both the encryption and decryption processes. To decrypt a particular piece of ciphertext, the key that was used to encrypt the data must be used.

The goal of every encryption algorithm is to make it as difficult as possible to decrypt the generated ciphertext without using the key. If a really good encryption algorithm is used, there is no technique significantly better than methodically trying every possible key. For such an algorithm, the longer the key, the more difficult it is to decrypt a piece of ciphertext without possessing the key.

It is difficult to determine the quality of an encryption algorithm. Algorithms that look promising sometimes turn out to be very easy to break, given the proper attack. When selecting an encryption algorithm, it is a good idea to choose one that has been in use for several years and has successfully resisted all attacks.

For more information, see [Data Encryption and Decryption Functions](cryptography-functions.md#data-encryption-and-decryption-functions).

 

 



