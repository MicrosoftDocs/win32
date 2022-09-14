---
title: Modifying the Security Defaults for a Computer
description: Modifying the Security Defaults for a Computer
ms.assetid: c6d84375-59ea-42d5-87f9-af514b6f7d7c
ms.topic: article
ms.date: 05/31/2018
---

# Modifying the Security Defaults for a Computer

It is not recommended that you change the system-wide security settings, because this will affect all COM server applications that do not set their own process-wide security, and might prevent them from working properly. If you are changing the system-wide security settings to affect the security settings for a particular COM application, then you should instead change the process-wide security settings for that particular COM application. For more information about setting process-wide security, see [Setting Process-Wide Security](setting-processwide-security.md).

Certain values in the registry determine security settings for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). You can modify these settings using Dcomcnfg.exe.

For more information, see the following topics:

-   [Registry Values for System-Wide Security](registry-values-for-machine-wide-security.md)
-   [Setting System-Wide Security Using DCOMCNFG](setting-machine-wide-security-using-dcomcnfg.md)

## Related topics

<dl> <dt>

[Setting Process-wide Security](setting-processwide-security.md)
</dt> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




