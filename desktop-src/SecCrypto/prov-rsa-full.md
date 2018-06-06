---
Description: Supports both digital signatures and data encryption. It is considered a general purpose CSP.
ms.assetid: 44b13a96-aba2-4b77-8e66-416aa0bcb8ad
title: PROV\_RSA\_FULL
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_FULL

The PROV\_RSA\_FULL provider type supports both [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) and data encryption. It is considered a general purpose CSP. The RSA public key algorithm is used for all public key operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)                                                                       |
| Signature    | RSA                                                                                                                               |
| Encryption   | [*RC2*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)[*RC4*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)<br/> |
| Hashing      | [*MD5*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)[*SHA*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

 

 




