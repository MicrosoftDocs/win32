---
title: Server-Side Security
description: Server-Side Security
ms.assetid: '6c1d210e-daf0-490a-a6b9-65d99b9e1d7d'
---

# Server-Side Security

The server can retrieve security information about a caller or impersonate the caller by using the methods of [**IServerSecurity**](iserversecurity.md). An implementation of **IServerSecurity** is supplied by COM on the context object for the current call when standard marshaling is used. However, this interface may be absent for some custom-marshaled interfaces.

When a call arrives at the server, the server can call [**CoGetCallContext**](cogetcallcontext.md) to obtain a pointer to the [**IServerSecurity**](iserversecurity.md) interface. With this pointer, **IServerSecurity** methods can be called by the server to find out what the client's authentication settings are and to impersonate the client, if needed. The **IServerSecurity** object is valid on any thread in the apartment until the call represented by **IServerSecurity** completes. For more information about impersonation, see [Impersonation](impersonation.md) and [Cloaking](cloaking.md).

The following helper functions that rely on the call context object's [**IServerSecurity**](iserversecurity.md) interface implementation are also available:

-   [**CoQueryClientBlanket**](coqueryclientblanket.md)
-   [**CoImpersonateClient**](coimpersonateclient.md)
-   [**CoRevertToSelf**](coreverttoself.md)

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




