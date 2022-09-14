---
description: The Microsoft Enhanced Cryptographic Provider supports the same capabilities as the Microsoft Base Cryptographic Provider, but supports stronger security through longer keys and additional algorithms.
ms.assetid: 87d0c865-8b29-439c-81aa-a40dc0034e3b
title: Microsoft Enhanced Cryptographic Provider
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Enhanced Cryptographic Provider

The Microsoft Enhanced Cryptographic Provider, called the Enhanced Provider, supports the same capabilities as the Microsoft Base Cryptographic Provider, called the Base Provider. The Enhanced Provider supports stronger security through longer keys and additional algorithms. It can be used with all versions of CryptoAPI.

To maintain backward compatibility with earlier provider versions, the provider name, as defined in the Wincrypt.h header file, retains the version 1.0 designation. However, version 2.0 of this provider is currently shipping. To determine the version of the provider in use, call [**CryptGetProvParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetprovparam) with the *dwParam* argument set to **PP\_VERSION**. Version 2.0 is in use if 0x0200 is returned.

|                   | Value               |
|-------------------|---------------------|
| **Provider type** | PROV\_RSA\_FULL     |
| **Provider name** | MS\_ENHANCED\_PROV  |



 

The following table highlights differences between the Base Provider, Strong Provider, and Enhanced Provider. The key lengths shown are the default key lengths.



| Algorithm                                                                                | Base Provider key length | Strong Provider key length | Enhanced Provider key length                |
|------------------------------------------------------------------------------------------|--------------------------|----------------------------|---------------------------------------------|
| RSA public key signature algorithm                                                       | 512 bits                 | 1,024 bits                 | 1,024 bits                                  |
| RSA public key exchange algorithm                                                        | 512 bits                 | 1,024 bits                 | 1,024 bits                                  |
| RC2 block encryption algorithm                                                           | 40 bits                  | 128 bits                   | 128 bits Salt length can be set.<br/> |
| RC4 stream encryption algorithm                                                          | 40 bits                  | 128 bits                   | 128 bits Salt length can be set.<br/> |
| DES                                                                                      | 56 bits                  | 56 bits                    | 56 bits                                     |
| [*Triple DES*](../secgloss/t-gly.md) (2 key) | Not supported            | 112 bits                   | 112 bits                                    |
| Triple DES (3 key)                                                                       | Not supported            | 168 bits                   | 168 bits                                    |



 

The Strong Provider and the Enhanced Provider are backward-compatible with the Base Provider except that the providers can only generate RC2 or RC4 keys of default [*key length*](../secgloss/k-gly.md). The default length for the Base Provider is 40 bits. The default length for the Enhanced Provider is 128 bits. Thus the Enhanced Provider cannot create keys with Base Provider-compatible key lengths. However, the Enhanced Provider can import RC2 and RC4 keys of up to 128 bits. Therefore, the Enhanced Provider can import and use 40 bit keys generated using the Base Provider.

 

 
