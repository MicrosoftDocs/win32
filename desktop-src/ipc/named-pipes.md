---
description: A named pipe is a named, one-way or duplex pipe for communication between the pipe server and one or more pipe clients.
ms.assetid: 7a4c11ac-14c0-4a93-b72e-02fb8852cc15
title: Named Pipes
ms.topic: article
ms.date: 05/31/2018
---

# Named Pipes

A *named pipe* is a named, one-way or duplex pipe for communication between the pipe server and one or more pipe clients. All instances of a named pipe share the same pipe name, but each instance has its own buffers and handles, and provides a separate conduit for client/server communication. The use of instances enables multiple pipe clients to use the same named pipe simultaneously.

Any process can access named pipes, subject to security checks, making named pipes an easy form of communication between related or unrelated processes.

Any process can act as both a server and a client, making peer-to-peer communication possible. As used here, the term pipe server refers to a process that creates a named pipe, and the term pipe client refers to a process that connects to an instance of a named pipe. The server-side function for instantiating a named pipe is [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea). The server-side function for accepting a connection is [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe). A client process connects to a named pipe by using the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) or [**CallNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-callnamedpipea) function.

Named pipes can be used to provide communication between processes on the same computer or between processes on different computers across a network. If the server service is running, all named pipes are accessible remotely. If you intend to use a named pipe locally only, deny access to NT AUTHORITY\\NETWORK or switch to local RPC.

For more information, see the following topics:

-   [Pipe Names](pipe-names.md)
-   [Named Pipe Open Modes](named-pipe-open-modes.md)
-   [Named Pipe Type, Read, and Wait Modes](named-pipe-type-read-and-wait-modes.md)
-   [Named Pipe Instances](named-pipe-instances.md)
-   [Named Pipe Operations](named-pipe-operations.md)
-   [Synchronous and Overlapped Input and Output](synchronous-and-overlapped-input-and-output.md)
-   [Named Pipe Security and Access Rights](named-pipe-security-and-access-rights.md)
-   [Impersonating a Named Pipe Client](impersonating-a-named-pipe-client.md)
-   [Using Pipes](using-pipes.md)

 

 
