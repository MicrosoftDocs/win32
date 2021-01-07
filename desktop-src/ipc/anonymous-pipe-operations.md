---
description: Anonymous pipe operations, including pipe creation, writing to a pipe, pipe handles.
ms.assetid: df81471c-1072-4456-a877-304e76ade4bd
title: Anonymous Pipe Operations
ms.topic: article
ms.date: 05/31/2018
---

# Anonymous Pipe Operations

The [**CreatePipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe) function creates an anonymous pipe and returns two handles: a read handle to the pipe and a write handle to the pipe. The read handle has read-only access to the pipe, and the write handle has write-only access to the pipe. To communicate using the pipe, the pipe server must pass a pipe handle to another process. Usually, this is done through inheritance; that is, the process allows the handle to be inherited by a child process. The process can also duplicate a pipe handle using the [**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle) function and send it to an unrelated process using some form of interprocess communication, such as DDE or shared memory.

A pipe server can send either the read handle or the write handle to the pipe client, depending on whether the client should use the anonymous pipe to send information or receive information. To read from the pipe, use the pipe's read handle in a call to the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) function. The **ReadFile** call returns when another process has written to the pipe. The **ReadFile** call can also return if all write handles to the pipe have been closed or if an error occurs before the read operation has been completed.

To write to the pipe, use the pipe's write handle in a call to the [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) function. The **WriteFile** call does not return until it has written the specified number of bytes to the pipe or an error occurs. If the pipe buffer is full and there are more bytes to be written, **WriteFile** does not return until another process reads from the pipe, making more buffer space available. The pipe server specifies the buffer size for the pipe when it calls [**CreatePipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe).

Asynchronous (overlapped) read and write operations are not supported by anonymous pipes. This means that you cannot use the [**ReadFileEx**](/windows/desktop/api/fileapi/nf-fileapi-readfileex) and [**WriteFileEx**](/windows/desktop/api/fileapi/nf-fileapi-writefileex) functions with anonymous pipes. In addition, the *lpOverlapped* parameter of [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) is ignored when these functions are used with anonymous pipes.

An anonymous pipe exists until all pipe handles, both read and write, have been closed. A process can close its pipe handles by using the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function. All pipe handles are also closed when the process terminates.

Anonymous pipes are implemented using a named pipe with a unique name. Therefore, you can often pass a handle to an anonymous pipe to a function that requires a handle to a named pipe.

 

 
