---
Description: Is the Windows module that performs interactive logon for a logon session. Winlogon behavior can be customized by implementing and registering a Credential Provider.
ms.assetid: 6721367b-e200-4297-897b-4772226203b0
title: Winlogon and Credential Providers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Winlogon and Credential Providers

[*Winlogon*](https://msdn.microsoft.com/031c898b-3b4d-4b29-811a-112da37b5e3d) is the Windows module that performs interactive logon for a [*logon session*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f). Winlogon behavior can be customized by implementing and registering a Credential Provider.

For information about implementing a Credential Provider, see the following topics.



| Topic                                                                                                           | Description                                                                                            |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [Credential Provider driven Windows Logon Experience](http://go.microsoft.com/fwlink/?LinkId=717287)<br/> | Overview of Winlogon and Credential Provider architecture and a sample Credential Provider.<br/> |
| [Shell Interfaces](https://msdn.microsoft.com/windows/desktop/05223970-14f5-44c2-937b-07826b8aecf9)<br/>                                                                | Credential Provider interface reference.<br/>                                                    |
| [Credential Providers in Windows 10](credential-providers-in-windows.md)<br/>                            | Third-party credential providers and system credential providers in Windows 10.<br/>             |



 

For a sample Credential Provider implementation, see the sample located in the Windows SDK installation directory under \\Samples\\Security\\CredentialProvider.

**Windows Server 2003 and Windows XP:** Credential Providers are not supported. For information about customizing Winlogon, see [Winlogon and GINA](winlogon-and-gina.md).

 

 




