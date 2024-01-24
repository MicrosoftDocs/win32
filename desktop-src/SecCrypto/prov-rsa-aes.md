---
description: Supports both digital signatures and data encryption. It is considered a general purpose cryptographic service provider (CSP).
ms.assetid: da0b50ec-25a6-40dd-af83-73500b4a4c08
title: PROV_RSA_AES
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_AES

The PROV\_RSA\_AES provider type supports both [digital signatures](digital-signatures.md) and data encryption. It is considered a general purpose [*cryptographic service provider*](../secgloss/c-gly.md) (CSP). The RSA [*public key algorithm*](../secgloss/p-gly.md) is used for all [*public key*](../secgloss/p-gly.md) operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                       |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](../secgloss/r-gly.md)<br/>                                                                                                                                                                                                                                     |
| Signature    | [*RSA*](../secgloss/r-gly.md)<br/>                                                                                                                                                                                                                                     |
| Encryption   | [*RC2*](../secgloss/r-gly.md)<br/> [*RC4*](../secgloss/r-gly.md)<br/> [*Advanced Encryption Standard*](../secgloss/a-gly.md) (AES) <br/>                                                       |
| Hashing      | [*MD2*](../secgloss/m-gly.md)<br/> [*MD4*](../secgloss/m-gly.md)<br/> [*MD5*](../secgloss/m-gly.md)<br/> [*SHA-1*](../secgloss/s-gly.md)<br/> SHA-2 (SHA-256, SHA-384, and SHA-512)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   *Microsoft Cryptographic Service Provider Programmer's Guide*, Microsoft, 1996.
-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

> [!Note]  
> These resources may not be available in some languages and countries or regions.

 

 

 
