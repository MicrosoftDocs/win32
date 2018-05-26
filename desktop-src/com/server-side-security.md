---
title: Server-Side Security
description: Server-Side Security
ms.assetid: 6c1d210e-daf0-490a-a6b9-65d99b9e1d7d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Server-Side Security

The server can retrieve security information about a caller or impersonate the caller by using the methods of [**IServerSecurity**](/windows/win32/objidlbase/nn-objidl-iserversecurity?branch=master). An implementation of **IServerSecurity** is supplied by COM on the context object for the current call when standard marshaling is used. However, this interface may be absent for some custom-marshaled interfaces.

When a call arrives at the server, the server can call [**CoGetCallContext**](/windows/win32/combaseapi/nf-combaseapi-cogetcallcontext?branch=master) to obtain a pointer to the [**IServerSecurity**](/windows/win32/objidlbase/nn-objidl-iserversecurity?branch=master) interface. With this pointer, **IServerSecurity** methods can be called by the server to find out what the client's authentication settings are and to impersonate the client, if needed. The **IServerSecurity** object is valid on any thread in the apartment until the call represented by **IServerSecurity** completes. For more information about impersonation, see [Impersonation](impersonation.md) and [Cloaking](cloaking.md).

The following helper functions that rely on the call context object's [**IServerSecurity**](/windows/win32/objidlbase/nn-objidl-iserversecurity?branch=master) interface implementation are also available:

-   [**CoQueryClientBlanket**](/windows/win32/combaseapi/nf-combaseapi-coqueryclientblanket?branch=master)
-   [**CoImpersonateClient**](/windows/win32/combaseapi/nf-combaseapi-coimpersonateclient?branch=master)
-   [**CoRevertToSelf**](/windows/win32/combaseapi/nf-combaseapi-coreverttoself?branch=master)

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




