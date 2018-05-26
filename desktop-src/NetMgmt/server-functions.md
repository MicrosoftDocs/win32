---
title: Server Functions
description: The network management server functions perform administrative tasks on a local or remote server. The server functions are listed following.
ms.assetid: 43e1285b-8c86-4af4-9834-fcd5ee8aceb8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Server Functions

The network management server functions perform administrative tasks on a local or remote server. The server functions are listed following.



| Function                                       | Description                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------|
| [**NetServerDiskEnum**](/windows/win32/Lmserver/nf-lmserver-netserverdiskenum?branch=master) | Returns a list of local disk drives on a server.                                   |
| [**NetServerEnum**](/windows/win32/Lmserver/nf-lmserver-netserverenum?branch=master)         | Lists all visible servers of a particular type (or types) in the specified domain. |
| [**NetServerGetInfo**](/windows/win32/Lmserver/nf-lmserver-netservergetinfo?branch=master)   | Returns configuration information about a specified server.                        |
| [**NetServerSetInfo**](/windows/win32/Lmserver/nf-lmserver-netserversetinfo?branch=master)   | Sets the operating parameters for a server.                                        |



 

Only a user or application with admin group membership on a local or remote server can perform administrative tasks on that server to control the server's operation, user access, and resource sharing. The low-level parameters that affect a server's operation can be examined and modified by calling the [**NetServerGetInfo**](/windows/win32/Lmserver/nf-lmserver-netservergetinfo?branch=master) and [**NetServerSetInfo**](/windows/win32/Lmserver/nf-lmserver-netserversetinfo?branch=master) functions. These parameters are defined in the server's LANMAN.INI file.

Most network management server functions execute only on a remote server. The [**NetServerEnum**](/windows/win32/Lmserver/nf-lmserver-netserverenum?branch=master) function executes on either a local workstation or a remote server. If you attempt to execute other server functions on a local workstation, the functions return the error NERR\_RemoteOnly.

Server-specific information is available at the following levels:

-   [**SERVER\_INFO\_100**](/windows/win32/Lmserver/ns-lmserver-_server_info_100?branch=master)
-   [**SERVER\_INFO\_101**](/windows/win32/Lmserver/ns-lmserver-_server_info_101?branch=master)
-   [**SERVER\_INFO\_102**](/windows/win32/Lmserver/ns-lmserver-_server_info_102?branch=master)
-   [**SERVER\_INFO\_402**](/windows/win32/Lmserver/ns-lmserver-_server_info_402?branch=master)
-   [**SERVER\_INFO\_403**](/windows/win32/Lmserver/ns-lmserver-_server_info_403?branch=master)
-   [**SERVER\_INFO\_1501**](/windows/win32/Lmserver/ns-lmserver-_server_info_1501?branch=master)
-   [**SERVER\_INFO\_1502**](/windows/win32/Lmserver/ns-lmserver-_server_info_1502?branch=master)
-   [**SERVER\_INFO\_1503**](/windows/win32/Lmserver/ns-lmserver-_server_info_1503?branch=master)
-   [**SERVER\_INFO\_1506**](/windows/win32/Lmserver/ns-lmserver-_server_info_1506?branch=master)
-   [**SERVER\_INFO\_1509**](/windows/win32/Lmserver/ns-lmserver-_server_info_1509?branch=master)
-   [**SERVER\_INFO\_1510**](/windows/win32/Lmserver/ns-lmserver-_server_info_1510?branch=master)
-   [**SERVER\_INFO\_1511**](/windows/win32/Lmserver/ns-lmserver-_server_info_1511?branch=master)
-   [**SERVER\_INFO\_1512**](/windows/win32/Lmserver/ns-lmserver-_server_info_1512?branch=master)
-   [**SERVER\_INFO\_1513**](/windows/win32/Lmserver/ns-lmserver-_server_info_1513?branch=master)
-   [**SERVER\_INFO\_1515**](/windows/win32/Lmserver/ns-lmserver-_server_info_1515?branch=master)
-   [**SERVER\_INFO\_1516**](/windows/win32/Lmserver/ns-lmserver-_server_info_1516?branch=master)
-   [**SERVER\_INFO\_1518**](/windows/win32/Lmserver/ns-lmserver-_server_info_1518?branch=master)
-   [**SERVER\_INFO\_1523**](/windows/win32/Lmserver/ns-lmserver-_server_info_1523?branch=master)
-   [**SERVER\_INFO\_1528**](/windows/win32/Lmserver/ns-lmserver-_server_info_1528?branch=master)
-   [**SERVER\_INFO\_1529**](/windows/win32/Lmserver/ns-lmserver-_server_info_1529?branch=master)
-   [**SERVER\_INFO\_1530**](/windows/win32/Lmserver/ns-lmserver-_server_info_1530?branch=master)
-   [**SERVER\_INFO\_1533**](/windows/win32/Lmserver/ns-lmserver-_server_info_1533?branch=master)
-   [**SERVER\_INFO\_1536**](/windows/win32/Lmserver/ns-lmserver-_server_info_1536?branch=master)
-   [**SERVER\_INFO\_1538**](/windows/win32/Lmserver/ns-lmserver-_server_info_1538?branch=master)
-   [**SERVER\_INFO\_1539**](/windows/win32/Lmserver/ns-lmserver-_server_info_1539?branch=master)
-   [**SERVER\_INFO\_1540**](/windows/win32/Lmserver/ns-lmserver-_server_info_1540?branch=master)
-   [**SERVER\_INFO\_1541**](/windows/win32/Lmserver/ns-lmserver-_server_info_1541?branch=master)
-   [**SERVER\_INFO\_1542**](/windows/win32/Lmserver/ns-lmserver-_server_info_1542?branch=master)
-   [**SERVER\_INFO\_1544**](/windows/win32/Lmserver/ns-lmserver-_server_info_1544?branch=master)
-   [**SERVER\_INFO\_1550**](/windows/win32/Lmserver/ns-lmserver-_server_info_1550?branch=master)
-   [**SERVER\_INFO\_1552**](/windows/win32/Lmserver/ns-lmserver-_server_info_1552?branch=master)

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management server functions. For more information, see [**IADsComputer**](https://msdn.microsoft.com/library/aa705980).

For more information, see the [Server and Workstation Transport Functions](server-and-workstation-transport-functions.md).

 

 




