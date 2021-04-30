---
description: Explains strategies for accessing network resources.
ms.assetid: d55b3204-430d-4fa4-b7a7-1e279beed8e3
title: Client Access to Network Resources
ms.topic: article
ms.date: 05/31/2018
---

# Client Access to Network Resources

A server can use the following strategies to access network resources:

-   If the server has the account name and password of a client, it can call [**WNetAddConnection2**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnection2a) with the client's [*credentials*](/windows/desktop/SecGloss/c-gly) to map a local drive letter to a network share.
-   After calling [**LogonUser**](/windows/desktop/api/winbase/nf-winbase-logonusera) with client credentials, the server can call the [**CreateProcessAsUser**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function to [create a process for the client](processes-in-the-client-security-context.md). This new client process can access network resources using the client's [*security context*](/windows/desktop/SecGloss/s-gly). For example, the process can call the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function to open a file on a remote computer. The system uses the client's [*primary token*](/windows/desktop/SecGloss/p-gly) to check access attempts by the client process.
-   A server can call [**WNetAddConnection2**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnection2a) with null credentials to establish either a connection to a network resource with server access or a default connection. If the server is running as the LocalSystem account, it authenticates to the network resource under the [*security context*](/windows/desktop/SecGloss/s-gly) of the domain server. If the server is running under a service account, it authenticates as that account. For more information, see the [LocalSystem Account](/windows/desktop/Services/localsystem-account).

For information about protecting passwords, see [Handling Passwords](/windows/desktop/SecBP/handling-passwords). For information about acquiring credentials, see [Asking the User for Credentials](/windows/desktop/SecBP/asking-the-user-for-credentials).

 

 
