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

The PROV\_RSA\_SCHANNEL provider type supports both RSA and [*Schannel*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) protocols.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                                          |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)                                                                                                                                                                                                                                                                   |
| Signature    | RSA                                                                                                                                                                                                                                                                                                                           |
| Encryption   | Any PROV\_RSA\_SCHANNEL CSP must implement one or more of the following algorithms: [*RC4*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)<br/> [*DES*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx)<br/> [*Triple DES*](https://msdn.microsoft.com/en-us/library/ms721627(v=VS.85).aspx)<br/> |
| Hashing      | [*MD5*](https://msdn.microsoft.com/en-us/library/ms721594(v=VS.85).aspx)[*SHA*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx)<br/>                                                                                                                                                                                             |



 

 

 




