---
title: Launching User
description: Launching User
ms.assetid: ea5140b6-0a79-4149-b845-4f6388e89104
ms.topic: article
ms.date: 05/31/2018
---

# Launching User

This is the default setting for the application identity. When the launching user is chosen for the application's identity, each client account gets a new instance of the server and each server gets its own [window station](/windows/desktop/winstation/window-stations). Because of the separate server instances, launching user is the highest-level security protection identity setting. However, there are finite limits on resource consumption. Also, any GUI the server displays will not be seen by the client.

If the application has the identity of the launching user, it runs with an impersonation token. For more information about impersonation and access tokens, see [Impersonation Levels](impersonation-levels.md) and [Cloaking](cloaking.md).

## Related topics

<dl> <dt>

[Application Identity](application-identity.md)
</dt> <dt>

[Interactive User](interactive-user.md)
</dt> <dt>

[Service Identity](service-identity.md)
</dt> <dt>

[Specified User](specified-user.md)
</dt> </dl>

 

 