---
title: Setting Process-Wide Security
description: There are several ways to set process-wide security.
ms.assetid: 596ba257-cbde-4243-aa29-78749304867a
ms.topic: article
ms.date: 05/31/2018
---

# Setting Process-Wide Security

There are several ways to set process-wide security. The first way, using the Dcomcnfg.exe tool, is easiest because it requires no programming. The second technique offers the programmer more control, and it requires a call to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). Another technique is to set process-wide security in the registry by using the [AppID](appid-key.md) key.

For more information about these techniques, see the following topics:

-   [Setting Process-Wide Security Using DCOMCNFG](setting-processwide-security-using-dcomcnfg.md)
-   [Setting Process-Wide Security with CoInitializeSecurity](setting-processwide-security-with-coinitializesecurity.md)
-   [Setting Process-Wide Security Through the Registry](setting-processwide-security-through-the-registry.md)

## Related topics

<dl> <dt>

[Setting Security at the Interface Proxy Level](setting-security-at-the-interface-proxy-level.md)
</dt> <dt>

[Setting Security for COM Applications](setting-security-for-com-applications.md)
</dt> </dl>

 

 




