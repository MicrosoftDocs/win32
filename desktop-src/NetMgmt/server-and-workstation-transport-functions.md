---
title: Server and Workstation Transport Functions
description: The network management server and workstation transport functions handle binding and unbinding of transport protocols to and from the server and redirector.
ms.assetid: 64342e21-98f1-42d3-b541-46b826391fad
ms.topic: article
ms.date: 05/31/2018
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
| [**NetServerComputerNameAdd**](/windows/desktop/api/Lmserver/nf-lmserver-netservercomputernameadd) | Binds an emulated server name to each of the transport protocols on which a server is active. (Combines the functionality of the [**NetServerTransportEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportenum) function and the [**NetServerTransportAddEx**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportaddex) function.)                                            |
| [**NetServerComputerNameDel**](/windows/desktop/api/Lmserver/nf-lmserver-netservercomputernamedel) | Disconnects each network transport protocol from an emulated server name set by a previous call to the **NetServerComputerNameAdd** function.                                                                                                                                                                               |
| [**NetServerTransportAdd**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportadd)       | Binds the specified server to the transport protocol. (This function supports only the [**SERVER\_TRANSPORT\_INFO\_0**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_0) information level.)                                                                                                                                                |
| [**NetServerTransportAddEx**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportaddex)   | Binds the specified server to the transport protocol. (This extended function supports the [**SERVER\_TRANSPORT\_INFO\_1**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_1), [**SERVER\_TRANSPORT\_INFO\_2**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_2), and [**SERVER\_TRANSPORT\_INFO\_3**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_3) information levels.) |
| [**NetServerTransportDel**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportdel)       | Disconnects the transport protocol from the server.                                                                                                                                                                                                                                                                         |
| [**NetServerTransportEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netservertransportenum)     | Enumerates the transport protocols managed by the server.                                                                                                                                                                                                                                                                   |



 

Server transport functions are available at the following information levels:

-   [**SERVER\_TRANSPORT\_INFO\_0**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_0)
-   [**SERVER\_TRANSPORT\_INFO\_1**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_1)
-   [**SERVER\_TRANSPORT\_INFO\_2**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_2)
-   [**SERVER\_TRANSPORT\_INFO\_3**](/windows/desktop/api/Lmserver/ns-lmserver-server_transport_info_3)

The workstation transport functions perform equivalent operations for the workstation.

**Windows Server 2003 and Windows XP/2000:** The redirector does not support the [**NetWkstaTransportAdd**](/windows/desktop/api/lmwksta/nf-lmwksta-netwkstatransportadd) function or the [**NetWkstaTransportDel**](/windows/desktop/api/lmwksta/nf-lmwksta-netwkstatransportdel) function. You can change the default settings for transport protocols manually through the **Local Area Connection Properties** dialog box in the **Network and Dial-Up Connections** folder.

The workstation transport functions are listed following.



| Function                                               | Description                                                       |
|--------------------------------------------------------|-------------------------------------------------------------------|
| [**NetWkstaTransportAdd**](/windows/desktop/api/lmwksta/nf-lmwksta-netwkstatransportadd)   | Connects the redirector to the transport protocol.                |
| [**NetWkstaTransportDel**](/windows/desktop/api/lmwksta/nf-lmwksta-netwkstatransportdel)   | Disconnects the transport protocol from the redirector.           |
| [**NetWkstaTransportEnum**](/windows/desktop/api/Lmwksta/nf-lmwksta-netwkstatransportenum) | Lists the transport protocols that are managed by the redirector. |



 

Workstation transport functions are available at one information level:

-   [**WKSTA\_TRANSPORT\_INFO\_0**](/windows/desktop/api/Lmwksta/ns-lmwksta-wksta_transport_info_0)

 

 




