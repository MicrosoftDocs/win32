---
description: The Microsoft Base Cryptographic Provider supports the following algorithms.
ms.assetid: 767d5192-6e8f-488a-b954-29d56488ccbb
title: Base Provider Algorithms
ms.topic: article
ms.date: 05/31/2018
---

# Base Provider Algorithms

The Microsoft Base Cryptographic Provider supports the following algorithms.



| Algorithm ID                  | Description                                                                                                                                                               | Comments                                                                                                                                                                |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CALG\_MD2<br/>          | MD2 hashing algorithm<br/>                                                                                                                                          | For more information, see [*MD2 algorithm*](../secgloss/m-gly.md).<br/>                                         |
| CALG\_MD5<br/>          | MD5 hashing algorithm<br/>                                                                                                                                          | For more information, see [*MD5 algorithm*](../secgloss/m-gly.md).<br/>                                         |
| CALG\_SHA<br/>          | SHA hashing algorithm<br/>                                                                                                                                          | For more information, see [*Secure Hash Algorithm*](../secgloss/s-gly.md).<br/>                 |
| CALG\_SHA1<br/>         | Same as CALG\_SHA<br/>                                                                                                                                              | For more information, see [*Secure Hash Algorithm*](../secgloss/s-gly.md).<br/>                 |
| CALG\_MAC<br/>          | [*Message Authentication Code*](../secgloss/m-gly.md) (MAC) keyed-hash algorithm<br/> | Block cipher MAC.<br/>                                                                                                                                            |
| CALG\_HMAC<br/>         | MAC keyed-hash algorithm<br/>                                                                                                                                       | HMAC computation.<br/>                                                                                                                                            |
| CALG\_SSL3\_SHAMD5<br/> | SLL3 client authentication algorithm<br/>                                                                                                                           | For more information, see [Creating a CALG\_SSL3\_SHAMD5 Hash](creating-a-calg-ssl3-shamd5-hash.md).<br/>                                                        |
| CALG\_RSA\_SIGN<br/>    | RSA public key signature algorithm<br/>                                                                                                                             | Key length: can be set from 384 bits to 16,384 bits in 8-bit increments.<br/> Default key length: 512 bits.<br/> Signature conforms to PKCS \#6.<br/> |
| CALG\_RSA\_KEYX<br/>    | RSA public key exchange algorithm<br/>                                                                                                                              | Key length: can be set from 384 bits to 1024 bits in 8-bit increments.<br/> Default key length: 512 bits.<br/>                                              |
| CALG\_RC2<br/>          | RC2 block encryption algorithm<br/>                                                                                                                                 | Key length: 40 bits.<br/> Default mode: Cipher block chaining.<br/> Block size: 64 bits.<br/> Salt length: 88 bits.<br/>                        |
| CALG\_RC4<br/>          | RC4 stream encryption algorithm<br/>                                                                                                                                | Key length: 40 bits.<br/> Salt length: 88 bits.<br/>                                                                                                        |
| CALG\_DES<br/>          | DES encryption<br/>                                                                                                                                                 | For more information, see [*Data Encryption Standard*](../secgloss/d-gly.md) (DES).<br/>  |



 

 

 
