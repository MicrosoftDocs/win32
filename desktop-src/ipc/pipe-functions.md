---
Description: The following function is used with anonymous pipes.
ms.assetid: 9e80783e-9641-4cbd-9c28-a8efe6b9efaa
title: Pipe Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Pipe Functions

The following function is used with anonymous pipes.



| Function                         | Description                |
|----------------------------------|----------------------------|
| [**CreatePipe**](/windows/desktop/api/Winbase/) | Creates an anonymous pipe. |



 

The following functions are used with named pipes.



| Function                                                                 | Description                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-callnamedpipea)                                   | Connects to a message-type pipe, writes to and reads from the pipe, and then closes the pipe.                                                                                                                                       |
| [**ConnectNamedPipe**](/windows/desktop/api/Winbase/)                             | Enables a named pipe server process to wait for a client process to connect to an instance of a named pipe.                                                                                                                         |
| [**CreateNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-createnamedpipea)                               | Creates an instance of a named pipe and returns a handle for subsequent pipe operations. A client process connects to a named pipe by using the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or [**CallNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-callnamedpipea) function. |
| [**DisconnectNamedPipe**](/windows/desktop/api/Winbase/)                       | Disconnects the server end of a named pipe instance from a client process.                                                                                                                                                          |
| [**GetNamedPipeClientComputerName**](/windows/desktop/api/Winbase/nf-winbase-getnamedpipeclientcomputernamea) | Retrieves the client computer name for the specified named pipe.                                                                                                                                                                    |
| [**GetNamedPipeClientProcessId**](/windows/desktop/api/Winbase/nf-winbase-getnamedpipeclientprocessid)       | Retrieves the client process identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeClientSessionId**](/windows/desktop/api/Winbase/nf-winbase-getnamedpipeclientsessionid)       | Retrieves the client session identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeHandleState**](/windows/desktop/api/Winbase/nf-winbase-getnamedpipehandlestatea)               | Retrieves information about a specified named pipe.                                                                                                                                                                                 |
| [**GetNamedPipeInfo**](/windows/desktop/api/Winbase/)                             | Retrieves information about the specified named pipe.                                                                                                                                                                               |
| [**GetNamedPipeServerProcessId**](/windows/desktop/api/Winbase/nf-winbase-getnamedpipeserverprocessid)       | Retrieves the server process identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeServerSessionId**](/windows/desktop/api/Winbase/nf-winbase-getnamedpipeserversessionid)       | Retrieves the server session identifier for the specified named pipe.                                                                                                                                                               |
| [**ImpersonateNamedPipeClient**](https://msdn.microsoft.com/library/windows/desktop/aa378618)    | Impersonates a named-pipe client application.                                                                                                                                                                                       |
| [**PeekNamedPipe**](/windows/desktop/api/Winbase/)                                   | Copies data from a named or anonymous pipe into a buffer without removing it from the pipe.                                                                                                                                         |
| [**SetNamedPipeHandleState**](/windows/desktop/api/Winbase/)               | Sets the read mode and the blocking mode of the specified named pipe.                                                                                                                                                               |
| [**TransactNamedPipe**](/windows/desktop/api/Winbase/)                           | Combines the functions that write a message to and read a message from the specified named pipe into a single network operation.                                                                                                    |
| [**WaitNamedPipe**](/windows/desktop/api/Winbase/nf-winbase-waitnamedpipea)                                   | Waits until either a time-out interval elapses or an instance of the specified named pipe is available for a connection.                                                                                                            |



 

 

 



