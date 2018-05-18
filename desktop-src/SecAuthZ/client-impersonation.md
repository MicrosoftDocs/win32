---
Description: 'Impersonation is the ability of a thread to execute using different security information than the process that owns the thread.'
ms.assetid: 'a3f74372-bdc9-43eb-b72f-7d00a43e78a8'
title: Client Impersonation
---

# Client Impersonation

[*Impersonation*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-gly) is the ability of a thread to execute using different security information than the process that owns the thread. Typically, a thread in a server application impersonates a client. This allows the server thread to act on behalf of that client to access objects on the server or validate access to the client's own objects.

The Microsoft Windows API provides the following functions to begin an impersonation:

-   A DDE server application can call the [**DdeImpersonateClient**](_win32_ddeimpersonateclient_cpp) function to impersonate a client.
-   A named-pipe server can call the [**ImpersonateNamedPipeClient**](impersonatenamedpipeclient.md) function.
-   You can call the [**ImpersonateLoggedOnUser**](impersonateloggedonuser.md) function to impersonate the security context of a logged-on user's [*access token*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly).
-   The [**ImpersonateSelf**](impersonateself.md) function enables a thread to generate a copy of its own access token. This is useful when an application needs to change the security context of a single thread. For example, sometimes only one thread of a process needs to enable a [*privilege*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-privilege-gly).
-   You can call the [**SetThreadToken**](setthreadtoken.md) function to cause the target thread to run in the security context of a specified [*impersonation token*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly).
-   A Microsoft Remote Procedure Call (RPC) server application can call the [**RpcImpersonateClient**](https://msdn.microsoft.com/library/windows/desktop/aa375720) function to impersonate a client.
-   A [*security package*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-package-gly) or application server can call the [**ImpersonateSecurityContext**](https://msdn.microsoft.com/library/windows/desktop/aa375497) function to impersonate a client.

For most of these impersonations, the impersonating thread can revert to its own security context by calling the [**RevertToSelf**](reverttoself.md) function. The exception is the RPC impersonation, in which the RPC server application calls [**RpcRevertToSelf**](https://msdn.microsoft.com/library/windows/desktop/aa378430) or [**RpcRevertToSelfEx**](https://msdn.microsoft.com/library/windows/desktop/aa378431) to revert to its own security context.

 

 



