---
title: Enabling COM Security Using DCOMCNFG
description: Dcomcnfg.exe provides a user interface for modifying certain settings in the registry.
ms.assetid: 9aad6b71-47b8-4377-88e5-f463991d9e86
ms.topic: article
ms.date: 05/31/2018
---

# Enabling COM Security Using DCOMCNFG

Dcomcnfg.exe provides a user interface for modifying certain settings in the registry. By using Dcomcnfg.exe, you can enable security either on a computer-wide or a process-wide basis. You can enable security for a particular computer so that when a process does not provide its own security settings, either programmatically or through registry values, the values set by Dcomcnfg.exe will be used. Or you can use Dcomcnfg.exe to enable security for a particular application only.

When enabling security, there are two primary tasks to accomplish:

-   Set an authentication level that is not None.
-   Set permissions, including both launch and access permissions.

The steps taken to accomplish these tasks depend on whether you are enabling security for the whole computer or just for a particular application. Also, you may want to set other values for the computer or application.

> [!Note]  
> You must be an administrator to run Dcomcnfg.exe.

 

The following topics provide step-by-step procedures on how to set security with Dcomcnfg.exe:

-   [Setting System-Wide Security Using DCOMCNFG](setting-machine-wide-security-using-dcomcnfg.md)
-   [Setting Processwide Security Using DCOMCNFG](setting-processwide-security-using-dcomcnfg.md)

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> <dt>

[Turning Off Security](turning-off-security.md)
</dt> </dl>

 

 




