---
description: The purpose of the Diffie-Hellman algorithm is to make it possible for two or more hosts to create and share an identical, secret encryption key, by simply sharing information over a network that is not secure.
ms.assetid: f89a1268-e364-41ec-a6a8-1f6331dbb787
title: Diffie-Hellman/Schannel Provider Algorithms
ms.topic: article
ms.date: 05/31/2018
---

# Diffie-Hellman/Schannel Provider Algorithms

The purpose of the Diffie-Hellman algorithm is to make it possible for two or more hosts to create and share an identical, secret encryption key, by simply sharing information over a network that is not secure. The information that gets shared over the network is in the form of a couple of constant values, and a D-H public key.

The Microsoft [*Diffie-Hellman*](../secgloss/d-gly.md)/[*Schannel*](../secgloss/s-gly.md) Cryptographic Provider supports the following algorithms.



| Algorithm ID                  | Description                                                                                                                                           | Comments                                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| CALG\_DH\_SF                  | Diffie-Hellman store and forward [*key exchange algorithm*](../secgloss/k-gly.md) | Key length: Can be set, 384 bits to 512 bits in 8 bit increments. Default key length: 512 bits.<br/> |
| CALG\_MD5                     | MD5 hashing algorithm.                                                                                                                                | Provided only for hashing.                                                                                 |
| CALG\_DH\_EPHEM               | Ephemeral D-H key exchange.                                                                                                                           | Key length: Can be set, 384 bits to 512 bits in 8 bit increments. Default key length: 512 bits.<br/> |
| CALG\_SHA                     | SHA hashing algorithm.                                                                                                                                | Must be used for DSS signatures.                                                                           |
| CALG\_RC2                     | RC2 block encryption algorithm                                                                                                                        | Key length: 40 to 88 bits.                                                                                 |
| CALG\_RC4                     | RC4 stream encryption algorithm                                                                                                                       | Key length: 40 to 88 bits.                                                                                 |
| CALG\_CYLINK\_ MEK<br/> | DES variant encryption algorithm                                                                                                                      | Key length: 40 bits.                                                                                       |



 

 

 
