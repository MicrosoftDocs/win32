---
Description: Important  This API is deprecated.
ms.assetid: 4e6eb2df-a917-4533-b9f1-8da39598d0b8
title: Cryptographic Service Providers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Service Providers

> \[!Important\]  
> This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.

 

A [*cryptographic service provider*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CSP) contains implementations of cryptographic standards and algorithms. At a minimum, a CSP consists of a [*dynamic-link library*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (DLL) that implements the functions in [*CryptoSPI*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (a [*system program interface*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)). Most CSPs contain the implementation of all of their own functions. Some CSPs, however, implement their functions mainly in a Windows-based service program managed by the Windows service control manager. Others implement functions in hardware, such as a [*smart card*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) or secure coprocessor. If a CSP does not implement its own functions, the DLL acts as a pass-through layer, facilitating the communication between the operating system and the actual CSP implementation.

This section includes the following topics.



| Topic                                                                                      | Contents                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cryptographic Provider Types](cryptographic-provider-types.md)                           | Cryptographic provider types are families of cryptographic services providers that share data formats and cryptographic protocols. Data formats include algorithms [*padding*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) schemes, [*key lengths*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33), and default modes. |
| [Microsoft Cryptographic Service Providers](microsoft-cryptographic-service-providers.md) | Detailed information about CSPs currently available from Microsoft.                                                                                                                                                                                                                                                                                       |



 

 

 



