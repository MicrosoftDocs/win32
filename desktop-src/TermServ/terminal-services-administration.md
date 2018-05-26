---
title: Remote Desktop Services Administration
description: The Remote Desktop Services API enables you to enumerate and manage Remote Desktop Session Host (RD Session Host) servers, client sessions, and processes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 85a9ed9d-79d6-4011-93a4-00847c689747
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Services Administration

The Remote Desktop Services API enables you to enumerate and manage Remote Desktop Session Host (RD Session Host) servers, client sessions, and processes.

To retrieve the names of all the RD Session Host servers in a domain, call the [**NetServerEnum**](https://msdn.microsoft.com/library/windows/desktop/aa370623) function to enumerate servers of the SV\_TYPE\_TERMINALSERVER type. To open a handle to a specific RD Session Host server, pass the server name in a call to the [**WTSOpenServer**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsopenservera?branch=master) function. When you have finished using the handle, release it by calling the [**WTSCloseServer**](/windows/win32/Wtsapi32/nf-wtsapi32-wtscloseserver?branch=master) function.

You can use the handle returned by **WTSOpenServer** to perform the following operations on the server.



| Function                                                         | Operation                                                                                                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WTSDisconnectSession**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsdisconnectsession?branch=master)             | Disconnects the client from a specified session. The session remains active and the user can log on again to connect to the same session.                                                                         |
| [**WTSEnumerateSessions**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumeratesessionsa?branch=master)             | Returns a list of sessions on the specified RD Session Host server.                                                                                                                                               |
| [**WTSEnumerateProcesses**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumerateprocessesa?branch=master)           | Returns a list of processes on the specified RD Session Host server.                                                                                                                                              |
| [**WTSLogoffSession**](/windows/win32/Wtsapi32/nf-wtsapi32-wtslogoffsession?branch=master)                     | Logs off the specified session.                                                                                                                                                                                   |
| [**WTSQuerySessionInformation**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsquerysessioninformationa?branch=master) | Returns information about the specified session on the specified RD Session Host server.                                                                                                                          |
| [**WTSSendMessage**](/windows/win32/Wtsapi32/nf-wtsapi32-wtssendmessagea?branch=master)                         | Shows a message box on the client display of a specified session.                                                                                                                                                 |
| [**WTSShutdownSystem**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsshutdownsystem?branch=master)                   | Shuts down and optionally restarts a specified RD Session Host server.                                                                                                                                            |
| [**WTSTerminateProcess**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsterminateprocess?branch=master)               | Terminates a specified process on a specified RD Session Host server.                                                                                                                                             |
| [**WTSVirtualChannelOpen**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopen?branch=master)           | Opens a handle to the server end of a specified virtual channel. For more information about virtual channels, see [Using Remote Desktop Services Virtual Channels](using-terminal-services-virtual-channels.md). |
| [**WTSWaitSystemEvent**](/windows/win32/Wtsapi32/nf-wtsapi32-wtswaitsystemevent?branch=master)                 | Waits for an event, such as the creation of a client session or a user logging on to the RD Session Host server.                                                                                                  |



 

Several of these functions allocate buffers to return information to the caller. When you have finished using the buffer, free it by calling the [**WTSFreeMemory**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsfreememory?branch=master) function.

 

 




