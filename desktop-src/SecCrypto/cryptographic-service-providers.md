---
Description: 'Important  This API is deprecated.'
ms.assetid: '4e6eb2df-a917-4533-b9f1-8da39598d0b8'
title: Cryptographic Service Providers
---

# Cryptographic Service Providers

> \[!Important\]  
> This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.

 

A [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) contains implementations of cryptographic standards and algorithms. At a minimum, a CSP consists of a [*dynamic-link library*](security.d_gly#-security-dynamic-link-library-gly) (DLL) that implements the functions in [*CryptoSPI*](security.c_gly#-security-cryptospi-gly) (a [*system program interface*](security.s_gly#-security-system-program-interface-gly)). Most CSPs contain the implementation of all of their own functions. Some CSPs, however, implement their functions mainly in a Windows-based service program managed by the Windows service control manager. Others implement functions in hardware, such as a [*smart card*](security.s_gly#-security-smart-card-gly) or secure coprocessor. If a CSP does not implement its own functions, the DLL acts as a pass-through layer, facilitating the communication between the operating system and the actual CSP implementation.

This section includes the following topics.



| Topic                                                                                      | Contents                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cryptographic Provider Types](cryptographic-provider-types.md)                           | Cryptographic provider types are families of cryptographic services providers that share data formats and cryptographic protocols. Data formats include algorithms [*padding*](security.p_gly#-security-padding-gly) schemes, [*key lengths*](security.k_gly#-security-key-length-gly), and default modes. |
| [Microsoft Cryptographic Service Providers](microsoft-cryptographic-service-providers.md) | Detailed information about CSPs currently available from Microsoft.                                                                                                                                                                                                                                                                                       |



 

 

 



