---
title: Setting Security for COM Applications
description: Setting Security for COM Applications
ms.assetid: 5b615007-e04b-41be-872c-20e0ea818ff1
ms.topic: article
ms.date: 05/31/2018
---

# Setting Security for COM Applications

There are several ways you can help control security for your applications. You can change a computer's default security settings, which are used by all applications on the computer that do not supply their own security values. You can set security for a particular process, either by using Dcomcnfg.exe or by calling [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). You can also programmatically control security settings at the interface proxy level.

The following topics provide procedures that explain how to set security:

-   [Modifying the Security Defaults for a Computer](modifying-the-security-defaults-for-a-computer.md)
-   [Setting Process-Wide Security](setting-processwide-security.md)
-   [Setting Security at the Interface Proxy Level](setting-security-at-the-interface-proxy-level.md)

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




