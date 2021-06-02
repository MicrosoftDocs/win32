---
description: Algorithms might be supported by the Microsoft RSA/Schannel Cryptographic Provider.
ms.assetid: 8793f0e8-a368-42be-8351-c60d99c34fb9
title: RSA/Schannel Provider Algorithms
ms.topic: article
ms.date: 05/31/2018
---

# RSA/Schannel Provider Algorithms

The following algorithms might be supported by the Microsoft [*RSA*](../secgloss/r-gly.md)/[*Schannel*](../secgloss/s-gly.md) Cryptographic Provider.



| Algorithm ID    | Description                                                                                                                         | Comments                                                                                                        |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| CALG\_RSA\_KEYX | RSA public key [*key exchange algorithm*](../secgloss/k-gly.md) | Key length: Can be set, 384 bits to 16,384 bits in 8 bit increments. Default key length: 1,024 bits.<br/> |
| CALG\_MD5       | MD5 hashing algorithm.                                                                                                              | Provided only for hashing.                                                                                      |
| CALG\_SHA       | SHA hashing algorithm.                                                                                                              | Must be used for DSS signatures.                                                                                |
| CALG\_RC2       | RC2 block encryption algorithm.                                                                                                     | Key length: 40 to 88 bits                                                                                       |
| CALG\_RC4       | RC4 stream encryption algorithm.                                                                                                    | Key length: 40 to 88 bits                                                                                       |



 

 

 
