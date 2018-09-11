---
Description: The PROV\_DSS provider type, like PROV\_RSA\_SIG, only supports hashes and digital signatures. The signature algorithm specified by the PROV\_DSS provider type is the Digital Signature Algorithm (DSA).
ms.assetid: b3b00f10-8f94-4c30-8267-db0c449e4d15
title: PROV_DSS
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_DSS

The PROV\_DSS provider type, like PROV\_RSA\_SIG, only supports [*hashes*](https://msdn.microsoft.com/en-us/library/ms721586(v=VS.85).aspx) and [*digital signatures*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx). The signature algorithm specified by the PROV\_DSS provider type is the [*Digital Signature Algorithm*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx) (DSA).

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | None                                                                                                                              |
| Signature    | [*DSS*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx)                                                                       |
| Encryption   | None                                                                                                                              |
| Hashing      | [*MD5*](https://msdn.microsoft.com/en-us/library/ms721594(v=VS.85).aspx)[*SHA*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx)<br/> |



 

## Related Documentation

The DSA was proposed by the [*National Institute of Standards and Technology*](https://msdn.microsoft.com/en-us/library/ms721596(v=VS.85).aspx) (NIST). A description of the algorithm can be found in the following government reference: "Proposed Federal Information Processing Standard for Digital Signature Standard (DSS)," Federal Register, v. 57, no. 21, 31 Jan 1992, pp. 3747-3749.

 

 




