---
description: A server with the SE\_TCB\_NAME privilege, such as a Windows service running in the LocalSystem Account, can call the LogonUser function to authenticate a client on the computer that the server is running on.
ms.assetid: 27328497-8f04-42e8-aadd-4c33b9907b94
title: Client Logon Sessions
ms.topic: article
ms.date: 05/31/2018
---

# Client Logon Sessions

A server with the SE\_TCB\_NAME privilege, such as a Windows service running in the [LocalSystem Account](/windows/desktop/Services/localsystem-account), can call the [**LogonUser**](/windows/desktop/api/winbase/nf-winbase-logonusera) function to [*authenticate*](/windows/desktop/SecGloss/a-gly) a client on the computer that the server is running on. The **LogonUser** function starts a new logon [*session*](/windows/desktop/SecGloss/s-gly) and returns a [*primary access token*](/windows/desktop/SecGloss/p-gly) that contains the client's security information. You can use this primary token in calling the [**ImpersonateLoggedOnUser**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateloggedonuser) function to impersonate the client or in calling the [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function to create a process that runs in the [*security context*](/windows/desktop/SecGloss/s-gly) of the client.

The advantage of authenticating the client in this way is that the server impersonating the authenticated client, or a [*process*](/windows/desktop/SecGloss/p-gly) created in the context of the authenticated client, can connect to remote network resources as the client. If this authentication is not done, the server can connect to network resources only if it has acquired the client's account name and password to pass to the [**WNetAddConnection2**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnection2a) function.

The disadvantage of authenticating the client in this way is that the server must have acquired the client's [*credentials*](/windows/desktop/SecGloss/c-gly) (domain name, user name, and password). If a remote client supplies these credentials to the server, it is the responsibility of the client and server to ensure that the credentials are transmitted in a secure manner.

 

 
