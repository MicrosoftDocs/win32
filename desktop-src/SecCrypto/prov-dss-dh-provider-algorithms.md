---
description: Algorithms supported by the Microsoft Base DSS and Diffie-Hellman Cryptographic Provider.
ms.assetid: 8db1c7cb-41e0-470b-b927-989da4c09324
title: PROV_DSS_DH Provider Algorithms
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_DSS\_DH Provider Algorithms

The following table lists the algorithms supported by the Microsoft Base DSS and Diffie-Hellman Cryptographic Provider.



| Algorithm ID      | Description                                 | Comments                                                                                                        |
|-------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| CALG\_MD5         | MD5 hashing algorithm.                      | Provided only for hashing.                                                                                      |
| CALG\_SHA         | SHA hashing algorithm.                      | Must be used for DSS signatures.                                                                                |
| CALG\_SHA1        | Same as CALG\_SHA.                          | No comment.                                                                                                     |
| CALG\_DSS\_SIGN   | DSS public/private key signature algorithm. | Key length: can be set, 512 bits to 1,024 bits in 64 bit increments. Default key length: 1,024 bits.<br/> |
| CALG\_DH\_SF      | Store and Forward D-H key exchange.         | Key length: can be set, 384 bits to 512 bits in 8 bit increments. Default key length: 512 bits.<br/>      |
| CALG\_DH\_EPHEM   | Ephemeral D-H key exchange.                 | Key length: can be set, 384 bits to 512 bits in 8 bit increments. Default key length: 512 bits.<br/>      |
| CALG\_CYLINK\_MEK | A 40-bit variant of a DES key.              | Key Length: 40 bits.                                                                                            |



 

 

 




