---
description: The Microsoft Enhanced Cryptographic Provider supports the following algorithms.
ms.assetid: d58bcd99-c54b-4fda-9fe1-e10a66707d81
title: Enhanced Provider Algorithms
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Provider Algorithms

The [Microsoft Enhanced Cryptographic Provider](microsoft-enhanced-cryptographic-provider.md) supports the following algorithms.



| Algorithm ID       | Description                                                                                                                                                     | Comments                                                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CALG\_3DES         | Triple DES.                                                                                                                                                     | Key length: 168 bits.Default mode: Cipher block chaining.<br/> Block size: 64 bits.<br/> No salt allowed.<br/>                           |
| CALG\_3DES\_112    | Two-key [*triple DES*](../secgloss/t-gly.md) encryption.                                                            | Key length: 112 bits.Default mode: Cipher block chaining.<br/> Block size: 64 bits.<br/> No salt allowed.<br/>                           |
| CALG\_DES          | DES encryption.                                                                                                                                                 | Key length: 56 bits.Default mode: Cipher block chaining.<br/> Block size: 64 bits.<br/> No salt allowed.<br/>                            |
| CALG\_HMAC         | MAC keyed-hash algorithm.                                                                                                                                       | HMAC computation.                                                                                                                                          |
| CALG\_MAC          | [*Message Authentication Code*](../secgloss/m-gly.md) (MAC) keyed hash algorithm. | Block cipher MAC.                                                                                                                                          |
| CALG\_MD2          | MD2 hashing algorithm.                                                                                                                                          | For more information, see [*MD2 algorithm*](../secgloss/m-gly.md).                                       |
| CALG\_MD5          | MD5 hashing algorithm.                                                                                                                                          | For more information, see [*MD5 algorithm*](../secgloss/m-gly.md).                                       |
| CALG\_RC2          | RC2 block encryption algorithm.                                                                                                                                 | Key length: 128 bits.Default mode: Cipher block chaining.<br/> Block size: 64 bits.<br/> Salt length: Can be set.<br/>                   |
| CALG\_RC4          | RC4 stream encryption algorithm.                                                                                                                                | Key length: 128 bits.Salt length: Can be set.<br/>                                                                                                   |
| CALG\_RSA\_KEYX    | RSA public key exchange algorithm.                                                                                                                              | Key length: Can be set, 384 bits to 16,384 bits in 8-bit increments. Default key length: 1,024 bits.<br/>                                            |
| CALG\_RSA\_SIGN    | RSA public key signature algorithm.                                                                                                                             | Key length: Can be set, 384 bits to 16,384 bits in 8-bit increments. Default key length: 1,024 bits.<br/> Signature conforms to PKCS \#6.<br/> |
| CALG\_SHA          | SHA hashing algorithm.                                                                                                                                          | For more information, see [*Secure Hash Algorithm*](../secgloss/s-gly.md).               |
| CALG\_SHA1         | Same as CALG\_SHA.                                                                                                                                              | For more information, see [*Secure Hash Algorithm*](../secgloss/s-gly.md).               |
| CALG\_SSL3\_SHAMD5 | SSL3 client authentication algorithm.                                                                                                                           | For more information, see [Creating a CALG\_SSL3\_SHAMD5 Hash](creating-a-calg-ssl3-shamd5-hash.md).                                                      |



 

 

 
