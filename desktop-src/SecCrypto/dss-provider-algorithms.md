---
description: The following table lists the algorithms supported by the Microsoft DSS Cryptographic Provider.
ms.assetid: 2a7aecf8-e242-4087-83ee-aaa637a9ec71
title: DSS Provider Algorithms
ms.topic: article
ms.date: 05/31/2018
---

# DSS Provider Algorithms

The following table lists the algorithms supported by the Microsoft DSS Cryptographic Provider.



| Algorithm ID    | Description                                 | Comments                                                                                                        |
|-----------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| CALG\_MD5       | MD5 hashing algorithm.                      | Provided only for hashing.                                                                                      |
| CALG\_SHA       | SHA hashing algorithm.                      | Must be used for DSS signatures.                                                                                |
| CALG\_SHA1      | Same as CALG\_SHA.                          | No comment.                                                                                                     |
| CALG\_DSS\_SIGN | DSS public/private key signature algorithm. | Key length: can be set, 512 bits to 1,024 bits in 64 bit increments. Default key length: 1,024 bits.<br/> |



 

 

 




