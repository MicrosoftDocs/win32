---
Description: A subset of PROV\_RSA\_FULL. It supports only those functions and algorithms required for hashes and digital signatures.
ms.assetid: ebb6192b-f34e-4218-a1e8-308708ae5935
title: PROV\_RSA\_SIG
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PROV\_RSA\_SIG

The PROV\_RSA\_SIG provider type is a subset of PROV\_RSA\_FULL. It supports only those functions and algorithms required for [*hashes*](security.h_gly#-security-hash-gly) and [*digital signatures*](security.d_gly#-security-digital-signature-gly).

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | None                                                                                                                              |
| Signature    | [*RSA*](security.r_gly#-security-rsa-gly)                                                                       |
| Encryption   | None                                                                                                                              |
| Hashing      | [*MD5*](security.m_gly#-security-md5-gly)[*SHA*](security.s_gly#-security-sha-gly)<br/> |



 

## Related Documentation

The documentation for the [PROV\_RSA\_FULL](prov-rsa-full.md) provider type also applies to the PROV\_RSA\_SIG provider type.

 

 




