---
description: Beginning with Windows 8, Microsoft began distributing the providers that enable you to securely share encrypted secrets and messages across computers.
ms.assetid: C2E62DD2-8316-407B-B879-2617873F8409
title: Protection Providers
ms.topic: article
ms.date: 05/31/2018
---

# Protection Providers

Beginning with Windows 8, Microsoft began distributing the providers that enable you to securely share encrypted secrets and messages across computers. There are currently two key protection providers. The Microsoft Key Protection provider allows you to protect content to a group in an Active Directory forest. The Microsoft Client Key Protection provider allows you to protect content to a set of web credentials.

The correct protector to use is automatically chosen for you when the [**NCryptCreateProtectionDescriptor**](/windows/desktop/api/NCryptprotect/nf-ncryptprotect-ncryptcreateprotectiondescriptor) function parses the protection descriptor rule string your provide as input. The Microsoft Key Protection provider is chosen for rule strings that begin with SID, SDDL, and LOCAL. The Microsoft Client Key Protection provider parses rule strings that begin with WEBCREDENTIALS. For more information about rule strings, see [Protection Descriptors](protection-descriptors.md).

> [!Note]  
> Custom providers are not currently allowed.[CNG DPAPI](cng-dpapi.md)

 

## Related topics

<dl> <dt>

[CNG DPAPI](cng-dpapi.md)
</dt> <dt>

[**NCryptCreateProtectionDescriptor**](/windows/desktop/api/NCryptprotect/nf-ncryptprotect-ncryptcreateprotectiondescriptor)
</dt> <dt>

[Protection Descriptors](protection-descriptors.md)
</dt> </dl>

 

 



