---
title: Client Shell API Core Functions
description: The following table provides an overview of the core functions for the Windows Remote Management (WinRM) Client Shell API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cd0e6b55-03e8-4ebe-aea8-35d268cdb18c
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Client Shell API Core Functions

The following table provides an overview of the core functions for the Windows Remote Management (WinRM) Client Shell API.



| Core functions                                                   | Description                                                                                                                                                                     |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSManCloseCommand**](/windows/win32/Wsman/nf-wsman-wsmanclosecommand?branch=master)                   | Closes a command.                                                                                                                                                               |
| [**WSManCloseOperation**](/windows/win32/Wsman/nf-wsman-wsmancloseoperation?branch=master)               | Closes an operation.                                                                                                                                                            |
| [**WSManCloseSession**](/windows/win32/Wsman/nf-wsman-wsmanclosesession?branch=master)                   | Closes a WinRM session.                                                                                                                                                         |
| [**WSManCloseShell**](/windows/win32/Wsman/nf-wsman-wsmancloseshell?branch=master)                       | Closes a shell object.                                                                                                                                                          |
| [**WSManConnectShell**](/windows/win32/Wsman/nf-wsman-wsmanconnectshell?branch=master)                   | Connects to an existing server session.                                                                                                                                         |
| [**WSManConnectShellCommand**](/windows/win32/Wsman/nf-wsman-wsmanconnectshellcommand?branch=master)     | Connects to an existing command running in a shell.                                                                                                                             |
| [**WSManCreateSession**](/windows/win32/Wsman/nf-wsman-wsmancreatesession?branch=master)                 | Creates a WinRM session.                                                                                                                                                        |
| [**WSManCreateShell**](/windows/win32/Wsman/nf-wsman-wsmancreateshell?branch=master)                     | Creates a shell object.                                                                                                                                                         |
| [**WSManCreateShellEx**](/windows/win32/Wsman/nf-wsman-wsmancreateshellex?branch=master)                 | Creates a shell object by using the same functionality as the [**WSManCreateShell**](/windows/win32/Wsman/nf-wsman-wsmancreateshell?branch=master) function, with the addition of a client-specified shell ID.          |
| [**WSManDeinitialize**](/windows/win32/Wsman/nf-wsman-wsmandeinitialize?branch=master)                   | Deinitializes the WinRM client stack.                                                                                                                                           |
| [**WSManDisconnectShell**](/windows/win32/Wsman/nf-wsman-wsmandisconnectshell?branch=master)             | Disconnects the network connection of an active shell and its associated commands.                                                                                              |
| [**WSManInitialize**](/windows/win32/Wsman/nf-wsman-wsmaninitialize?branch=master)                       | Initializes WinRM.                                                                                                                                                              |
| [**WSManReceiveShellOutput**](/windows/win32/Wsman/nf-wsman-wsmanreceiveshelloutput?branch=master)       | Receives shell output.                                                                                                                                                          |
| [**WSManReconnectShell**](/windows/win32/Wsman/nf-wsman-wsmanreconnectshell?branch=master)               | Reconnects a previously disconnected shell session. To reconnect the shell session's associated commands, use [**WSManReconnectShellCommand**](/windows/win32/Wsman/nf-wsman-wsmanreconnectshellcommand?branch=master). |
| [**WSManReconnectShellCommand**](/windows/win32/Wsman/nf-wsman-wsmanreconnectshellcommand?branch=master) | Reconnects a previously disconnected command.                                                                                                                                   |
| [**WSManRunShellCommand**](/windows/win32/Wsman/nf-wsman-wsmanrunshellcommand?branch=master)             | Runs a shell command.                                                                                                                                                           |
| [**WSManRunShellCommandEx**](/windows/win32/Wsman/nf-wsman-wsmanrunshellcommandex?branch=master)         | Provides the same functionality as the [**WSManRunShellCommand**](/windows/win32/Wsman/nf-wsman-wsmanrunshellcommand?branch=master) function, with the addition of a command ID option.                                 |
| [**WSManSendShellInput**](/windows/win32/Wsman/nf-wsman-wsmansendshellinput?branch=master)               | Sends input to a shell.                                                                                                                                                         |
| [**WSManSignalShell**](/windows/win32/Wsman/nf-wsman-wsmansignalshell?branch=master)                     | Signals a shell.                                                                                                                                                                |



 

 

 




