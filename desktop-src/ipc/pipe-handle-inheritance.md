---
description: The pipe server controls whether its handles can be inherited in the following ways.
ms.assetid: 72302f8b-f3a2-4efc-aab1-e596b8323984
title: Pipe Handle Inheritance
ms.topic: article
ms.date: 05/31/2018
---

# Pipe Handle Inheritance

The pipe server controls whether its handles can be inherited in the following ways:

-   The [**CreatePipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe) function receives a [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure. If the pipe server sets the **bInheritHandle** member of this structure to **TRUE**, the handles created by **CreatePipe** can be inherited.
-   The pipe server can use the [**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle) function to change the inheritance of a pipe handle. The pipe server can create a noninheritable duplicate of an inheritable pipe handle or an inheritable duplicate of a noninheritable pipe handle.
-   The [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) function enables the pipe server to specify whether a child process inherits all or none of its inheritable handles.

When a child process inherits a pipe handle, the system enables the process to access the pipe. However, the parent process must communicate the handle value to the child process. The parent process typically does this by redirecting the standard output handle to the child process, as shown in the following steps:

1.  Call the [**GetStdHandle**](/windows/console/getstdhandle) function to get the current standard output handle; save this handle so you can restore the original standard output handle after the child process has been created.
2.  Call the [**SetStdHandle**](/windows/console/setstdhandle) function to set the standard output handle to the write handle to the pipe. Now the parent process can create the child process.
3.  Call the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function to close the write handle to the pipe. After the child process inherits the write handle, the parent process no longer needs its copy.
4.  Call [**SetStdHandle**](/windows/console/setstdhandle) to restore the original standard output handle.

The child process uses the [**GetStdHandle**](/windows/console/getstdhandle) function to get its standard output handle, which is now a handle to the write end of a pipe. The child process then uses the [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) function to send its output to the pipe. When the child has finished with the pipe, it should close the pipe handle by calling [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) or by terminating, which automatically closes the handle.

The parent process uses the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) function to receive input from the pipe. Data is written to an anonymous pipe as a stream of bytes. This means that the parent process reading from a pipe cannot distinguish between the bytes written in separate write operations, unless both the parent and child processes use a protocol to indicate where the write operation ends. When all write handles to the pipe are closed, the **ReadFile** function returns zero. It is important for the parent process to close its handle to the write end of the pipe before calling **ReadFile**. If this is not done, the **ReadFile** operation cannot return zero because the parent process has an open handle to the write end of the pipe.

The procedure for redirecting the standard input handle is similar to that for redirecting the standard output handle, except that the pipe's read handle is used as the child's standard input handle. In this case, the parent process must ensure that the child process does not inherit the pipe's write handle. If this is not done, the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) operation performed by the child process cannot return zero because the child process has an open handle to the write end of the pipe.

For an example program that uses anonymous pipes to redirect the standard handles of a child process, see [Creating a Child Process with Redirected Input and Output](/windows/desktop/ProcThread/creating-a-child-process-with-redirected-input-and-output).

 

 
