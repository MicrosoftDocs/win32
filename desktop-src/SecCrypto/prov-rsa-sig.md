---
Description: A subset of PROV\_RSA\_FULL. It supports only those functions and algorithms required for hashes and digital signatures.
ms.assetid: ebb6192b-f34e-4218-a1e8-308708ae5935
title: PROV\_RSA\_SIG
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_SIG

The PROV\_RSA\_SIG provider type is a subset of PROV\_RSA\_FULL. It supports only those functions and algorithms required for [*hashes*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) and [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2).

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | None                                                                                                                              |
| Signature    | [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)                                                                       |
| Encryption   | None                                                                                                                              |
| Hashing      | [*MD5*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)[*SHA*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)<br/> |



 

## Related Documentation

The documentation for the [PROV\_RSA\_FULL](prov-rsa-full.md) provider type also applies to the PROV\_RSA\_SIG provider type.

 

 




