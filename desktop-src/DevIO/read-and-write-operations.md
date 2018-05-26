---
Description: Windows supports both synchronous and asynchronous (overlapped) file I/O operations on serial communications resources.
ms.assetid: cee44596-ad73-4afb-b86a-744b0b46d9d5
title: Read and Write Operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Read and Write Operations

Windows supports both synchronous and asynchronous (overlapped) file I/O operations on serial communications resources. Overlapped operations enable the calling thread to perform other tasks while the operation executes in the background. A thread uses the [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467) or [**ReadFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365468) function to read from a communications resource, and the [**WriteFile**](https://msdn.microsoft.com/library/windows/desktop/aa365747) or [**WriteFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365748) function to write to a communications resource. **ReadFile** and **WriteFile** can be performed synchronously or asynchronously. **ReadFileEx** and **WriteFileEx** can only be performed asynchronously.

The behavior of these read and write functions is affected by whether the function is executed as an overlapped operation, whether the time-out parameters are associated with the handle, and whether flow control parameters are associated with the handle.

A thread can also write to a communications resource by using the [**TransmitCommChar**](/windows/win32/Winbase/nf-winbase-transmitcommchar?branch=master) function, which transmits a specified character ahead of any pending data in the output buffer. This function is useful for transmitting a high priority signal character to the receiving system. Transmission of the high priority character is still subject to flow control and write time-outs, and the operation is performed synchronously.

A thread can use the [**PurgeComm**](/windows/win32/Winbase/nf-winbase-purgecomm?branch=master) function to discard all characters in a device's output or input buffer. **PurgeComm** can also terminate pending read or write operations, even if the operations have not been completed. If a thread uses **PurgeComm** to flush an output buffer, the deleted characters are not transmitted. To empty the output buffer while ensuring that the contents are transmitted, a thread can call the [**FlushFileBuffers**](https://msdn.microsoft.com/library/windows/desktop/aa364439) function (a synchronous operation). Note, however, that **FlushFileBuffers** is subject to flow control but not to write time-outs, and it will not return until all pending write operations have been transmitted.

 

 



