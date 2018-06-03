---
Description: The following algorithms compute hashes and digital signatures. Each of these algorithms is supported in the Microsoft Base, Strong, and Enhanced Cryptographic Providers.
ms.assetid: 91bf898d-658a-4e45-aa6e-eded46657563
title: Hash and Signature Algorithms
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Hash and Signature Algorithms

The following algorithms compute [*hashes*](https://www.bing.com/search?q=*hashes*) and [*digital signatures*](https://www.bing.com/search?q=*digital signatures*). Each of these algorithms is supported in the Microsoft Base, Strong, and Enhanced Cryptographic Providers. Internal details of these algorithms are beyond the scope of this documentation. For a list of additional sources, refer to [Additional Documentation on Cryptography](additional-documentation-on-cryptography.md).



| Algorithms                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cipher Block Chaining (CBC) MAC<br/>     | One of the algorithms (CALG\_MAC) implemented by Microsoft providers is a [*block cipher*](https://www.bing.com/search?q=*block cipher*) [*Message Authentication Code*](https://www.bing.com/search?q=*Message Authentication Code*) (MAC). This method encrypts the base data with a block cipher and then uses the last encrypted block as the [*hash*](https://www.bing.com/search?q=*hash*) value. The encryption algorithm used to build the MAC is the one that was specified when the session key was created. <br/>                                                                            |
| HMAC<br/>                                | An algorithm (CALG\_HMAC) implemented by Microsoft providers. This algorithm also uses a [*symmetric key*](https://www.bing.com/search?q=*symmetric key*) to create the [*hash*](https://www.bing.com/search?q=*hash*), but is more complex than the simple [*Cipher Block Chaining*](https://www.bing.com/search?q=*Cipher Block Chaining*) (CBC) MAC algorithm. It can be used with any iterated cryptographic hash algorithm, such as MD5 or SHA-1. For details, see [Creating an HMAC](creating-an-hmac.md).<br/>                                                                                       |
| MD2, MD4, and MD5<br/>                   | These hashing algorithms were all developed by RSA Data Security, Inc. These algorithms were developed in sequential order. All three generate 128-bit hash values. All three are known to have weaknesses and should only be used where needed for compatibility purposes. For new code, we recommend the SHA-2 family of hashes.<br/> These algorithms are well known and can be reviewed in detail in any reference on [*cryptography*](https://www.bing.com/search?q=*cryptography*).<br/>                                                                                                                                                           |
| Message Authentication Code (MAC)<br/>   | MAC algorithms are similar to [*hash*](https://www.bing.com/search?q=*hash*) algorithms, but are computed by using a [*symmetric*](https://www.bing.com/search?q=*symmetric*) (session) key. The original [*session key*](https://www.bing.com/search?q=*session key*) is required to recompute the hash value. The recomputed hash value is used to verify that the base data was not changed. These algorithms are sometimes called keyed-hash algorithms. To see which Microsoft providers support MAC, see [Microsoft Cryptographic Service Providers](microsoft-cryptographic-service-providers.md).<br/>    |
| Secure Hash Algorithm (SHA-1)<br/>       | This hashing algorithm was developed by the [*National Institute of Standards and Technology*](https://www.bing.com/search?q=*National Institute of Standards and Technology*) (NIST) and by the National Security Agency (NSA). This algorithm was developed for use with DSA (Digital Signature Algorithm) or DSS (Digital Signature Standard). This algorithm generates a 160-bit [*hash*](https://www.bing.com/search?q=*hash*) value. SHA-1 is known to have weaknesses, and should only be used where required for compatibility purposes. For new code, we recommend the SHA-2 family of hashes.<br/> |
| Secure Hash Algorithm - 2 (SHA-2)<br/>   | This hashing algorithm was developed as a successor to SHA-1 by the [*National Institute of Standards and Technology*](https://www.bing.com/search?q=*National Institute of Standards and Technology*) (NIST) and the National Security Agency (NSA). It has four variants—SHA-224, SHA-256, SHA-384, and SHA-512—which are named according to the number of bits in their outputs. Of these, SHA-256, SHA-384, and SHA-512 are implemented in the Microsoft AES Cryptographic Provider.<br/>                                                                                                                                |
| SSL3 Client Authorization Algorithm<br/> | This algorithm is used for SSL3 client authentication. In the SSL3 protocol, a concatenation of an MD5 hash and a SHA hash is signed with an RSA [*private key*](https://www.bing.com/search?q=*private key*). CryptoAPI 2.0 and the Microsoft Base and Enhanced Cryptographic Providers support this with the [*hash*](https://www.bing.com/search?q=*hash*) type CALG\_SSL3\_SHAMD5. For more information, see [Creating a CALG\_SSL3\_SHAMD5 Hash](creating-a-calg-ssl3-shamd5-hash.md).<br/>                                                                                                                                               |



 

 

 




