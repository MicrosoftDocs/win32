---
description: A hash of a text or other string of bytes is an associated, statistically unique, fixed-length value.
ms.assetid: e54d5a3b-cae1-47dd-a565-7bf1ccef7f52
title: Data Hashes
ms.topic: article
ms.date: 05/31/2018
---

# Data Hashes

A [*hash*](../secgloss/h-gly.md) of a text or other string of bytes is an associated, statistically unique, fixed-length value. In some documents, a *hash* of a text is also called a digest; however, in this documentation the term hash will always be used. CryptoAPI functions provide a means to create a hash for any text or other string of bytes. That hash, then, can be used as a unique identifier of its associated data.

To ensure the [*integrity*](../secgloss/i-gly.md) of a text, a [*hash*](../secgloss/h-gly.md) of a text can be sent to accompany the text. The receiver can then compute a hash on the data received and compare the hash computed with the hash received. If the two match, the data received must be the same as the data from which the received hash was created.

To obtain a hash value, create a hash object using [**CryptCreateHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatehash). This object will accumulate the data to be verified. The data is then added to the hash object with the [**CryptHashData**](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashdata) function.

After the last block of data is added to the hash, the [**CryptGetHashParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgethashparam) function is used to obtain the hash value of the data.

Better security is provided by destroying the hash object with [**CryptDestroyHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroyhash) as soon as the hash value has been obtained.

 

 
