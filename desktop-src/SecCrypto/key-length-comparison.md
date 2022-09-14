---
description: The Microsoft Enhanced Cryptographic Provider provides an application with stronger security than currently available with the Microsoft Base Cryptographic Provider. Greater key length gives users more protection for sensitive data.
ms.assetid: cd16705c-c617-4843-a303-52d1019a60bb
title: Key Length Comparison
ms.topic: article
ms.date: 05/31/2018
---

# Key Length Comparison

The Microsoft Enhanced Cryptographic Provider provides an application with stronger security than currently available with the Microsoft Base Cryptographic Provider. Greater key length gives users more protection for sensitive data.

The following table lists the default [*key lengths*](../secgloss/k-gly.md) supported by the Base Provider and the Enhanced Provider for standard algorithms.



| Algorithm                                                                                | Base Provider | Strong and Enhanced Providers |
|------------------------------------------------------------------------------------------|---------------|-------------------------------|
| RSA Key Exchange                                                                         | 512-bit       | 1,024-bit                     |
| RSA Signature                                                                            | 512-bit       | 1,024-bit                     |
| RC2                                                                                      | 40-bit        | 128-bit                       |
| RC4                                                                                      | 40-bit        | 128-bit                       |
| DES                                                                                      | Not supported | 56-bit                        |
| [*Triple DES*](../secgloss/t-gly.md) (2-key) | Not supported | 112-bit                       |
| Triple DES (3-key)                                                                       | Not supported | 168-bit                       |



 

[*DES*](../secgloss/d-gly.md) and [*Triple DES*](../secgloss/t-gly.md) algorithms are supported in the Enhanced Provider.

The Enhanced Provider is backward-compatible with the Base Provider distributed with earlier versions of CryptoAPI with the following exception. Both the base provider and the Enhanced Provider can only generate session keys of default key length. The default length of session keys for the Base Provider is 40 bits. The default key length for the Enhanced Provider is 128 bits. The Enhanced Provider cannot create keys with Base Provider-compatible key lengths. However, the Enhanced Provider can import key lengths of any size, up to 128 bits.

 

 
