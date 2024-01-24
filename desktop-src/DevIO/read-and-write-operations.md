---
description: Windows supports both synchronous and asynchronous (overlapped) file I/O operations on serial communications resources.
ms.assetid: cee44596-ad73-4afb-b86a-744b0b46d9d5
title: Read and Write Operations
ms.topic: article
ms.date: 05/31/2018
---

# Read and Write Operations

Windows supports both synchronous and asynchronous (overlapped) file I/O operations on serial communications resources. Overlapped operations enable the calling thread to perform other tasks while the operation executes in the background. A thread uses the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) or [**ReadFileEx**](/windows/desktop/api/fileapi/nf-fileapi-readfileex) function to read from a communications resource, and the [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) or [**WriteFileEx**](/windows/desktop/api/fileapi/nf-fileapi-writefileex) function to write to a communications resource. **ReadFile** and **WriteFile** can be performed synchronously or asynchronously. **ReadFileEx** and **WriteFileEx** can only be performed asynchronously.

The behavior of these read and write functions is affected by whether the function is executed as an overlapped operation, whether the time-out parameters are associated with the handle, and whether flow control parameters are associated with the handle.

A thread can also write to a communications resource by using the [**TransmitCommChar**](/windows/desktop/api/Winbase/nf-winbase-transmitcommchar) function, which transmits a specified character ahead of any pending data in the output buffer. This function is useful for transmitting a high priority signal character to the receiving system. Transmission of the high priority character is still subject to flow control and write time-outs, and the operation is performed synchronously.

A thread can use the [**PurgeComm**](/windows/desktop/api/Winbase/nf-winbase-purgecomm) function to discard all characters in a device's output or input buffer. **PurgeComm** can also terminate pending read or write operations, even if the operations have not been completed. If a thread uses **PurgeComm** to flush an output buffer, the deleted characters are not transmitted. To empty the output buffer while ensuring that the contents are transmitted, a thread can call the [**FlushFileBuffers**](/windows/desktop/api/fileapi/nf-fileapi-flushfilebuffers) function (a synchronous operation). Note, however, that **FlushFileBuffers** is subject to flow control but not to write time-outs, and it will not return until all pending write operations have been transmitted.

 

 
