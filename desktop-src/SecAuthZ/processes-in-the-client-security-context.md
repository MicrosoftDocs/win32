---
description: A server application can call the CreateProcessAsUser function to create a new process that runs in a clients security context.
ms.assetid: bd416109-fe76-4d55-bc63-3ebbcf32b92a
title: Processes in the Client Security Context
ms.topic: article
ms.date: 05/31/2018
---

# Processes in the Client Security Context

A server application can call the [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function to create a new process that runs in a client's [*security context*](/windows/desktop/SecGloss/s-gly). When called with a client's [*access token*](/windows/desktop/SecGloss/a-gly), **CreateProcessAsUser** requires the SE\_ASSIGNPRIMARYTOKEN\_NAME and SE\_INCREASE\_QUOTA\_NAME privileges, which are held by Windows services running in the [LocalSystem Account](/windows/desktop/Services/localsystem-account).

The [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function also requires a [*primary access token*](/windows/desktop/SecGloss/p-gly). A server can get a primary access token for a client either by [starting a logon session](client-logon-sessions.md) for the client or by [impersonating the client](client-impersonation.md) and duplicating the [*impersonation token*](/windows/desktop/SecGloss/i-gly).

The following procedures describe two ways to create a client process.

**To create a client process by logging on to the client**

1.  Log the client on to the local computer using the client's [*credentials*](/windows/desktop/SecGloss/c-gly) in a call to [**LogonUser**](/windows/desktop/api/winbase/nf-winbase-logonusera). **LogonUser** produces a primary token for the client's [*logon session*](/windows/desktop/SecGloss/l-gly).
2.  If the server needs to use the client's security context, get access to the executable file for the client [*process*](/windows/desktop/SecGloss/p-gly) by using the primary token in a call to the [**ImpersonateLoggedOnUser**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateloggedonuser) function.
3.  Create a process in the client's security context by using the primary token in a call to [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera).

> [!Note]  
> A process created by using the following technique may not be able to access network resources unless it has the client's [*credentials*](/windows/desktop/SecGloss/c-gly).

 

**To create a client process by impersonating the client**

1.  Start the impersonation by using an impersonation function, such as [**ImpersonateNamedPipeClient**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-impersonatenamedpipeclient).
2.  Call the [**OpenThreadToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthreadtoken) function to get an impersonation token that has the security context of the client.
3.  Call the [**DuplicateTokenEx**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetokenex) function to convert the impersonation token into a primary token.
4.  Use the primary token in a call to the [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function to create a process in the client's security context.

By default, [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) creates the client [*process*](/windows/desktop/SecGloss/p-gly) on a noninteractive window station and desktop. To create an interactive process, the server must first set the [*discretionary access control lists*](/windows/desktop/SecGloss/d-gly) (DACLs) of the interactive window station and desktop to ensure that the client is allowed access to them. The preferred way to do this is to log the client on, [get the security identifier (SID) of the client's logon session](/previous-versions//aa446670(v=vs.85)), and then use that SID in access-allowed ACEs on both the interactive window station and desktop. The server can then call **CreateProcessAsUser**, specifying the interactive window station and desktop winsta0\\default. For an example that shows this procedure, see [Starting an Interactive Client Process in C++](/previous-versions//aa379608(v=vs.85)).

 

 
