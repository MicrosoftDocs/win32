---
Description: The PROV\_DSS provider type, like PROV\_RSA\_SIG, only supports hashes and digital signatures. The signature algorithm specified by the PROV\_DSS provider type is the Digital Signature Algorithm (DSA).
ms.assetid: b3b00f10-8f94-4c30-8267-db0c449e4d15
title: PROV\_DSS
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_DSS

The PROV\_DSS provider type, like PROV\_RSA\_SIG, only supports [*hashes*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) and [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2). The signature algorithm specified by the PROV\_DSS provider type is the [*Digital Signature Algorithm*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (DSA).

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | None                                                                                                                              |
| Signature    | [*DSS*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2)                                                                       |
| Encryption   | None                                                                                                                              |
| Hashing      | [*MD5*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)[*SHA*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)<br/> |



 

## Related Documentation

The DSA was proposed by the [*National Institute of Standards and Technology*](https://msdn.microsoft.com/28d229ef-53ce-4d17-aba0-3bbf51e3ff0c) (NIST). A description of the algorithm can be found in the following government reference: "Proposed Federal Information Processing Standard for Digital Signature Standard (DSS)," Federal Register, v. 57, no. 21, 31 Jan 1992, pp. 3747-3749.

 

 




