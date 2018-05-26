---
Description: Supports both digital signatures and data encryption. It is considered a general purpose cryptographic service provider (CSP).
ms.assetid: da0b50ec-25a6-40dd-af83-73500b4a4c08
title: PROV\_RSA\_AES
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PROV\_RSA\_AES

The PROV\_RSA\_AES provider type supports both [digital signatures](digital-signatures.md) and data encryption. It is considered a general purpose [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP). The RSA [*public key algorithm*](security.p_gly#-security-public-key-algorithm-gly) is used for all [*public key*](security.p_gly#-security-public-key-gly) operations.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                       |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](security.r_gly#-security-rsa-gly)<br/>                                                                                                                                                                                                                                     |
| Signature    | [*RSA*](security.r_gly#-security-rsa-gly)<br/>                                                                                                                                                                                                                                     |
| Encryption   | [*RC2*](security.r_gly#-security-rc2-gly)<br/> [*RC4*](security.r_gly#-security-rc4-gly)<br/> [*Advanced Encryption Standard*](security.a_gly#-security-aes-gly) (AES) <br/>                                                       |
| Hashing      | [*MD2*](security.m_gly#-security-md2-gly)<br/> [*MD4*](security.m_gly)<br/> [*MD5*](security.m_gly#-security-md5-gly)<br/> [*SHA-1*](security.s_gly#-security-sha-gly)<br/> SHA-2 (SHA-256, SHA-384, and SHA-512)<br/> |



 

## Related Documentation

This provider type is defined by Microsoft and RSA Data Security. It is described in the following documents:

-   *Microsoft Cryptographic Service Provider Programmer's Guide*, Microsoft, 1996.
-   RSA Laboratories, Public Key Cryptography Standards, RSA Data Security, November 1993.

> [!Note]  
> These resources may not be available in some languages and countries or regions.

 

 

 




