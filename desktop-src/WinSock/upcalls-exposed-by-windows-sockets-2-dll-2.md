---
Description: This section lists the upcalls that service providers may make into the Windows Sockets client.
ms.assetid: a2069814-de95-40a2-ab09-c5187ecd56a7
title: Upcalls Exposed by Windows Sockets 2 DLL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Upcalls Exposed by Windows Sockets 2 DLL

This section lists the upcalls that service providers may make into the Windows Sockets client. Service providers receive an upcall dispatch table as a parameter to [**WSPStartup**](/windows/win32/Ws2spi/nf-ws2spi-wspstartup?branch=master) function, and use entries in this table to make the upcalls. Therefore, a client does not need to export its WPU functions.

It is not mandatory that providers use all of these upcalls. The following table indicates which upcalls must be used and which are optional.

| Function                                                               | Description                                                                                                              | Status                         | Meaning                                                                                                                                                                          |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WPUCloseEvent**](/windows/win32/Ws2spi/nf-ws2spi-wpucloseevent?branch=master)                               | Closes an open event object handle.                                                                                      | Optional.                      | The provider may use an an appropriate Windows call instead.                                                                                                                     |
| [**WPUCloseSocketHandle**](/windows/win32/Ws2spi/nf-ws2spi-wpuclosesockethandle?branch=master)                 | Closes a socket handle allocated by the Windows Sockets DLL.                                                             | Required.                      | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUCloseThread**](/windows/win32/Ws2spi/nf-ws2spi-wpuclosethread?branch=master)                             | Closes a thread ID for an internal service thread.                                                                       |                                |                                                                                                                                                                                  |
| [**WPUCompleteOverlappedRequest**](/windows/win32/Ws2spi/nf-ws2spi-wpucompleteoverlappedrequest?branch=master) | Delivers overlapped I/O completion notification where the completion mechanism is something other than user mode APC.    |                                |                                                                                                                                                                                  |
| [**WPUCreateEvent**](/windows/win32/Ws2spi/nf-ws2spi-wpucreateevent?branch=master)                             | Creates a new event object.                                                                                              | Optional.                      | The provider may use an appropriate Windows call instead.                                                                                                                        |
| [**WPUCreateSocketHandle**](/windows/win32/Ws2spi/nf-ws2spi-wpucreatesockethandle?branch=master)               | Creates a new socket handle for nonIFS providers.                                                                        | Required for nonIFS providers. | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUFDIsSet**](/windows/win32/Ws2spi/nf-ws2spi-wpufdisset?branch=master)                                     | Checks the membership of the specified socket handle.                                                                    | Optional.                      | This is just a convenience function that knows how to dig through [**fd\_set**](/windows/win32/winsock/nf-winsock-fd_set?branch=master) structures. A provider may need to dig through these structures explicitly anyway. |
| [**WPUGetProviderPath**](/windows/win32/Ws2spi/nf-ws2spi-wpugetproviderpath?branch=master)                     | Retrieves the DLL path for the specified provider.                                                                       | Required.                      | Only the Ws2\_32.dll would know where an adjacent protocol layer (potentially from another vendor) has been installed.                                                           |
| [**WPUModifyIFSHandle**](/windows/win32/Ws2spi/nf-ws2spi-wpumodifyifshandle?branch=master)                     | Receives a (possibly) modified IFS handle from the Windows Sockets DLL.                                                  | Required for IFS providers.    | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUPostMessage**](/windows/win32/Ws2spi/nf-ws2spi-wpupostmessage?branch=master)                             | Performs the standard [**PostMessage**](_win32_postmessage_cpp) function in a way that maintains backward compatibility. | Required.                      | Windows 2000 and Windows NT only. Windows 95 allows post message from kernel mode.                                                                                               |
| [**WPUQueryBlockingCallback**](/windows/win32/Ws2spi/nf-ws2spi-wpuqueryblockingcallback?branch=master)         | Returns a pointer to a thread's blocking hook function.                                                                  | Required.                      | There is no corresponding Windows functionality. Only the Ws2\_32.dll has the information to accomplish this.                                                                    |
| [**WPUQuerySocketHandleContext**](/windows/win32/Ws2spi/nf-ws2spi-wpuquerysockethandlecontext?branch=master)   | Gets a socket's context value (nonIFS providers only).                                                                   | Required for nonIFS providers. | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUQueueApc**](/windows/win32/Ws2spi/nf-ws2spi-wpuqueueapc?branch=master)                                   | Queues a user-mode APC to the specified thread.                                                                          | Optional.                      | The [**QueueUserApc**](base.queueuserapc) may also be used.                                                                                                                      |
| [**WPUResetEvent**](/windows/win32/Ws2spi/nf-ws2spi-wpuresetevent?branch=master)                               | Resets an event object.                                                                                                  | Optional.                      | The provider may use an appropriate Windows call instead.                                                                                                                        |
| [**WPUSetEvent**](/windows/win32/Ws2spi/nf-ws2spi-wpusetevent?branch=master)                                   | Sets an event object.                                                                                                    | Optional.                      | The provider may use an appropriate Windows call instead.                                                                                                                        |



 

 

 



