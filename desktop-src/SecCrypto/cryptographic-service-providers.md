---
description: Important  This API is deprecated.
ms.assetid: 4e6eb2df-a917-4533-b9f1-8da39598d0b8
title: Cryptographic Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Service Providers

> [!IMPORTANT]
> This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](/windows/desktop/SecCNG/cng-portal) Microsoft may remove this API in future releases.

 

A [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) contains implementations of cryptographic standards and algorithms. At a minimum, a CSP consists of a [*dynamic-link library*](../secgloss/d-gly.md) (DLL) that implements the functions in [*CryptoSPI*](../secgloss/c-gly.md) (a [*system program interface*](../secgloss/s-gly.md)). Most CSPs contain the implementation of all of their own functions. Some CSPs, however, implement their functions mainly in a Windows-based service program managed by the Windows service control manager. Others implement functions in hardware, such as a [*smart card*](../secgloss/s-gly.md) or secure coprocessor. If a CSP does not implement its own functions, the DLL acts as a pass-through layer, facilitating the communication between the operating system and the actual CSP implementation.

This section includes the following topics.



| Topic                                                                                      | Contents                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cryptographic Provider Types](cryptographic-provider-types.md)                           | Cryptographic provider types are families of cryptographic services providers that share data formats and cryptographic protocols. Data formats include algorithms [*padding*](../secgloss/p-gly.md) schemes, [*key lengths*](../secgloss/k-gly.md), and default modes. |
| [Microsoft Cryptographic Service Providers](microsoft-cryptographic-service-providers.md) | Detailed information about CSPs currently available from Microsoft.                                                                                                                                                                                                                                                                                       |



 

 

 
