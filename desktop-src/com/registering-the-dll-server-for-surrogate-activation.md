---
title: Registering the DLL Server for Surrogate Activation
description: Registering the DLL Server for Surrogate Activation
ms.assetid: 7133daa4-43b2-402e-a8ac-b357bea745d9
ms.topic: article
ms.date: 05/31/2018
---

# Registering the DLL Server for Surrogate Activation

A DLL server will be loaded into a surrogate process under the following conditions:

-   There must be an AppID value specified under the CLSID key in the registry, and a corresponding [AppID](appid-key.md) key.
-   In an activation call, the [**CLSCTX\_LOCAL\_SERVER**](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx) bit is set and the CLSID key does not specify [LocalServer32](localserver32.md), [LocalServer](localserver.md), or [LocalService](localservice.md). If other **CLSCTX** bits are set, the [**processing algorithm**](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)for the in-process, local, or remote execution flags is followed.
-   The CLSID key contains the [InprocServer32](inprocserver32.md) subkey.
-   The proxy/stub DLL specified in the **InprocServer32** key exists.
-   The [DllSurrogate](dllsurrogate.md) value exists under the **AppID** key.

If there is a **LocalServer**, **LocalServer32**, or **LocalService**, indicating the existence of an EXE, the EXE server or service will always be launched in preference to loading a DLL server into a surrogate process.

The **DllSurrogate** named-value must be specified for surrogate activation to occur. Activation refers to calls to any of the following activation functions:

-   [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject)
-   [**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex)
-   [**CoGetInstanceFromFile**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromfile)
-   [**CoGetInstanceFromIStorage**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromistorage)
-   [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject)

To launch an instance of the system-supplied surrogate, set the value of **DllSurrogate** either to an empty string or to **NULL**. To specify the launch of a custom surrogate, set the value to the path of the surrogate.

If both [RemoteServerName](remoteservername.md) and **DllSurrogate** are specified for the same AppID, the **RemoteServerName** value is ignored and the **DllSurrogate** value causes an activation on the local computer. For remote surrogate activation, specify **RemoteServerName** but not **DllSurrogate** on the client, and specify **DllSurrogate** on the server.

A DLL server that is designed to always run alone in its own surrogate process is best configured with an AppID equal its CLSID. Under **AppID**, simply specify a **DllSurrogate** named-value with an empty string value.

It is best to configure a DLL server that is designed to run alone in its own surrogate process and to service multiple clients across a network with a [RunAs](runas.md) value specified under the **AppID** registry key. Whether the **RunAs** specifies "Interactive User" or a specific user identity depends upon the user interface, security, and other server requirements. When a **RunAs** value is specified, only one instance of the server is loaded to service all of the clients, regardless of the identity of the client. On the other hand, do not configure the server with **RunAs** if the intention is to have one instance of the DLL server running in surrogate to service each remote client identity.

## Related topics

<dl> <dt>

[DLL Server Requirements](dll-server-requirements.md)
</dt> <dt>

[Surrogate Sharing](surrogate-sharing.md)
</dt> </dl>

 

 