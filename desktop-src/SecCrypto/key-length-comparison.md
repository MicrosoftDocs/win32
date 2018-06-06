---
Description: The Microsoft Enhanced Cryptographic Provider provides an application with stronger security than currently available with the Microsoft Base Cryptographic Provider. Greater key length gives users more protection for sensitive data.
ms.assetid: cd16705c-c617-4843-a303-52d1019a60bb
title: Key Length Comparison
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Key Length Comparison

The Microsoft Enhanced Cryptographic Provider provides an application with stronger security than currently available with the Microsoft Base Cryptographic Provider. Greater key length gives users more protection for sensitive data.

The following table lists the default [*key lengths*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) supported by the Base Provider and the Enhanced Provider for standard algorithms.



| Algorithm                                                                                | Base Provider | Strong and Enhanced Providers |
|------------------------------------------------------------------------------------------|---------------|-------------------------------|
| RSA Key Exchange                                                                         | 512-bit       | 1,024-bit                     |
| RSA Signature                                                                            | 512-bit       | 1,024-bit                     |
| RC2                                                                                      | 40-bit        | 128-bit                       |
| RC4                                                                                      | 40-bit        | 128-bit                       |
| DES                                                                                      | Not supported | 56-bit                        |
| [*Triple DES*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f) (2-key) | Not supported | 112-bit                       |
| Triple DES (3-key)                                                                       | Not supported | 168-bit                       |



 

[*DES*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) and [*Triple DES*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f) algorithms are supported in the Enhanced Provider.

The Enhanced Provider is backward-compatible with the Base Provider distributed with earlier versions of CryptoAPI with the following exception. Both the base provider and the Enhanced Provider can only generate session keys of default key length. The default length of session keys for the Base Provider is 40 bits. The default key length for the Enhanced Provider is 128 bits. The Enhanced Provider cannot create keys with Base Provider-compatible key lengths. However, the Enhanced Provider can import key lengths of any size, up to 128 bits.

 

 



