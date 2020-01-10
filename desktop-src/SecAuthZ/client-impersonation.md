---
Description: Impersonation is the ability of a thread to execute using different security information than the process that owns the thread.
ms.assetid: a3f74372-bdc9-43eb-b72f-7d00a43e78a8
title: Client Impersonation (Authorization)
ms.topic: article
ms.date: 05/31/2018
---

# Client Impersonation (Authorization)

[*Impersonation*](https://docs.microsoft.com/windows/desktop/SecGloss/i-gly) is the ability of a thread to execute using different security information than the process that owns the thread. Typically, a thread in a server application impersonates a client. This allows the server thread to act on behalf of that client to access objects on the server or validate access to the client's own objects.

The Microsoft Windows API provides the following functions to begin an impersonation:

-   A DDE server application can call the [**DdeImpersonateClient**](https://msdn.microsoft.com/library/ms648756(v=VS.85).aspx) function to impersonate a client.
-   A named-pipe server can call the [**ImpersonateNamedPipeClient**](https://msdn.microsoft.com/library/Aa378618(v=VS.85).aspx) function.
-   You can call the [**ImpersonateLoggedOnUser**](https://msdn.microsoft.com/library/Aa378612(v=VS.85).aspx) function to impersonate the security context of a logged-on user's [*access token*](https://docs.microsoft.com/windows/desktop/SecGloss/a-gly).
-   The [**ImpersonateSelf**](https://msdn.microsoft.com/library/Aa378729(v=VS.85).aspx) function enables a thread to generate a copy of its own access token. This is useful when an application needs to change the security context of a single thread. For example, sometimes only one thread of a process needs to enable a [*privilege*](https://docs.microsoft.com/windows/desktop/SecGloss/p-gly).
-   You can call the [**SetThreadToken**](https://msdn.microsoft.com/library/Aa379590(v=VS.85).aspx) function to cause the target thread to run in the security context of a specified [*impersonation token*](https://docs.microsoft.com/windows/desktop/SecGloss/i-gly).
-   A Microsoft Remote Procedure Call (RPC) server application can call the [**RpcImpersonateClient**](https://docs.microsoft.com/windows/desktop/api/rpcdce/nf-rpcdce-rpcimpersonateclient) function to impersonate a client.
-   A [*security package*](https://docs.microsoft.com/windows/desktop/SecGloss/s-gly) or application server can call the [**ImpersonateSecurityContext**](https://docs.microsoft.com/windows/desktop/api/sspi/nf-sspi-impersonatesecuritycontext) function to impersonate a client.

For most of these impersonations, the impersonating thread can revert to its own security context by calling the [**RevertToSelf**](https://msdn.microsoft.com/library/Aa379317(v=VS.85).aspx) function. The exception is the RPC impersonation, in which the RPC server application calls [**RpcRevertToSelf**](https://docs.microsoft.com/windows/desktop/api/rpcdce/nf-rpcdce-rpcreverttoself) or [**RpcRevertToSelfEx**](https://docs.microsoft.com/windows/desktop/api/rpcdce/nf-rpcdce-rpcreverttoselfex) to revert to its own security context.

 

 



