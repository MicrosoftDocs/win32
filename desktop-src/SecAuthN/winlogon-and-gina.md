---
description: Winlogon, the GINA, and network providers are the parts of the interactive logon model.
ms.assetid: 'd049d83f-b962-4c47-a79a-da556831e319'
title: Winlogon and GINA
ms.topic: article
ms.date: 05/31/2018
---

# Winlogon and GINA

[*Winlogon*](../secgloss/w-gly.md), the [*GINA*](../secgloss/g-gly.md), and network providers are the parts of the interactive logon model. The interactive logon procedure is normally controlled by Winlogon, MSGina.dll, and network providers. To change the interactive logon procedure, MSGina.dll can be replaced with a customized GINA DLL.

To work with Winlogon, the GINA, and network providers, you should have a firm knowledge of the Windows security architecture, especially with regard to [*tokens*](../secgloss/a-gly.md), [*authentication packages*](../secgloss/a-gly.md), and related matters.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

For information about specific functions and structures, see [Authentication Reference](authentication-reference.md). This reference section includes descriptions of the functions that a GINA DLL must implement, the Winlogon support functions that the GINA DLL can call, and the data structures used to pass information between Winlogon and the GINA.

Sample GINA code can be found in the Platform Software Development Kit (SDK) Security samples. The samples contain C code for implementing a GINA stub and a GINA hook. For more information about custom GINA DLL development, send an email message to: ginareqs@microsoft.com.

For information about the authentication model supported by Windows and for details about the [*Local Security Authority*](../secgloss/l-gly.md) (LSA) services and [*authentication package*](../secgloss/a-gly.md) interfaces, see [LSA Authentication](lsa-authentication.md).

For information about the aspects of the Local Security Authority that relate to the administration of security policy, which includes trust relationships with other computers and domains, assignment of privileges, audit generation control, system accessibility, and other similar topics, see [LSA Policy](../secmgmt/lsa-policy.md).

For information about Winlogon and GINA, see the following topics.



| Topic                                                                              | Description                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Winlogon](winlogon.md)                                                           | Winlogon provides a set of support functions for the GINA DLL.<br/>                                                                                                                                                                 |
| [GINA](gina.md)                                                                   | A GINA DLL provides customizable user identification and authentication procedures.<br/>                                                                                                                                            |
| [Terminal Services GINA Functions](terminal-services-gina-functions.md)           | When Terminal Services are enabled, the GINA must call Winlogon support functions to complete several tasks.<br/>                                                                                                                   |
| [Interaction with Network Providers](interaction-with-network-providers.md)       | You can configure a system to support zero or more network providers.<br/>                                                                                                                                                          |
| [Responsibilities and Features](responsibilities-and-features.md)                 | Each part of the interactive logon process has a set of responsibilities.<br/>                                                                                                                                                      |
| [Interaction Between Winlogon and GINA](interaction-between-winlogon-and-gina.md) | The state of Winlogon determines which GINA function is called to process any given [*secure attention sequence*](../secgloss/s-gly.md) (SAS) event.<br/> |
| [Winlogon Notification Packages](winlogon-notification-packages.md)               | You can implement a notification package to monitor and respond to Winlogon events.<br/>                                                                                                                                            |



 

 

 
