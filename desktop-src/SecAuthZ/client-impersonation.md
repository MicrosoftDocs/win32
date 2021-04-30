---
description: Impersonation is the ability of a thread to execute using different security information than the process that owns the thread.
ms.assetid: a3f74372-bdc9-43eb-b72f-7d00a43e78a8
title: Client Impersonation (Authorization)
ms.topic: article
ms.date: 05/31/2018
---

# Client Impersonation (Authorization)

[*Impersonation*](/windows/desktop/SecGloss/i-gly) is the ability of a thread to execute using different security information than the process that owns the thread. Typically, a thread in a server application impersonates a client. This allows the server thread to act on behalf of that client to access objects on the server or validate access to the client's own objects.

The Microsoft Windows API provides the following functions to begin an impersonation:

-   A DDE server application can call the [**DdeImpersonateClient**](/windows/win32/api/ddeml/nf-ddeml-ddeimpersonateclient) function to impersonate a client.
-   A named-pipe server can call the [**ImpersonateNamedPipeClient**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-impersonatenamedpipeclient) function.
-   You can call the [**ImpersonateLoggedOnUser**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateloggedonuser) function to impersonate the security context of a logged-on user's [*access token*](/windows/desktop/SecGloss/a-gly).
-   The [**ImpersonateSelf**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateself) function enables a thread to generate a copy of its own access token. This is useful when an application needs to change the security context of a single thread. For example, sometimes only one thread of a process needs to enable a [*privilege*](/windows/desktop/SecGloss/p-gly).
-   You can call the [**SetThreadToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadtoken) function to cause the target thread to run in the security context of a specified [*impersonation token*](/windows/desktop/SecGloss/i-gly).
-   A Microsoft Remote Procedure Call (RPC) server application can call the [**RpcImpersonateClient**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcimpersonateclient) function to impersonate a client.
-   A [*security package*](/windows/desktop/SecGloss/s-gly) or application server can call the [**ImpersonateSecurityContext**](/windows/desktop/api/sspi/nf-sspi-impersonatesecuritycontext) function to impersonate a client.

For most of these impersonations, the impersonating thread can revert to its own security context by calling the [**RevertToSelf**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-reverttoself) function. The exception is the RPC impersonation, in which the RPC server application calls [**RpcRevertToSelf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcreverttoself) or [**RpcRevertToSelfEx**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcreverttoselfex) to revert to its own security context.

 

 
