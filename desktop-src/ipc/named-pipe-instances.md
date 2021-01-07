---
description: Strategies for communicating with multiple pipe clients and servicing multiple pipe instances.
ms.assetid: c764bde5-e053-4124-b859-1d2839ada918
title: Named Pipe Instances
ms.topic: article
ms.date: 05/31/2018
---

# Named Pipe Instances

The simplest pipe server creates a single instance of a pipe, connects to a single client, communicates with the client, disconnects from the client, closes the pipe handle, and terminates. However, it is more common for a pipe server to communicate with multiple pipe clients. A pipe server could use a single pipe instance to connect with multiple pipe clients by connecting to and disconnecting from each client in sequence, but performance would be poor. The pipe server must create multiple pipe instances to efficiently handle multiple clients simultaneously.

There are three basic strategies for servicing multiple pipe instances.

-   Create a separate thread for each instance of the pipe. For an example of a multithreaded pipe server, see [Multithreaded Pipe Server](multithreaded-pipe-server.md).
-   Use overlapped operations by specifying an [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure in the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile), [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), and [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) functions. For an example, see [Named Pipe Server Using Overlapped I/O](named-pipe-server-using-overlapped-i-o.md).
-   Use overlapped operations by using the [**ReadFileEx**](/windows/desktop/api/fileapi/nf-fileapi-readfileex) and [**WriteFileEx**](/windows/desktop/api/fileapi/nf-fileapi-writefileex) functions, which specify a completion routine to be executed when the operation is completed. For an example, see [Named Pipe Server Using Completion Routines](named-pipe-server-using-completion-routines.md).

The multithreaded pipe server is easiest to write, because the thread for each instance handles communications for a single pipe client. The system allocates processor time to each thread as needed. But each thread uses system resources, which is a disadvantage for a pipe server that handles a large number of clients.

With a single-threaded server, it is easier to coordinate operations that affect multiple clients, and it is easier to protect shared resources from simultaneous access by multiple clients. The challenge of a single-threaded server is that it requires coordination of overlapped operations to allocate processor time for handling the simultaneous needs of clients.

 

 
