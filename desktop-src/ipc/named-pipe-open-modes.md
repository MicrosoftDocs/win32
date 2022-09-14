---
description: The pipe server specifies the pipe access, overlap, and write-through modes in the dwOpenMode parameter of the CreateNamedPipe function. The pipe clients can specify these open modes for their pipe handles using the CreateFile function.
ms.assetid: 88824566-93c7-4941-a4fc-3a7ae9a332a4
title: Named Pipe Open Modes
ms.topic: article
ms.date: 05/31/2018
---

# Named Pipe Open Modes

The pipe server specifies the pipe access, overlap, and write-through modes in the *dwOpenMode* parameter of the [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea) function. The pipe clients can specify these open modes for their pipe handles using the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function.

## Access Mode

Setting the pipe access mode is equivalent to specifying read or write access associated with the pipe server's handles. The following table shows the equivalent generic access right for each access mode you can specify with [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea).



| Access mode            | Equivalent generic access right |
|------------------------|---------------------------------|
| PIPE\_ACCESS\_INBOUND  | GENERIC\_READ                   |
| PIPE\_ACCESS\_OUTBOUND | GENERIC\_WRITE                  |
| PIPE\_ACCESS\_DUPLEX   | GENERIC\_READ \| GENERIC\_WRITE |



 

If the pipe server creates a pipe with PIPE\_ACCESS\_INBOUND, the pipe is read-only for the pipe server and write-only for the pipe client. If the pipe server creates a pipe with PIPE\_ACCESS\_OUTBOUND, the pipe is write-only for the pipe server and read-only for the pipe client. A pipe created with PIPE\_ACCESS\_DUPLEX is read/write for both the pipe server and the pipe client.

Pipe clients using [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) to connect to a named pipe must specify an access right in the *dwDesiredAccess* parameter that is compatible with the access mode specified by the pipe server. For example, a client must specify GENERIC\_READ access to open a handle for a pipe that the pipe server created with PIPE\_ACCESS\_OUTBOUND. The access modes must be the same for all instances of a pipe.

To read pipe attributes such as the read mode or blocking mode, the pipe handle must have the FILE\_READ\_ATTRIBUTES access right; to write pipe attributes, the pipe handle must have the FILE\_WRITE\_ATTRIBUTES access right. These access rights can be combined with the generic access right that is appropriate for the pipe: GENERIC\_READ with FILE\_WRITE\_ATTRIBUTES for a read-only pipe, or GENERIC\_WRITE with FILE\_READ\_ATTRIBUTES for a write-only pipe. Restricting access rights in this way provides better security for the pipe.

## Overlapped Mode

In overlapped mode, functions performing lengthy read, write, and connect operations can return immediately. This enables the thread to perform other operations while a time-consuming operation is executing in the background. To specify overlapped mode, use the FILE\_FLAG\_OVERLAPPED flag. For more information, see [Synchronous and Overlapped Input and Output](synchronous-and-overlapped-input-and-output.md).

The [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function allows the pipe client to set overlapped mode (FILE\_FLAG\_OVERLAPPED) for its pipe handles using the *dwFlagsAndAttributes* parameter.

## Write-Through Mode

Specify write-through mode with FILE\_FLAG\_WRITE\_THROUGH. This mode affects only write operations to byte-type pipes between pipe clients and pipe servers on different computers. In write-through mode, the functions that write to a named pipe do not return until the data is transmitted across the network and into the pipe's buffer on the remote computer. Write-through mode is useful for applications that require synchronization for every write operation.

If write-through mode is not enabled, the system enhances the efficiency of network operations by buffering data until a minimum number of bytes have accumulated or until a maximum time period has elapsed. Buffering enables the system to combine multiple write operations into a single network transmission. This means that a write operation can be successfully completed after the system puts the data in the outbound buffer, but before the system transmits it across the network.

The [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function allows the pipe client to set write-through mode (FILE\_FLAG\_WRITE\_THROUGH) for its pipe handles using the *dwFlagsAndAttributes* parameter. The write-through mode of a pipe handle cannot be changed after the pipe handle has been created. The write-through mode can be different for server and client handles to the same pipe instance.

A pipe client can use the [**SetNamedPipeHandleState**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-setnamedpipehandlestate) function to control the number of bytes and the time-out period before transmission for a pipe on which write-through mode is disabled. For a read-only pipe, the pipe handle must be opened with the GENERIC\_READ and FILE\_WRITE\_ATTRIBUTES access rights.

 

 
