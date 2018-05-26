---
Description: Supports both digital signatures and data encryption. It is considered a general purpose CSP.
ms.assetid: 44b13a96-aba2-4b77-8e66-416aa0bcb8ad
title: PROV\_RSA\_FULL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PROV\_RSA\_FULL

The PROV\_RSA\_FULL provider type supports both [*digital signatures*](security.d_gly#-security-digital-signature-gly) and data encryption. It is considered a general purpose CSP. The RSA public key algorithm is used for all public key operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](security.r_gly#-security-rsa-gly)                                                                       |
| Signature    | RSA                                                                                                                               |
| Encryption   | [*RC2*](security.r_gly#-security-rc2-gly)[*RC4*](security.r_gly#-security-rc4-gly)<br/> |
| Hashing      | [*MD5*](security.m_gly#-security-md5-gly)[*SHA*](security.s_gly#-security-sha-gly)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

 

 




