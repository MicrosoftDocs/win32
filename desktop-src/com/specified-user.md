---
title: Specified User
description: Specified User
ms.assetid: ec7684fb-a9f1-4ef2-a7d4-07caf24b6023
ms.topic: article
ms.date: 05/31/2018
---

# Specified User

Specifying a particular user (and the user's password) is the preferred identity for COM servers. The reason this identity is preferred is that no one has to be logged on the machine where the server is running for the server to run, and every client talks to the same instance of the server if the server registers its class factory as multi-use. If the server has a GUI, you should not choose this identity; if you do, the user will not be able to see the user interface.

This type of server has a primary token and can access remote resources where a server that has the launching-user identity might not be able to. For more information about impersonation and access tokens, see [Impersonation Levels](impersonation-levels.md) and [Cloaking](cloaking.md).

Running as a fixed user account is more secure than the interactive user identity because this identity can be assigned to the application only by someone who has the specific user's password.

## Related topics

<dl> <dt>

[Application Identity](application-identity.md)
</dt> <dt>

[Interactive User](interactive-user.md)
</dt> <dt>

[Launching User](launching-user.md)
</dt> <dt>

[Service Identity](service-identity.md)
</dt> </dl>

 

 




