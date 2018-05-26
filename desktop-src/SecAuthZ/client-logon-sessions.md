---
Description: A server with the SE\_TCB\_NAME privilege, such as a Windows service running in the LocalSystem Account, can call the LogonUser function to authenticate a client on the computer that the server is running on.
ms.assetid: 27328497-8f04-42e8-aadd-4c33b9907b94
title: Client Logon Sessions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Logon Sessions

A server with the SE\_TCB\_NAME privilege, such as a Windows service running in the [LocalSystem Account](https://msdn.microsoft.com/library/windows/desktop/ms684190), can call the [**LogonUser**](https://msdn.microsoft.com/library/windows/desktop/aa378184) function to [*authenticate*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-authentication-gly) a client on the computer that the server is running on. The **LogonUser** function starts a new logon [*session*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-session-gly) and returns a [*primary access token*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) that contains the client's security information. You can use this primary token in calling the [**ImpersonateLoggedOnUser**](impersonateloggedonuser.md) function to impersonate the client or in calling the [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429) function to create a process that runs in the [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) of the client.

The advantage of authenticating the client in this way is that the server impersonating the authenticated client, or a [*process*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly) created in the context of the authenticated client, can connect to remote network resources as the client. If this authentication is not done, the server can connect to network resources only if it has acquired the client's account name and password to pass to the [**WNetAddConnection2**](https://msdn.microsoft.com/library/windows/desktop/aa385413) function.

The disadvantage of authenticating the client in this way is that the server must have acquired the client's [*credentials*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-credentials-gly) (domain name, user name, and password). If a remote client supplies these credentials to the server, it is the responsibility of the client and server to ensure that the credentials are transmitted in a secure manner.

 

 



