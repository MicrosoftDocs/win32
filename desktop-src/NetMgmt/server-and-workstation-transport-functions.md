---
title: Server and Workstation Transport Functions
description: The network management server and workstation transport functions handle binding and unbinding of transport protocols to and from the server and redirector.
ms.assetid: '64342e21-98f1-42d3-b541-46b826391fad'
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
| [**NetServerComputerNameAdd**](netservercomputernameadd.md) | Binds an emulated server name to each of the transport protocols on which a server is active. (Combines the functionality of the [**NetServerTransportEnum**](netservertransportenum.md) function and the [**NetServerTransportAddEx**](netservertransportaddex.md) function.)                                            |
| [**NetServerComputerNameDel**](netservercomputernamedel.md) | Disconnects each network transport protocol from an emulated server name set by a previous call to the **NetServerComputerNameAdd** function.                                                                                                                                                                               |
| [**NetServerTransportAdd**](netservertransportadd.md)       | Binds the specified server to the transport protocol. (This function supports only the [**SERVER\_TRANSPORT\_INFO\_0**](server-transport-info-0-str.md) information level.)                                                                                                                                                |
| [**NetServerTransportAddEx**](netservertransportaddex.md)   | Binds the specified server to the transport protocol. (This extended function supports the [**SERVER\_TRANSPORT\_INFO\_1**](server-transport-info-1-str.md), [**SERVER\_TRANSPORT\_INFO\_2**](server-transport-info-2-str.md), and [**SERVER\_TRANSPORT\_INFO\_3**](server-transport-info-3-str.md) information levels.) |
| [**NetServerTransportDel**](netservertransportdel.md)       | Disconnects the transport protocol from the server.                                                                                                                                                                                                                                                                         |
| [**NetServerTransportEnum**](netservertransportenum.md)     | Enumerates the transport protocols managed by the server.                                                                                                                                                                                                                                                                   |



 

Server transport functions are available at the following information levels:

-   [**SERVER\_TRANSPORT\_INFO\_0**](server-transport-info-0-str.md)
-   [**SERVER\_TRANSPORT\_INFO\_1**](server-transport-info-1-str.md)
-   [**SERVER\_TRANSPORT\_INFO\_2**](server-transport-info-2-str.md)
-   [**SERVER\_TRANSPORT\_INFO\_3**](server-transport-info-3-str.md)

The workstation transport functions perform equivalent operations for the workstation.

**Windows Server 2003 and Windows XP/2000:** The redirector does not support the [**NetWkstaTransportAdd**](netwkstatransportadd.md) function or the [**NetWkstaTransportDel**](netwkstatransportdel.md) function. You can change the default settings for transport protocols manually through the **Local Area Connection Properties** dialog box in the **Network and Dial-Up Connections** folder.

The workstation transport functions are listed following.



| Function                                               | Description                                                       |
|--------------------------------------------------------|-------------------------------------------------------------------|
| [**NetWkstaTransportAdd**](netwkstatransportadd.md)   | Connects the redirector to the transport protocol.                |
| [**NetWkstaTransportDel**](netwkstatransportdel.md)   | Disconnects the transport protocol from the redirector.           |
| [**NetWkstaTransportEnum**](netwkstatransportenum.md) | Lists the transport protocols that are managed by the redirector. |



 

Workstation transport functions are available at one information level:

-   [**WKSTA\_TRANSPORT\_INFO\_0**](wksta-transport-info-0-str.md)

 

 




