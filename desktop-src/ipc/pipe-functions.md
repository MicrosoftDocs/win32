---
Description: The following function is used with anonymous pipes.
ms.assetid: 9e80783e-9641-4cbd-9c28-a8efe6b9efaa
title: Pipe Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pipe Functions

The following function is used with anonymous pipes.



| Function                         | Description                |
|----------------------------------|----------------------------|
| [**CreatePipe**](/windows/win32/Winbase/?branch=master) | Creates an anonymous pipe. |



 

The following functions are used with named pipes.



| Function                                                                 | Description                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallNamedPipe**](/windows/win32/Winbase/nf-winbase-callnamedpipea?branch=master)                                   | Connects to a message-type pipe, writes to and reads from the pipe, and then closes the pipe.                                                                                                                                       |
| [**ConnectNamedPipe**](/windows/win32/Winbase/?branch=master)                             | Enables a named pipe server process to wait for a client process to connect to an instance of a named pipe.                                                                                                                         |
| [**CreateNamedPipe**](/windows/win32/Winbase/nf-winbase-createnamedpipea?branch=master)                               | Creates an instance of a named pipe and returns a handle for subsequent pipe operations. A client process connects to a named pipe by using the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or [**CallNamedPipe**](/windows/win32/Winbase/nf-winbase-callnamedpipea?branch=master) function. |
| [**DisconnectNamedPipe**](/windows/win32/Winbase/?branch=master)                       | Disconnects the server end of a named pipe instance from a client process.                                                                                                                                                          |
| [**GetNamedPipeClientComputerName**](/windows/win32/Winbase/nf-winbase-getnamedpipeclientcomputernamea?branch=master) | Retrieves the client computer name for the specified named pipe.                                                                                                                                                                    |
| [**GetNamedPipeClientProcessId**](/windows/win32/Winbase/nf-winbase-getnamedpipeclientprocessid?branch=master)       | Retrieves the client process identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeClientSessionId**](/windows/win32/Winbase/nf-winbase-getnamedpipeclientsessionid?branch=master)       | Retrieves the client session identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeHandleState**](/windows/win32/Winbase/nf-winbase-getnamedpipehandlestatea?branch=master)               | Retrieves information about a specified named pipe.                                                                                                                                                                                 |
| [**GetNamedPipeInfo**](/windows/win32/Winbase/?branch=master)                             | Retrieves information about the specified named pipe.                                                                                                                                                                               |
| [**GetNamedPipeServerProcessId**](/windows/win32/Winbase/nf-winbase-getnamedpipeserverprocessid?branch=master)       | Retrieves the server process identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeServerSessionId**](/windows/win32/Winbase/nf-winbase-getnamedpipeserversessionid?branch=master)       | Retrieves the server session identifier for the specified named pipe.                                                                                                                                                               |
| [**ImpersonateNamedPipeClient**](https://msdn.microsoft.com/library/windows/desktop/aa378618)    | Impersonates a named-pipe client application.                                                                                                                                                                                       |
| [**PeekNamedPipe**](/windows/win32/Winbase/?branch=master)                                   | Copies data from a named or anonymous pipe into a buffer without removing it from the pipe.                                                                                                                                         |
| [**SetNamedPipeHandleState**](/windows/win32/Winbase/?branch=master)               | Sets the read mode and the blocking mode of the specified named pipe.                                                                                                                                                               |
| [**TransactNamedPipe**](/windows/win32/Winbase/?branch=master)                           | Combines the functions that write a message to and read a message from the specified named pipe into a single network operation.                                                                                                    |
| [**WaitNamedPipe**](/windows/win32/Winbase/nf-winbase-waitnamedpipea?branch=master)                                   | Waits until either a time-out interval elapses or an instance of the specified named pipe is available for a connection.                                                                                                            |



 

 

 



