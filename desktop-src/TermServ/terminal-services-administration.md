---
title: Remote Desktop Services Administration
description: The Remote Desktop Services API enables you to enumerate and manage Remote Desktop Session Host (RD Session Host) servers, client sessions, and processes.
ms.assetid: 85a9ed9d-79d6-4011-93a4-00847c689747
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services Administration

The Remote Desktop Services API enables you to enumerate and manage Remote Desktop Session Host (RD Session Host) servers, client sessions, and processes.

To retrieve the names of all the RD Session Host servers in a domain, call the [**NetServerEnum**](/windows/desktop/api/lmserver/nf-lmserver-netserverenum) function to enumerate servers of the SV\_TYPE\_TERMINALSERVER type. To open a handle to a specific RD Session Host server, pass the server name in a call to the [**WTSOpenServer**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsopenservera) function. When you have finished using the handle, release it by calling the [**WTSCloseServer**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtscloseserver) function.

You can use the handle returned by **WTSOpenServer** to perform the following operations on the server.



| Function                                                         | Operation                                                                                                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WTSDisconnectSession**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsdisconnectsession)             | Disconnects the client from a specified session. The session remains active and the user can log on again to connect to the same session.                                                                         |
| [**WTSEnumerateSessions**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsenumeratesessionsa)             | Returns a list of sessions on the specified RD Session Host server.                                                                                                                                               |
| [**WTSEnumerateProcesses**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsenumerateprocessesa)           | Returns a list of processes on the specified RD Session Host server.                                                                                                                                              |
| [**WTSLogoffSession**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtslogoffsession)                     | Logs off the specified session.                                                                                                                                                                                   |
| [**WTSQuerySessionInformation**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsquerysessioninformationa) | Returns information about the specified session on the specified RD Session Host server.                                                                                                                          |
| [**WTSSendMessage**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtssendmessagea)                         | Shows a message box on the client display of a specified session.                                                                                                                                                 |
| [**WTSShutdownSystem**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsshutdownsystem)                   | Shuts down and optionally restarts a specified RD Session Host server.                                                                                                                                            |
| [**WTSTerminateProcess**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsterminateprocess)               | Terminates a specified process on a specified RD Session Host server.                                                                                                                                             |
| [**WTSVirtualChannelOpen**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopen)           | Opens a handle to the server end of a specified virtual channel. For more information about virtual channels, see [Using Remote Desktop Services Virtual Channels](using-terminal-services-virtual-channels.md). |
| [**WTSWaitSystemEvent**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtswaitsystemevent)                 | Waits for an event, such as the creation of a client session or a user logging on to the RD Session Host server.                                                                                                  |



 

Several of these functions allocate buffers to return information to the caller. When you have finished using the buffer, free it by calling the [**WTSFreeMemory**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsfreememory) function.

 

 