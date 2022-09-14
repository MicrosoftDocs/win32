---
description: Pipe operations, including pipe clients and servers can call one of several functions — in addition to CallNamedPipe — to read from and write to a named pipe.
ms.assetid: ae06455e-33bc-433d-be8f-aeb8eeb99b1d
title: Named Pipe Operations
ms.topic: article
ms.date: 05/31/2018
---

# Named Pipe Operations

The first time the pipe server calls the [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea) function, it uses the *nMaxInstances* parameter to specify the maximum number of instances of the pipe that can exist simultaneously. The server can call **CreateNamedPipe** repeatedly to create additional instances of the pipe, as long as it does not exceed the maximum number of instances. If the function succeeds, each call returns a handle to the server end of a named pipe instance.

As soon as the pipe server creates a pipe instance, a pipe client can connect to it by calling the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) or [**CallNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-callnamedpipea) function. If a pipe instance is available, **CreateFile** returns a handle to the client end of the pipe instance. If no instances of the pipe are available, a pipe client can use the [**WaitNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-waitnamedpipea) function to wait until a pipe becomes available.

A pipe server can determine when a pipe client is connected to a pipe instance by calling the [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) function. If the pipe handle is in blocking-wait mode, **ConnectNamedPipe** does not return until a client is connected.

Pipe clients and servers can call one of several functions — in addition to [**CallNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-callnamedpipea) — to read from and write to a named pipe. The behavior of these functions depends on the type of pipe and the modes in effect for the specified pipe handle, as follows:

-   The [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) functions can be used with either byte-type or message-type pipes.
-   The [**ReadFileEx**](/windows/desktop/api/fileapi/nf-fileapi-readfileex) and [**WriteFileEx**](/windows/desktop/api/fileapi/nf-fileapi-writefileex) functions can be used with either byte-type or message-type pipes if the pipe handle was opened for overlapped operations.
-   The [**PeekNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-peeknamedpipe) function can be used to read without removing the contents of either a byte-type pipe or a message-type pipe. **PeekNamedPipe** can also return additional information about the pipe instance.
-   The [**TransactNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-transactnamedpipe) function can be used with message-type duplex pipes if the pipe handle to the calling process is set to message-read mode. The function writes a request message and reads a reply message in a single operation, enhancing network performance.

The pipe server should not perform a blocking read operation until the pipe client has started. Otherwise, a race condition can occur. This typically occurs when initialization code, such as that of the C run-time library, needs to lock and examine inherited handles.

When a client and server finish using a pipe instance, the server should first call the [**FlushFileBuffers**](/windows/desktop/api/fileapi/nf-fileapi-flushfilebuffers) function, to ensure that all bytes or messages written to the pipe are read by the client. **FlushFileBuffers** does not return until the client has read all data from the pipe. The server then calls the [**DisconnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-disconnectnamedpipe) function to close the connection to the pipe client. This function makes the client's handle invalid, if it has not already been closed. Any unread data in the pipe is discarded. After the client is disconnected, the server calls the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function to close its handle to the pipe instance. Alternatively, the server can use [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) to enable a new client to connect to this instance of the pipe.

A process can retrieve information about a named pipe by calling the [**GetNamedPipeInfo**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-getnamedpipeinfo) function, which returns the type of the pipe, the size of the input and output buffers, and the maximum number of pipe instances that can be created. The [**GetNamedPipeHandleState**](/windows/desktop/api/Winbase/nf-winbase-getnamedpipehandlestatea) function reports on the read and wait modes of a pipe handle, the current number of pipe instances, and additional information for pipes that communicate over a network. The [**SetNamedPipeHandleState**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-setnamedpipehandlestate) function sets the read mode and wait modes of a pipe handle. For pipe clients communicating with a remote server, the function also controls the maximum number of bytes to collect or the maximum time to wait before transmitting a message (assuming the client's handle was not opened with write-through mode enabled).

 

 
