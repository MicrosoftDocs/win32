---
description: Is the Windows module that performs interactive logon for a logon session. Winlogon behavior can be customized by implementing and registering a Credential Provider.
ms.assetid: 6721367b-e200-4297-897b-4772226203b0
title: Winlogon and Credential Providers
ms.topic: article
ms.date: 05/31/2018
---

# Winlogon and Credential Providers

[*Winlogon*](../secgloss/w-gly.md) is the Windows module that performs interactive logon for a [*logon session*](../secgloss/l-gly.md). Winlogon behavior can be customized by implementing and registering a Credential Provider.

For information about implementing a Credential Provider, see the following topics.



| Topic                                                                                                           | Description                                                                                            |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [Credential Provider driven Windows Logon Experience](https://go.microsoft.com/fwlink/?LinkId=717287)<br/> | Overview of Winlogon and Credential Provider architecture and a sample Credential Provider.<br/> |
| [Shell Interfaces](../shell/samples-usingthumbnailproviders.md)<br/>                                                                | Credential Provider interface reference.<br/>                                                    |
| [Credential Providers in Windows 10](credential-providers-in-windows.md)<br/>                            | Third-party credential providers and system credential providers in Windows 10.<br/>             |



 

For a sample Credential Provider implementation, see the sample located in the Windows SDK installation directory under \\Samples\\Security\\CredentialProvider.

**Windows Server 2003 and Windows XP:** Credential Providers are not supported. For information about customizing Winlogon, see [Winlogon and GINA](winlogon-and-gina.md).

 

 
