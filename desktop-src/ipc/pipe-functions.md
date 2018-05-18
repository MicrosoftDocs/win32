---
Description: 'The following function is used with anonymous pipes.'
ms.assetid: '9e80783e-9641-4cbd-9c28-a8efe6b9efaa'
title: Pipe Functions
---

# Pipe Functions

The following function is used with anonymous pipes.



| Function                         | Description                |
|----------------------------------|----------------------------|
| [**CreatePipe**](createpipe.md) | Creates an anonymous pipe. |



 

The following functions are used with named pipes.



| Function                                                                 | Description                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallNamedPipe**](callnamedpipe.md)                                   | Connects to a message-type pipe, writes to and reads from the pipe, and then closes the pipe.                                                                                                                                       |
| [**ConnectNamedPipe**](connectnamedpipe.md)                             | Enables a named pipe server process to wait for a client process to connect to an instance of a named pipe.                                                                                                                         |
| [**CreateNamedPipe**](createnamedpipe.md)                               | Creates an instance of a named pipe and returns a handle for subsequent pipe operations. A client process connects to a named pipe by using the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or [**CallNamedPipe**](callnamedpipe.md) function. |
| [**DisconnectNamedPipe**](disconnectnamedpipe.md)                       | Disconnects the server end of a named pipe instance from a client process.                                                                                                                                                          |
| [**GetNamedPipeClientComputerName**](getnamedpipeclientcomputername.md) | Retrieves the client computer name for the specified named pipe.                                                                                                                                                                    |
| [**GetNamedPipeClientProcessId**](getnamedpipeclientprocessid.md)       | Retrieves the client process identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeClientSessionId**](getnamedpipeclientsessionid.md)       | Retrieves the client session identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeHandleState**](getnamedpipehandlestate.md)               | Retrieves information about a specified named pipe.                                                                                                                                                                                 |
| [**GetNamedPipeInfo**](getnamedpipeinfo.md)                             | Retrieves information about the specified named pipe.                                                                                                                                                                               |
| [**GetNamedPipeServerProcessId**](getnamedpipeserverprocessid.md)       | Retrieves the server process identifier for the specified named pipe.                                                                                                                                                               |
| [**GetNamedPipeServerSessionId**](getnamedpipeserversessionid.md)       | Retrieves the server session identifier for the specified named pipe.                                                                                                                                                               |
| [**ImpersonateNamedPipeClient**](https://msdn.microsoft.com/library/windows/desktop/aa378618)    | Impersonates a named-pipe client application.                                                                                                                                                                                       |
| [**PeekNamedPipe**](peeknamedpipe.md)                                   | Copies data from a named or anonymous pipe into a buffer without removing it from the pipe.                                                                                                                                         |
| [**SetNamedPipeHandleState**](setnamedpipehandlestate.md)               | Sets the read mode and the blocking mode of the specified named pipe.                                                                                                                                                               |
| [**TransactNamedPipe**](transactnamedpipe.md)                           | Combines the functions that write a message to and read a message from the specified named pipe into a single network operation.                                                                                                    |
| [**WaitNamedPipe**](waitnamedpipe.md)                                   | Waits until either a time-out interval elapses or an instance of the specified named pipe is available for a connection.                                                                                                            |



 

 

 



