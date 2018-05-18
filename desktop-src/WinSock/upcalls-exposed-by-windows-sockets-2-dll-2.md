---
Description: 'This section lists the upcalls that service providers may make into the Windows Sockets client.'
ms.assetid: 'a2069814-de95-40a2-ab09-c5187ecd56a7'
title: Upcalls Exposed by Windows Sockets 2 DLL
---

# Upcalls Exposed by Windows Sockets 2 DLL

This section lists the upcalls that service providers may make into the Windows Sockets client. Service providers receive an upcall dispatch table as a parameter to [**WSPStartup**](wspstartup-2.md) function, and use entries in this table to make the upcalls. Therefore, a client does not need to export its WPU functions.

It is not mandatory that providers use all of these upcalls. The following table indicates which upcalls must be used and which are optional.

| Function                                                               | Description                                                                                                              | Status                         | Meaning                                                                                                                                                                          |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WPUCloseEvent**](wpucloseevent-2.md)                               | Closes an open event object handle.                                                                                      | Optional.                      | The provider may use an an appropriate Windows call instead.                                                                                                                     |
| [**WPUCloseSocketHandle**](wpuclosesockethandle-2.md)                 | Closes a socket handle allocated by the Windows Sockets DLL.                                                             | Required.                      | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUCloseThread**](wpuclosethread-2.md)                             | Closes a thread ID for an internal service thread.                                                                       |                                |                                                                                                                                                                                  |
| [**WPUCompleteOverlappedRequest**](wpucompleteoverlappedrequest-2.md) | Delivers overlapped I/O completion notification where the completion mechanism is something other than user mode APC.    |                                |                                                                                                                                                                                  |
| [**WPUCreateEvent**](wpucreateevent-2.md)                             | Creates a new event object.                                                                                              | Optional.                      | The provider may use an appropriate Windows call instead.                                                                                                                        |
| [**WPUCreateSocketHandle**](wpucreatesockethandle-2.md)               | Creates a new socket handle for nonIFS providers.                                                                        | Required for nonIFS providers. | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUFDIsSet**](wpufdisset-2.md)                                     | Checks the membership of the specified socket handle.                                                                    | Optional.                      | This is just a convenience function that knows how to dig through [**fd\_set**](fd-set-2.md) structures. A provider may need to dig through these structures explicitly anyway. |
| [**WPUGetProviderPath**](wpugetproviderpath-2.md)                     | Retrieves the DLL path for the specified provider.                                                                       | Required.                      | Only the Ws2\_32.dll would know where an adjacent protocol layer (potentially from another vendor) has been installed.                                                           |
| [**WPUModifyIFSHandle**](wpumodifyifshandle-2.md)                     | Receives a (possibly) modified IFS handle from the Windows Sockets DLL.                                                  | Required for IFS providers.    | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUPostMessage**](wpupostmessage-2.md)                             | Performs the standard [**PostMessage**](_win32_postmessage_cpp) function in a way that maintains backward compatibility. | Required.                      | Windows 2000 and Windows NT only. Windows 95 allows post message from kernel mode.                                                                                               |
| [**WPUQueryBlockingCallback**](wpuqueryblockingcallback-2.md)         | Returns a pointer to a thread's blocking hook function.                                                                  | Required.                      | There is no corresponding Windows functionality. Only the Ws2\_32.dll has the information to accomplish this.                                                                    |
| [**WPUQuerySocketHandleContext**](wpuquerysockethandlecontext-2.md)   | Gets a socket's context value (nonIFS providers only).                                                                   | Required for nonIFS providers. | The Ws2\_32.dll needs to query and/or modify internal state information associated with the socket handle.                                                                       |
| [**WPUQueueApc**](wpuqueueapc-2.md)                                   | Queues a user-mode APC to the specified thread.                                                                          | Optional.                      | The [**QueueUserApc**](base.queueuserapc) may also be used.                                                                                                                      |
| [**WPUResetEvent**](wpuresetevent-2.md)                               | Resets an event object.                                                                                                  | Optional.                      | The provider may use an appropriate Windows call instead.                                                                                                                        |
| [**WPUSetEvent**](wpusetevent-2.md)                                   | Sets an event object.                                                                                                    | Optional.                      | The provider may use an appropriate Windows call instead.                                                                                                                        |



 

 

 



