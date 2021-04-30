---
description: Like all processes, a protected server has a primary access token that describes its security context.
ms.assetid: '4e6393b2-4a71-49e4-b1e7-f34bf317d60d'
title: The Client Security Context
ms.topic: article
ms.date: 05/31/2018
---

# The Client Security Context

Like all [*processes*](/windows/desktop/SecGloss/p-gly), a protected server has a [*primary access token*](/windows/desktop/SecGloss/p-gly) that describes its [*security context*](/windows/desktop/SecGloss/s-gly). When a client connects to a protected server, the server may want to perform actions using the client's security context instead of the server's security context. For example, when a client in a dynamic data exchange (DDE) conversation requests information from a DDE server, the server needs to verify that the client is allowed access to the information.

There are two ways that a server can act in the client's security context:

-   A thread of the server process can impersonate the client. In this case, the server's thread has an impersonation [*access token*](/windows/desktop/SecGloss/a-gly) that identifies the client, the client's groups, and the client's [*privileges*](/windows/desktop/SecGloss/p-gly). For more information, see [Client Impersonation](client-impersonation.md).
-   The server can get the client's [*credentials*](/windows/desktop/SecGloss/c-gly) and log the client on to the server's computer. This creates a new logon [*session*](/windows/desktop/SecGloss/s-gly) and produces a primary access token for the client. The server can then use the client's access token to impersonate the client or to start a new process that runs in the security context of the client. For more information, see [Client Logon Sessions](client-logon-sessions.md).

In most cases, impersonating the client is sufficient. Impersonation enables the server to check the client's access to securable objects, check the client's privileges, and generate audit trail entries that identify the client. Typically, a server needs to start a client logon session only if it needs to use the client's security context to access network resources.

 

 
