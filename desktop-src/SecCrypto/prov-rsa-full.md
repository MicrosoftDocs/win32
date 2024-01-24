---
description: Supports both digital signatures and data encryption. It is considered a general purpose CSP.
ms.assetid: 44b13a96-aba2-4b77-8e66-416aa0bcb8ad
title: PROV_RSA_FULL
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_FULL

The PROV\_RSA\_FULL provider type supports both [*digital signatures*](../secgloss/d-gly.md) and data encryption. It is considered a general purpose CSP. The RSA public key algorithm is used for all public key operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](../secgloss/r-gly.md)                                                                       |
| Signature    | RSA                                                                                                                               |
| Encryption   | [*RC2*](../secgloss/r-gly.md)[*RC4*](../secgloss/r-gly.md)<br/> |
| Hashing      | [*MD5*](../secgloss/m-gly.md)[*SHA*](../secgloss/s-gly.md)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

 

 
