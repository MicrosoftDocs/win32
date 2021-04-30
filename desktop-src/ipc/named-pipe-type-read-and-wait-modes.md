---
description: The pipe server specifies the pipe type mode, read mode, and wait mode in the dwPipeMode parameter of the CreateNamedPipe function. Pipe clients can specify these pipe modes for their pipe handles using the CreateFile function.
ms.assetid: 07cf9d06-6265-47f4-a9f1-c19c06cc5f9f
title: Named Pipe Type, Read, and Wait Modes
ms.topic: article
ms.date: 05/31/2018
---

# Named Pipe Type, Read, and Wait Modes

The pipe server specifies the pipe type mode, read mode, and wait mode in the *dwPipeMode* parameter of the [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea) function. Pipe clients can specify these pipe modes for their pipe handles using the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function.

## Type Mode

The type mode of a pipe determines how data is written to a named pipe. Data can be transmitted through a named pipe as either a stream of bytes or as a stream of messages. The pipe server specifies the pipe type when calling [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea) to create an instance of a named pipe. The type modes must be the same for all instances of a pipe.

To create a byte-type pipe, specify PIPE\_TYPE\_BYTE or use the default value. The data is written to the pipe as a stream of bytes, and the system does not differentiate between the bytes written in different write operations.

To create a message-type pipe, specify PIPE\_TYPE\_MESSAGE. The system treats the bytes written in each write operation to the pipe as a message unit. The system always performs write operations on message-type pipes as if write-through mode were enabled.

## Read Mode

The read mode of a pipe determines how data is read from a named pipe. The pipe server specifies the initial read mode for a pipe handle when calling [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea). Data can be read in byte-read mode or message-read mode. A handle to a byte-type pipe can be in byte-read mode only. A handle to a message-type pipe can be in either byte-read or message-read mode. For a message-type pipe, the read mode can be different for server and client handles to the same pipe instance.

To create the pipe handle in byte-read mode, specify PIPE\_READMODE\_BYTE or use the default value. Data is read from the pipe as a stream of bytes. A read operation is completed successfully when all available bytes in the pipe are read or when the specified number of bytes is read.

To create the pipe handle in message-read mode, specify PIPE\_READMODE\_MESSAGE. Data is read from the pipe as a stream of messages. A read operation is completed successfully only when the entire message is read. If the specified number of bytes to read is less than the size of the next message, the function reads as much of the message as possible before returning zero (the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns ERROR\_MORE\_DATA). The remainder of the message can be read using another read operation.

For a pipe client, a pipe handle returned by [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) is always in byte-read mode initially. Both pipe clients and pipe servers can use the [**SetNamedPipeHandleState**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-setnamedpipehandlestate) function to change the read mode of a pipe handle. The pipe handle must have the FILE\_WRITE\_ATTRIBUTES access right.

## Wait Mode

The wait mode of a pipe handle determines how the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile), [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), and [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) functions handle lengthy operations. In blocking-wait mode, the functions wait indefinitely for a process on the other end of the pipe to complete an operation. In nonblocking-wait mode, the functions return immediately in situations that would otherwise require an indefinite wait.

A [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) operation is affected by the wait mode of a pipe handle when the pipe is empty. With a blocking-wait handle, the operation is not completed successfully until data is available from a thread writing to the other end of the pipe. Using a nonblocking-wait handle, the function returns zero immediately, and the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns ERROR\_NO\_DATA.

A [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) operation is affected by the wait mode of a pipe handle when there is insufficient space in the pipe's buffer. With a blocking-wait handle, the write operation cannot succeed until sufficient space is created in the buffer by a thread reading from the other end of the pipe. With a nonblocking-wait handle, the write operation returns a nonzero value immediately, without writing any bytes (for a message-type pipe) or after writing as many bytes as the buffer holds (for a byte-type pipe).

A [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) operation is affected by the wait mode of a pipe handle when there is no client connected or waiting to connect to the pipe instance. With a blocking-wait handle, the connect operation does not succeed until a pipe client connects to the pipe instance by calling either the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) or [**CallNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-callnamedpipea) function. With a nonblocking-wait handle, the connect operation returns zero immediately, and the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns ERROR\_PIPE\_LISTENING.

By default, all named pipe handles returned by the [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea) or [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function are created with blocking-wait mode enabled. To create the pipe in nonblocking-wait mode, the pipe server specifies PIPE\_NOWAIT when calling **CreateNamedPipe**.

Both pipe clients and pipe servers can change a pipe handle's wait mode by specifying either PIPE\_WAIT or PIPE\_NOWAIT in a call to the [**SetNamedPipeHandleState**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-setnamedpipehandlestate) function.

> [!Note]  
> The nonblocking-wait mode is supported for compatibility with Microsoft LAN Manager version 2.0. This mode should not be used to achieve overlapped input and output (I/O) with named pipes. Overlapped I/O should be used instead, because it enables time-consuming operations to run in the background after the function returns. For more information about overlapped I/O, see [Synchronous and Overlapped Input and Output](synchronous-and-overlapped-input-and-output.md).

 

 

 
