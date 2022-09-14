---
title: RPC Security Essentials
description: To complete any remote procedure call, all distributed applications must create a binding between the client and the server.
ms.assetid: 7b8adba2-19aa-4179-b6b3-ef27f4383bd4
ms.topic: article
ms.date: 05/31/2018
---

# RPC Security Essentials

To complete any remote procedure call, all distributed applications must create a binding between the client and the server. For more information on bindings, see [Binding and Handles](binding-and-handles.md). To complete a secure remote procedure call, additional steps are necessary. First, the server must choose a security provider (authentication service in DCE terminology). Then it must decide on its authentication mechanism. After that, the client obtains a binding to the server, and requests a secure remote procedure call from the RPC run time, and specifies various security options, such as security provider, security QOS options, and so on.

This section explains the essential concepts and information required to use the RPC functions to create a client and server for an authenticated distributed application. It is organized into the following topics:

-   [Principal Names](principal-names.md)
-   [Authentication Levels](authentication-levels.md)
-   [Authentication Services](authentication-services.md)
-   [Client Authentication Credentials](client-authentication-credentials.md)
-   [Authorization Services](authorization-services.md)
-   [Quality of Service](quality-of-service.md)
-   [Authorization Functions](authorization-functions.md)
-   [Key Acquisition Functions](key-acquisition-functions.md)
-   [Client Impersonation](client-impersonation.md)

 

 




