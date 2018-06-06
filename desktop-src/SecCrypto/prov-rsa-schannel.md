---
Description: Supports both RSA and Schannel protocols.
ms.assetid: f0c11a04-7931-424a-b085-0cc584ea7bb7
title: PROV\_RSA\_SCHANNEL
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PROV\_RSA\_SCHANNEL

The PROV\_RSA\_SCHANNEL provider type supports both RSA and [*Schannel*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) protocols.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                                          |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)                                                                                                                                                                                                                                                                   |
| Signature    | RSA                                                                                                                                                                                                                                                                                                                           |
| Encryption   | Any PROV\_RSA\_SCHANNEL CSP must implement one or more of the following algorithms: [*RC4*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd)<br/> [*DES*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2)<br/> [*Triple DES*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f)<br/> |
| Hashing      | [*MD5*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)[*SHA*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)<br/>                                                                                                                                                                                             |



 

 

 




