---
title: Server and Workstation Transport Functions
description: The network management server and workstation transport functions handle binding and unbinding of transport protocols to and from the server and redirector.
ms.assetid: 64342e21-98f1-42d3-b541-46b826391fad
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Server and Workstation Transport Functions

The network management server and workstation transport functions handle binding and unbinding of transport protocols to and from the server and redirector. The server transport functions deal with transport protocols managed by the server; the workstation transport functions deal with transport protocols managed by the redirector.

File sharing between a transport device and a server has two components:

-   The server computer where the files reside
-   A Server Message Block (SMB) client that accesses the files

The client computer communicates with the server computer over a local area network using a transport protocol; for example, TCP or XNS. The client sends requests to the server to retrieve data. The software on the client computer that generates the file requests is called the *redirector* because it redirects local file requests to the server computer. The software on the computer that receives and acts on the file requests is called the *server* because it serves the clients. The format specific to these requests is called the SMB protocol.

The server transport functions are listed following.



| Function                                                     | Description                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetServerComputerNameAdd**](/windows/win32/Lmserver/nf-lmserver-netservercomputernameadd?branch=master) | Binds an emulated server name to each of the transport protocols on which a server is active. (Combines the functionality of the [**NetServerTransportEnum**](/windows/win32/Lmserver/nf-lmserver-netservertransportenum?branch=master) function and the [**NetServerTransportAddEx**](/windows/win32/Lmserver/nf-lmserver-netservertransportaddex?branch=master) function.)                                            |
| [**NetServerComputerNameDel**](/windows/win32/Lmserver/nf-lmserver-netservercomputernamedel?branch=master) | Disconnects each network transport protocol from an emulated server name set by a previous call to the **NetServerComputerNameAdd** function.                                                                                                                                                                               |
| [**NetServerTransportAdd**](/windows/win32/Lmserver/nf-lmserver-netservertransportadd?branch=master)       | Binds the specified server to the transport protocol. (This function supports only the [**SERVER\_TRANSPORT\_INFO\_0**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_0?branch=master) information level.)                                                                                                                                                |
| [**NetServerTransportAddEx**](/windows/win32/Lmserver/nf-lmserver-netservertransportaddex?branch=master)   | Binds the specified server to the transport protocol. (This extended function supports the [**SERVER\_TRANSPORT\_INFO\_1**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_1?branch=master), [**SERVER\_TRANSPORT\_INFO\_2**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_2?branch=master), and [**SERVER\_TRANSPORT\_INFO\_3**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_3?branch=master) information levels.) |
| [**NetServerTransportDel**](/windows/win32/Lmserver/nf-lmserver-netservertransportdel?branch=master)       | Disconnects the transport protocol from the server.                                                                                                                                                                                                                                                                         |
| [**NetServerTransportEnum**](/windows/win32/Lmserver/nf-lmserver-netservertransportenum?branch=master)     | Enumerates the transport protocols managed by the server.                                                                                                                                                                                                                                                                   |



 

Server transport functions are available at the following information levels:

-   [**SERVER\_TRANSPORT\_INFO\_0**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_0?branch=master)
-   [**SERVER\_TRANSPORT\_INFO\_1**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_1?branch=master)
-   [**SERVER\_TRANSPORT\_INFO\_2**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_2?branch=master)
-   [**SERVER\_TRANSPORT\_INFO\_3**](/windows/win32/Lmserver/ns-lmserver-_server_transport_info_3?branch=master)

The workstation transport functions perform equivalent operations for the workstation.

**Windows Server 2003 and Windows XP/2000:** The redirector does not support the [**NetWkstaTransportAdd**](/windows/win32/lmwksta/nf-lmwksta-netwkstatransportadd?branch=master) function or the [**NetWkstaTransportDel**](/windows/win32/lmwksta/nf-lmwksta-netwkstatransportdel?branch=master) function. You can change the default settings for transport protocols manually through the **Local Area Connection Properties** dialog box in the **Network and Dial-Up Connections** folder.

The workstation transport functions are listed following.



| Function                                               | Description                                                       |
|--------------------------------------------------------|-------------------------------------------------------------------|
| [**NetWkstaTransportAdd**](/windows/win32/lmwksta/nf-lmwksta-netwkstatransportadd?branch=master)   | Connects the redirector to the transport protocol.                |
| [**NetWkstaTransportDel**](/windows/win32/lmwksta/nf-lmwksta-netwkstatransportdel?branch=master)   | Disconnects the transport protocol from the redirector.           |
| [**NetWkstaTransportEnum**](/windows/win32/Lmwksta/nf-lmwksta-netwkstatransportenum?branch=master) | Lists the transport protocols that are managed by the redirector. |



 

Workstation transport functions are available at one information level:

-   [**WKSTA\_TRANSPORT\_INFO\_0**](/windows/win32/Lmwksta/ns-lmwksta-_wksta_transport_info_0?branch=master)

 

 




