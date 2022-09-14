---
title: Server Functions (Network Management)
description: The network management server functions perform administrative tasks on a local or remote server. The server functions are listed following.
ms.assetid: 43e1285b-8c86-4af4-9834-fcd5ee8aceb8
ms.topic: article
ms.date: 05/31/2018
---

# Server Functions (Network Management)

The network management server functions perform administrative tasks on a local or remote server. The server functions are listed following.



| Function                                       | Description                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------|
| [**NetServerDiskEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netserverdiskenum) | Returns a list of local disk drives on a server.                                   |
| [**NetServerEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netserverenum)         | Lists all visible servers of a particular type (or types) in the specified domain. |
| [**NetServerGetInfo**](/windows/desktop/api/Lmserver/nf-lmserver-netservergetinfo)   | Returns configuration information about a specified server.                        |
| [**NetServerSetInfo**](/windows/desktop/api/Lmserver/nf-lmserver-netserversetinfo)   | Sets the operating parameters for a server.                                        |



 

Only a user or application with admin group membership on a local or remote server can perform administrative tasks on that server to control the server's operation, user access, and resource sharing. The low-level parameters that affect a server's operation can be examined and modified by calling the [**NetServerGetInfo**](/windows/desktop/api/Lmserver/nf-lmserver-netservergetinfo) and [**NetServerSetInfo**](/windows/desktop/api/Lmserver/nf-lmserver-netserversetinfo) functions. These parameters are defined in the server's LANMAN.INI file.

Most network management server functions execute only on a remote server. The [**NetServerEnum**](/windows/desktop/api/Lmserver/nf-lmserver-netserverenum) function executes on either a local workstation or a remote server. If you attempt to execute other server functions on a local workstation, the functions return the error NERR\_RemoteOnly.

Server-specific information is available at the following levels:

-   [**SERVER\_INFO\_100**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_100)
-   [**SERVER\_INFO\_101**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_101)
-   [**SERVER\_INFO\_102**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_102)
-   [**SERVER\_INFO\_402**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_402)
-   [**SERVER\_INFO\_403**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_403)
-   [**SERVER\_INFO\_1501**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1501)
-   [**SERVER\_INFO\_1502**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1502)
-   [**SERVER\_INFO\_1503**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1503)
-   [**SERVER\_INFO\_1506**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1506)
-   [**SERVER\_INFO\_1509**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1509)
-   [**SERVER\_INFO\_1510**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1510)
-   [**SERVER\_INFO\_1511**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1511)
-   [**SERVER\_INFO\_1512**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1512)
-   [**SERVER\_INFO\_1513**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1513)
-   [**SERVER\_INFO\_1515**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1515)
-   [**SERVER\_INFO\_1516**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1516)
-   [**SERVER\_INFO\_1518**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1518)
-   [**SERVER\_INFO\_1523**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1523)
-   [**SERVER\_INFO\_1528**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1528)
-   [**SERVER\_INFO\_1529**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1529)
-   [**SERVER\_INFO\_1530**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1530)
-   [**SERVER\_INFO\_1533**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1533)
-   [**SERVER\_INFO\_1536**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1536)
-   [**SERVER\_INFO\_1538**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1538)
-   [**SERVER\_INFO\_1539**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1539)
-   [**SERVER\_INFO\_1540**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1540)
-   [**SERVER\_INFO\_1541**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1541)
-   [**SERVER\_INFO\_1542**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1542)
-   [**SERVER\_INFO\_1544**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1544)
-   [**SERVER\_INFO\_1550**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1550)
-   [**SERVER\_INFO\_1552**](/windows/desktop/api/Lmserver/ns-lmserver-server_info_1552)

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management server functions. For more information, see [**IADsComputer**](/windows/desktop/api/iads/nn-iads-iadscomputer).

For more information, see the [Server and Workstation Transport Functions](server-and-workstation-transport-functions.md).

 

 
