---
Description: A server application can call the CreateProcessAsUser function to create a new process that runs in a clients security context.
ms.assetid: bd416109-fe76-4d55-bc63-3ebbcf32b92a
title: Processes in the Client Security Context
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Processes in the Client Security Context

A server application can call the [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429) function to create a new process that runs in a client's [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly). When called with a client's [*access token*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly), **CreateProcessAsUser** requires the SE\_ASSIGNPRIMARYTOKEN\_NAME and SE\_INCREASE\_QUOTA\_NAME privileges, which are held by Windows services running in the [LocalSystem Account](https://msdn.microsoft.com/library/windows/desktop/ms684190).

The [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429) function also requires a [*primary access token*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly). A server can get a primary access token for a client either by [starting a logon session](client-logon-sessions.md) for the client or by [impersonating the client](client-impersonation.md) and duplicating the [*impersonation token*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-impersonation-token-gly).

The following procedures describe two ways to create a client process.

**To create a client process by logging on to the client**

1.  Log the client on to the local computer using the client's [*credentials*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-credentials-gly) in a call to [**LogonUser**](https://msdn.microsoft.com/library/windows/desktop/aa378184). **LogonUser** produces a primary token for the client's [*logon session*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-logon-session-gly).
2.  If the server needs to use the client's security context, get access to the executable file for the client [*process*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly) by using the primary token in a call to the [**ImpersonateLoggedOnUser**](https://msdn.microsoft.com/en-us/library/Aa378612(v=VS.85).aspx) function.
3.  Create a process in the client's security context by using the primary token in a call to [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429).

> [!Note]  
> A process created by using the following technique may not be able to access network resources unless it has the client's [*credentials*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-credentials-gly).

 

**To create a client process by impersonating the client**

1.  Start the impersonation by using an impersonation function, such as [**ImpersonateNamedPipeClient**](https://msdn.microsoft.com/en-us/library/Aa378618(v=VS.85).aspx).
2.  Call the [**OpenThreadToken**](https://msdn.microsoft.com/en-us/library/Aa379296(v=VS.85).aspx) function to get an impersonation token that has the security context of the client.
3.  Call the [**DuplicateTokenEx**](https://msdn.microsoft.com/en-us/library/Aa446617(v=VS.85).aspx) function to convert the impersonation token into a primary token.
4.  Use the primary token in a call to the [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429) function to create a process in the client's security context.

By default, [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429) creates the client [*process*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly) on a noninteractive window station and desktop. To create an interactive process, the server must first set the [*discretionary access control lists*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACLs) of the interactive window station and desktop to ensure that the client is allowed access to them. The preferred way to do this is to log the client on, [get the security identifier (SID) of the client's logon session](https://msdn.microsoft.com/library/windows/desktop/aa446670), and then use that SID in access-allowed ACEs on both the interactive window station and desktop. The server can then call **CreateProcessAsUser**, specifying the interactive window station and desktop winsta0\\default. For an example that shows this procedure, see [Starting an Interactive Client Process in C++](https://msdn.microsoft.com/library/windows/desktop/aa379608).

 

 



