---
Description: 'Pipe operations, including pipe clients and servers can call one of several functions — in addition to CallNamedPipe — to read from and write to a named pipe.'
ms.assetid: 'ae06455e-33bc-433d-be8f-aeb8eeb99b1d'
title: Named Pipe Operations
---

# Named Pipe Operations

The first time the pipe server calls the [**CreateNamedPipe**](createnamedpipe.md) function, it uses the *nMaxInstances* parameter to specify the maximum number of instances of the pipe that can exist simultaneously. The server can call **CreateNamedPipe** repeatedly to create additional instances of the pipe, as long as it does not exceed the maximum number of instances. If the function succeeds, each call returns a handle to the server end of a named pipe instance.

As soon as the pipe server creates a pipe instance, a pipe client can connect to it by calling the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or [**CallNamedPipe**](callnamedpipe.md) function. If a pipe instance is available, **CreateFile** returns a handle to the client end of the pipe instance. If no instances of the pipe are available, a pipe client can use the [**WaitNamedPipe**](waitnamedpipe.md) function to wait until a pipe becomes available.

A pipe server can determine when a pipe client is connected to a pipe instance by calling the [**ConnectNamedPipe**](connectnamedpipe.md) function. If the pipe handle is in blocking-wait mode, **ConnectNamedPipe** does not return until a client is connected.

Pipe clients and servers can call one of several functions — in addition to [**CallNamedPipe**](callnamedpipe.md) — to read from and write to a named pipe. The behavior of these functions depends on the type of pipe and the modes in effect for the specified pipe handle, as follows:

-   The [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467) and [**WriteFile**](https://msdn.microsoft.com/library/windows/desktop/aa365747) functions can be used with either byte-type or message-type pipes.
-   The [**ReadFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365468) and [**WriteFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365748) functions can be used with either byte-type or message-type pipes if the pipe handle was opened for overlapped operations.
-   The [**PeekNamedPipe**](peeknamedpipe.md) function can be used to read without removing the contents of either a byte-type pipe or a message-type pipe. **PeekNamedPipe** can also return additional information about the pipe instance.
-   The [**TransactNamedPipe**](transactnamedpipe.md) function can be used with message-type duplex pipes if the pipe handle to the calling process is set to message-read mode. The function writes a request message and reads a reply message in a single operation, enhancing network performance.

The pipe server should not perform a blocking read operation until the pipe client has started. Otherwise, a race condition can occur. This typically occurs when initialization code, such as that of the C run-time library, needs to lock and examine inherited handles.

When a client and server finish using a pipe instance, the server should first call the [**FlushFileBuffers**](https://msdn.microsoft.com/library/windows/desktop/aa364439) function, to ensure that all bytes or messages written to the pipe are read by the client. **FlushFileBuffers** does not return until the client has read all data from the pipe. The server then calls the [**DisconnectNamedPipe**](disconnectnamedpipe.md) function to close the connection to the pipe client. This function makes the client's handle invalid, if it has not already been closed. Any unread data in the pipe is discarded. After the client is disconnected, the server calls the [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) function to close its handle to the pipe instance. Alternatively, the server can use [**ConnectNamedPipe**](connectnamedpipe.md) to enable a new client to connect to this instance of the pipe.

A process can retrieve information about a named pipe by calling the [**GetNamedPipeInfo**](getnamedpipeinfo.md) function, which returns the type of the pipe, the size of the input and output buffers, and the maximum number of pipe instances that can be created. The [**GetNamedPipeHandleState**](getnamedpipehandlestate.md) function reports on the read and wait modes of a pipe handle, the current number of pipe instances, and additional information for pipes that communicate over a network. The [**SetNamedPipeHandleState**](setnamedpipehandlestate.md) function sets the read mode and wait modes of a pipe handle. For pipe clients communicating with a remote server, the function also controls the maximum number of bytes to collect or the maximum time to wait before transmitting a message (assuming the client's handle was not opened with write-through mode enabled).

 

 



