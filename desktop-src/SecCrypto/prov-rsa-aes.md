---
Description: Supports both digital signatures and data encryption. It is considered a general purpose cryptographic service provider (CSP).
ms.assetid: da0b50ec-25a6-40dd-af83-73500b4a4c08
title: PROV_RSA_AES
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_AES

The PROV\_RSA\_AES provider type supports both [digital signatures](digital-signatures.md) and data encryption. It is considered a general purpose [*cryptographic service provider*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSP). The RSA [*public key algorithm*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) is used for all [*public key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                       |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)<br/>                                                                                                                                                                                                                                     |
| Signature    | [*RSA*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)<br/>                                                                                                                                                                                                                                     |
| Encryption   | [*RC2*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)<br/> [*RC4*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)<br/> [*Advanced Encryption Standard*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx) (AES) <br/>                                                       |
| Hashing      | [*MD2*](https://msdn.microsoft.com/en-us/library/ms721594(v=VS.85).aspx)<br/> [*MD4*](https://msdn.microsoft.com/en-us/library/ms721594(v=VS.85).aspx)<br/> [*MD5*](https://msdn.microsoft.com/en-us/library/ms721594(v=VS.85).aspx)<br/> [*SHA-1*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx)<br/> SHA-2 (SHA-256, SHA-384, and SHA-512)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   *Microsoft Cryptographic Service Provider Programmer's Guide*, Microsoft, 1996.
-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

> [!Note]  
> These resources may not be available in some languages and countries or regions.

 

 

 




