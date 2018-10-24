---
Description: Impersonation is the ability of a thread to execute in a security context different from that of the process that owns the thread.
ms.assetid: 1bde4d4d-958e-45f4-8cdb-0572adcaa3ac
title: Impersonating a Named Pipe Client
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Impersonating a Named Pipe Client

*Impersonation* is the ability of a thread to execute in a security context different from that of the process that owns the thread. Impersonation enables the server thread to perform actions on behalf of the client, but within the limits of the client's security context. The client typically has some lesser level of access rights. For more information, see [Impersonation](https://msdn.microsoft.com/library/windows/desktop/aa376391).

A named pipe server thread can call the [**ImpersonateNamedPipeClient**](https://msdn.microsoft.com/library/windows/desktop/aa378618) function to assume the access token of the user connected to the client end of the pipe. For example, a named pipe server can provide access to a database or file system to which the pipe server has privileged access. When a pipe client sends a request to the server, the server impersonates the client and attempts to access the protected database. The system then grants or denies the server's access, based on the security level of the client. When the server is finished, it uses the [**RevertToSelf**](https://msdn.microsoft.com/library/windows/desktop/aa379317) function to restore its original security token.

The [impersonation level](https://msdn.microsoft.com/library/windows/desktop/aa378832) determines the operations the server can perform while impersonating the client. By default, a server impersonates at the SecurityImpersonation impersonation level. However, when the client calls the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function to open a handle to the client end of the pipe, the client can use the SECURITY\_SQOS\_PRESENT flag to control the server's impersonation level.

 

 



