---
Description: Explains strategies for accessing network resources.
ms.assetid: d55b3204-430d-4fa4-b7a7-1e279beed8e3
title: Client Access to Network Resources
ms.topic: article
ms.date: 05/31/2018
---

# Client Access to Network Resources

A server can use the following strategies to access network resources:

-   If the server has the account name and password of a client, it can call [**WNetAddConnection2**](https://msdn.microsoft.com/library/windows/desktop/aa385413) with the client's [*credentials*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-credentials-gly) to map a local drive letter to a network share.
-   After calling [**LogonUser**](https://msdn.microsoft.com/library/windows/desktop/aa378184) with client credentials, the server can call the [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429) function to [create a process for the client](processes-in-the-client-security-context.md). This new client process can access network resources using the client's [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly). For example, the process can call the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function to open a file on a remote computer. The system uses the client's [*primary token*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-primary-token-gly) to check access attempts by the client process.
-   A server can call [**WNetAddConnection2**](https://msdn.microsoft.com/library/windows/desktop/aa385413) with null credentials to establish either a connection to a network resource with server access or a default connection. If the server is running as the LocalSystem account, it authenticates to the network resource under the [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) of the domain server. If the server is running under a service account, it authenticates as that account. For more information, see the [LocalSystem Account](https://msdn.microsoft.com/library/windows/desktop/ms684190).

For information about protecting passwords, see [Handling Passwords](https://msdn.microsoft.com/library/windows/desktop/ms717799). For information about acquiring credentials, see [Asking the User for Credentials](https://msdn.microsoft.com/library/windows/desktop/ms717794).

 

 



