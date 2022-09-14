---
title: Client/Server application guidelines
description: Client/server applications must not assume that a single computer connection is equivalent to a single user session.
ms.assetid: 69822ef1-eca8-4302-b014-8e5894d52109
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Client/Server application guidelines

Client/server applications must not assume that a single computer connection is equivalent to a single user session. This is a special case of the issue discussed in [IP Addresses and Computer Names](ip-addresses-and-computer-names.md).

To uniquely identify a client/server connection, each client module must use a unique name or identifier. Applications can use named objects or pipes, sockets, or other IPC methods. For more information, see [Kernel Object Namespaces](kernel-object-namespaces.md).

To be Remote Desktop Services compatible, the server module in a client/server application must be able to handle multiple clients connecting from the same computer. To accomplish this, the server module must accept client connections through a well-defined global interface, such as RPC or named pipes. The server and client must negotiate a different communication channel for each user session. The client must establish a connection to the server by using protocols that easily support this type of operation, such as TCP/IP, where a different socket connection can be used for each client application.

The client module can call the [**ProcessIdToSessionId**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-processidtosessionid) function to retrieve the identifier of its Remote Desktop Services session. The client then uses some form of interprocess communication to pass its session identifier to the server module. The client and server modules can then use the session identifier to set up a private communication channel. For example, the server module can use a session identifier to access objects in the session's namespace for kernel objects.

Furthermore, the server module can use the session identifier in a [**WTSQuerySessionInformation**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsquerysessioninformationa) call to retrieve additional information about the client. The server module can also use the session identifier in a [**WTSSendMessage**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtssendmessagea) call to display a message on the client terminal. The server module can also create two events to monitor client connection to and disconnection from a session. However, it must be registered on the Remote Desktop Session Host (RD Session Host) server to do this. For more information, see [Monitoring Session Connections and Disconnections](monitoring-session-connections-and-disconnections.md).

Prompts for user input are a potential source of problems for client/server applications. For example, if a service calls the [**MessageBox**](/windows/desktop/api/winuser/nf-winuser-messagebox) function, the message box is displayed on the desktop of the RD Session Host server, not on the client desktop. To display a message on a client desktop, the service can call the [**WtsSendMessage**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtssendmessagea) function. Alternatively, the service can request input from the client module, and the client module can display the user interface and send the resulting input back to the service.

Processes spawned from multiple sessions can send data to and receive data from each other through the use of shared memory blocks. For more information, see [Creating Named Shared Memory](/windows/desktop/Memory/creating-named-shared-memory). Shared memory cannot be used under the following conditions:

-   The processes using the shared memory block were spawned by multiple sessions.
-   The sessions share the same user authentication credential.

 

 