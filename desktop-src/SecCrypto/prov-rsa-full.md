---
Description: Supports both digital signatures and data encryption. It is considered a general purpose CSP.
ms.assetid: 44b13a96-aba2-4b77-8e66-416aa0bcb8ad
title: PROV_RSA_FULL
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_FULL

The PROV\_RSA\_FULL provider type supports both [*digital signatures*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx) and data encryption. It is considered a general purpose CSP. The RSA public key algorithm is used for all public key operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)                                                                       |
| Signature    | RSA                                                                                                                               |
| Encryption   | [*RC2*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)[*RC4*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)<br/> |
| Hashing      | [*MD5*](https://msdn.microsoft.com/en-us/library/ms721594(v=VS.85).aspx)[*SHA*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

 

 




