---
title: Client Shell API Core Functions
description: The following table provides an overview of the core functions for the Windows Remote Management (WinRM) Client Shell API.
ms.assetid: cd0e6b55-03e8-4ebe-aea8-35d268cdb18c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Client Shell API Core Functions

The following table provides an overview of the core functions for the Windows Remote Management (WinRM) Client Shell API.



| Core functions                                                   | Description                                                                                                                                                                     |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSManCloseCommand**](/windows/desktop/api/Wsman/nf-wsman-wsmanclosecommand)                   | Closes a command.                                                                                                                                                               |
| [**WSManCloseOperation**](/windows/desktop/api/Wsman/nf-wsman-wsmancloseoperation)               | Closes an operation.                                                                                                                                                            |
| [**WSManCloseSession**](/windows/desktop/api/Wsman/nf-wsman-wsmanclosesession)                   | Closes a WinRM session.                                                                                                                                                         |
| [**WSManCloseShell**](/windows/desktop/api/Wsman/nf-wsman-wsmancloseshell)                       | Closes a shell object.                                                                                                                                                          |
| [**WSManConnectShell**](/windows/desktop/api/Wsman/nf-wsman-wsmanconnectshell)                   | Connects to an existing server session.                                                                                                                                         |
| [**WSManConnectShellCommand**](/windows/desktop/api/Wsman/nf-wsman-wsmanconnectshellcommand)     | Connects to an existing command running in a shell.                                                                                                                             |
| [**WSManCreateSession**](/windows/desktop/api/Wsman/nf-wsman-wsmancreatesession)                 | Creates a WinRM session.                                                                                                                                                        |
| [**WSManCreateShell**](/windows/desktop/api/Wsman/nf-wsman-wsmancreateshell)                     | Creates a shell object.                                                                                                                                                         |
| [**WSManCreateShellEx**](/windows/desktop/api/Wsman/nf-wsman-wsmancreateshellex)                 | Creates a shell object by using the same functionality as the [**WSManCreateShell**](/windows/desktop/api/Wsman/nf-wsman-wsmancreateshell) function, with the addition of a client-specified shell ID.          |
| [**WSManDeinitialize**](/windows/desktop/api/Wsman/nf-wsman-wsmandeinitialize)                   | Deinitializes the WinRM client stack.                                                                                                                                           |
| [**WSManDisconnectShell**](/windows/desktop/api/Wsman/nf-wsman-wsmandisconnectshell)             | Disconnects the network connection of an active shell and its associated commands.                                                                                              |
| [**WSManInitialize**](/windows/desktop/api/Wsman/nf-wsman-wsmaninitialize)                       | Initializes WinRM.                                                                                                                                                              |
| [**WSManReceiveShellOutput**](/windows/desktop/api/Wsman/nf-wsman-wsmanreceiveshelloutput)       | Receives shell output.                                                                                                                                                          |
| [**WSManReconnectShell**](/windows/desktop/api/Wsman/nf-wsman-wsmanreconnectshell)               | Reconnects a previously disconnected shell session. To reconnect the shell session's associated commands, use [**WSManReconnectShellCommand**](/windows/desktop/api/Wsman/nf-wsman-wsmanreconnectshellcommand). |
| [**WSManReconnectShellCommand**](/windows/desktop/api/Wsman/nf-wsman-wsmanreconnectshellcommand) | Reconnects a previously disconnected command.                                                                                                                                   |
| [**WSManRunShellCommand**](/windows/desktop/api/Wsman/nf-wsman-wsmanrunshellcommand)             | Runs a shell command.                                                                                                                                                           |
| [**WSManRunShellCommandEx**](/windows/desktop/api/Wsman/nf-wsman-wsmanrunshellcommandex)         | Provides the same functionality as the [**WSManRunShellCommand**](/windows/desktop/api/Wsman/nf-wsman-wsmanrunshellcommand) function, with the addition of a command ID option.                                 |
| [**WSManSendShellInput**](/windows/desktop/api/Wsman/nf-wsman-wsmansendshellinput)               | Sends input to a shell.                                                                                                                                                         |
| [**WSManSignalShell**](/windows/desktop/api/Wsman/nf-wsman-wsmansignalshell)                     | Signals a shell.                                                                                                                                                                |



 

 

 




