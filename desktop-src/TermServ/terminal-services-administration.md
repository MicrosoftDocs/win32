---
title: Remote Desktop Services Administration
description: The Remote Desktop Services API enables you to enumerate and manage Remote Desktop Session Host (RD Session Host) servers, client sessions, and processes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '85a9ed9d-79d6-4011-93a4-00847c689747'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Remote Desktop Services Administration

The Remote Desktop Services API enables you to enumerate and manage Remote Desktop Session Host (RD Session Host) servers, client sessions, and processes.

To retrieve the names of all the RD Session Host servers in a domain, call the [**NetServerEnum**](https://msdn.microsoft.com/library/windows/desktop/aa370623) function to enumerate servers of the SV\_TYPE\_TERMINALSERVER type. To open a handle to a specific RD Session Host server, pass the server name in a call to the [**WTSOpenServer**](wtsopenserver.md) function. When you have finished using the handle, release it by calling the [**WTSCloseServer**](wtscloseserver.md) function.

You can use the handle returned by **WTSOpenServer** to perform the following operations on the server.



| Function                                                         | Operation                                                                                                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WTSDisconnectSession**](wtsdisconnectsession.md)             | Disconnects the client from a specified session. The session remains active and the user can log on again to connect to the same session.                                                                         |
| [**WTSEnumerateSessions**](wtsenumeratesessions.md)             | Returns a list of sessions on the specified RD Session Host server.                                                                                                                                               |
| [**WTSEnumerateProcesses**](wtsenumerateprocesses.md)           | Returns a list of processes on the specified RD Session Host server.                                                                                                                                              |
| [**WTSLogoffSession**](wtslogoffsession.md)                     | Logs off the specified session.                                                                                                                                                                                   |
| [**WTSQuerySessionInformation**](wtsquerysessioninformation.md) | Returns information about the specified session on the specified RD Session Host server.                                                                                                                          |
| [**WTSSendMessage**](wtssendmessage.md)                         | Shows a message box on the client display of a specified session.                                                                                                                                                 |
| [**WTSShutdownSystem**](wtsshutdownsystem.md)                   | Shuts down and optionally restarts a specified RD Session Host server.                                                                                                                                            |
| [**WTSTerminateProcess**](wtsterminateprocess.md)               | Terminates a specified process on a specified RD Session Host server.                                                                                                                                             |
| [**WTSVirtualChannelOpen**](wtsvirtualchannelopen.md)           | Opens a handle to the server end of a specified virtual channel. For more information about virtual channels, see [Using Remote Desktop Services Virtual Channels](using-terminal-services-virtual-channels.md). |
| [**WTSWaitSystemEvent**](wtswaitsystemevent.md)                 | Waits for an event, such as the creation of a client session or a user logging on to the RD Session Host server.                                                                                                  |



 

Several of these functions allocate buffers to return information to the caller. When you have finished using the buffer, free it by calling the [**WTSFreeMemory**](wtsfreememory.md) function.

 

 




