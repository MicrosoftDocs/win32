---
Description: The PROV\_DSS provider type, like PROV\_RSA\_SIG, only supports hashes and digital signatures. The signature algorithm specified by the PROV\_DSS provider type is the Digital Signature Algorithm (DSA).
ms.assetid: b3b00f10-8f94-4c30-8267-db0c449e4d15
title: PROV\_DSS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PROV\_DSS

The PROV\_DSS provider type, like PROV\_RSA\_SIG, only supports [*hashes*](security.h_gly#-security-hash-gly) and [*digital signatures*](security.d_gly#-security-digital-signature-gly). The signature algorithm specified by the PROV\_DSS provider type is the [*Digital Signature Algorithm*](security.d_gly#-security-digital-signature-algorithm-gly) (DSA).

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | None                                                                                                                              |
| Signature    | [*DSS*](security.d_gly#-security-dss-gly)                                                                       |
| Encryption   | None                                                                                                                              |
| Hashing      | [*MD5*](security.m_gly#-security-md5-gly)[*SHA*](security.s_gly#-security-sha-gly)<br/> |



 

## Related Documentation

The DSA was proposed by the [*National Institute of Standards and Technology*](security.n_gly#-security-national-institute-of-standards-and-technology-gly) (NIST). A description of the algorithm can be found in the following government reference: "Proposed Federal Information Processing Standard for Digital Signature Standard (DSS)," Federal Register, v. 57, no. 21, 31 Jan 1992, pp. 3747-3749.

 

 




