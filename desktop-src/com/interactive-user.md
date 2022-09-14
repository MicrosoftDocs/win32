---
title: Interactive User
description: The interactive user is the user that is currently logged on to the computer where the COM server is running.
ms.assetid: 6d43842c-0ad1-4563-b50c-5024bda480f1
ms.topic: article
ms.date: 05/31/2018
---

# Interactive User

The *interactive user* is the user that is currently logged on to the computer where the COM server is running. If the identity is set to be the interactive user, all clients use the same instance of the server if the server registers its class factory as multi-use. If no user is logged on, the server will not run. If the server has a graphical user interface (GUI) that the client needs to see, you should use interactive user for the server's identity. However, choosing this identity carries some security risks because the server runs under the identity of the logged on user without the logged on user's knowledge or consent. In addition, a service application cannot display a user interface. For more information, see [Interactive Services](/windows/desktop/Services/interactive-services).

If a COM server is configured to run as the interactive user, in a terminal services environment, the server will be launched in the interactive session that matches the client's user identity. However, the client application can use the session moniker to reference an object provided by the server in a session that does not match the client identity. When this is used, the client application can specify any session, in which case the server will run as the user who owns the session, not the launching user. The default access permissions in this scenario would not allow the launching user to call methods on the server. However, the following security risks remain:

-   If the COM server exposes interfaces that are not controlled by COM, such as TCP ports, named pipes, LPC ports, shared memory sections, and so on, these could be used by the launching user to influence the server. COM objects configured to run as the interactive user should reduce this attack surface as much as possible.
-   COM objects are free to set their own access permissions. If the object sets access permissions, either in its AppID registration or by calling [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity), to allow the launching user access, the user would be able to launch the server to run as another user, then access the object.

## Related topics

<dl> <dt>

[Application Identity](application-identity.md)
</dt> <dt>

[Launching User](launching-user.md)
</dt> <dt>

[Service Identity](service-identity.md)
</dt> <dt>

[Specified User](specified-user.md)
</dt> </dl>

 

 