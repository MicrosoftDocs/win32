---
Description: Like all processes, a protected server has a primary access token that describes its security context.
ms.assetid: bd416109-fe76-4d55-bc63-3ebbcf32b92a
title: The Client Security Context
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Client Security Context

Like all [*processes*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly), a protected server has a [*primary access token*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) that describes its [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly). When a client connects to a protected server, the server may want to perform actions using the client's security context instead of the server's security context. For example, when a client in a dynamic data exchange (DDE) conversation requests information from a DDE server, the server needs to verify that the client is allowed access to the information.

There are two ways that a server can act in the client's security context:

-   A thread of the server process can impersonate the client. In this case, the server's thread has an impersonation [*access token*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly) that identifies the client, the client's groups, and the client's [*privileges*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-privilege-gly). For more information, see [Client Impersonation](client-impersonation.md).
-   The server can get the client's [*credentials*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-credentials-gly) and log the client on to the server's computer. This creates a new logon [*session*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-session-gly) and produces a primary access token for the client. The server can then use the client's access token to impersonate the client or to start a new process that runs in the security context of the client. For more information, see [Client Logon Sessions](client-logon-sessions.md).

In most cases, impersonating the client is sufficient. Impersonation enables the server to check the client's access to securable objects, check the client's privileges, and generate audit trail entries that identify the client. Typically, a server needs to start a client logon session only if it needs to use the client's security context to access network resources.

 

 



