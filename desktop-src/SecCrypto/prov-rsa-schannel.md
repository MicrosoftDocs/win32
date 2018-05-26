---
Description: Supports both RSA and Schannel protocols.
ms.assetid: f0c11a04-7931-424a-b085-0cc584ea7bb7
title: PROV\_RSA\_SCHANNEL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PROV\_RSA\_SCHANNEL

The PROV\_RSA\_SCHANNEL provider type supports both RSA and [*Schannel*](security.s_gly#-security-schannel-gly) protocols.

## Algorithms Supported

For descriptions of each of these algorithms, see the glossary.



| Purpose      | Supported algorithms                                                                                                                                                                                                                                                                                                          |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Exchange | [*RSA*](security.r_gly#-security-rsa-gly)                                                                                                                                                                                                                                                                   |
| Signature    | RSA                                                                                                                                                                                                                                                                                                                           |
| Encryption   | Any PROV\_RSA\_SCHANNEL CSP must implement one or more of the following algorithms: [*RC4*](security.r_gly#-security-rc4-gly)<br/> [*DES*](security.d_gly#-security-des-gly)<br/> [*Triple DES*](security.t_gly#-security-triple-des-gly)<br/> |
| Hashing      | [*MD5*](security.m_gly#-security-md5-gly)[*SHA*](security.s_gly#-security-sha-gly)<br/>                                                                                                                                                                                             |



 

 

 




