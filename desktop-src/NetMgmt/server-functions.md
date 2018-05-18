---
title: Server Functions
description: The network management server functions perform administrative tasks on a local or remote server. The server functions are listed following.
ms.assetid: '43e1285b-8c86-4af4-9834-fcd5ee8aceb8'
---

# Server Functions

The network management server functions perform administrative tasks on a local or remote server. The server functions are listed following.



| Function                                       | Description                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------|
| [**NetServerDiskEnum**](netserverdiskenum.md) | Returns a list of local disk drives on a server.                                   |
| [**NetServerEnum**](netserverenum.md)         | Lists all visible servers of a particular type (or types) in the specified domain. |
| [**NetServerGetInfo**](netservergetinfo.md)   | Returns configuration information about a specified server.                        |
| [**NetServerSetInfo**](netserversetinfo.md)   | Sets the operating parameters for a server.                                        |



 

Only a user or application with admin group membership on a local or remote server can perform administrative tasks on that server to control the server's operation, user access, and resource sharing. The low-level parameters that affect a server's operation can be examined and modified by calling the [**NetServerGetInfo**](netservergetinfo.md) and [**NetServerSetInfo**](netserversetinfo.md) functions. These parameters are defined in the server's LANMAN.INI file.

Most network management server functions execute only on a remote server. The [**NetServerEnum**](netserverenum.md) function executes on either a local workstation or a remote server. If you attempt to execute other server functions on a local workstation, the functions return the error NERR\_RemoteOnly.

Server-specific information is available at the following levels:

-   [**SERVER\_INFO\_100**](server-info-100-str.md)
-   [**SERVER\_INFO\_101**](server-info-101-str.md)
-   [**SERVER\_INFO\_102**](server-info-102-str.md)
-   [**SERVER\_INFO\_402**](server-info-402-str.md)
-   [**SERVER\_INFO\_403**](server-info-403-str.md)
-   [**SERVER\_INFO\_1501**](server-info-1501-str.md)
-   [**SERVER\_INFO\_1502**](server-info-1502-str.md)
-   [**SERVER\_INFO\_1503**](server-info-1503-str.md)
-   [**SERVER\_INFO\_1506**](server-info-1506-str.md)
-   [**SERVER\_INFO\_1509**](server-info-1509-str.md)
-   [**SERVER\_INFO\_1510**](server-info-1510-str.md)
-   [**SERVER\_INFO\_1511**](server-info-1511-str.md)
-   [**SERVER\_INFO\_1512**](server-info-1512-str.md)
-   [**SERVER\_INFO\_1513**](server-info-1513-str.md)
-   [**SERVER\_INFO\_1515**](server-info-1515-str.md)
-   [**SERVER\_INFO\_1516**](server-info-1516-str.md)
-   [**SERVER\_INFO\_1518**](server-info-1518-str.md)
-   [**SERVER\_INFO\_1523**](server-info-1523-str.md)
-   [**SERVER\_INFO\_1528**](server-info-1528-str.md)
-   [**SERVER\_INFO\_1529**](server-info-1529-str.md)
-   [**SERVER\_INFO\_1530**](server-info-1530-str.md)
-   [**SERVER\_INFO\_1533**](server-info-1533-str.md)
-   [**SERVER\_INFO\_1536**](server-info-1536-str.md)
-   [**SERVER\_INFO\_1538**](server-info-1538-str.md)
-   [**SERVER\_INFO\_1539**](server-info-1539-str.md)
-   [**SERVER\_INFO\_1540**](server-info-1540-str.md)
-   [**SERVER\_INFO\_1541**](server-info-1541-str.md)
-   [**SERVER\_INFO\_1542**](server-info-1542-str.md)
-   [**SERVER\_INFO\_1544**](server-info-1544-str.md)
-   [**SERVER\_INFO\_1550**](server-info-1550-str.md)
-   [**SERVER\_INFO\_1552**](server-info-1552-str.md)

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management server functions. For more information, see [**IADsComputer**](https://msdn.microsoft.com/library/aa705980).

For more information, see the [Server and Workstation Transport Functions](server-and-workstation-transport-functions.md).

 

 




