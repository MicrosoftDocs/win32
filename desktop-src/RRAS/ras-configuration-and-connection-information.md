---
title: RAS Configuration and Connection Information
description: Applications running on Windows NT 4.0 and later versions, and Windows 95, can use the RasEnumConnections function to get information about the existing connections on the local computer.
ms.assetid: b738ed87-1ff5-4366-9e83-08ac08ec261c
keywords:
- Configuration and Connection, RAS
ms.topic: article
ms.date: 05/31/2018
---

# RAS Configuration and Connection Information

Applications running on Windows NT 4.0 and later versions, and Windows 95, can use the [**RasEnumConnections**](/windows/desktop/api/Ras/nf-ras-rasenumconnectionsa) function to get information about the existing connections on the local computer. The information for each connection includes a connection handle and the name of the phone-book entry used to establish the connection. You can use the connection handle in a call to the [**RasGetConnectStatus**](/windows/desktop/api/Ras/nf-ras-rasgetconnectstatusa) function get the current status of the connection.

Windows NT Server 4.0 and later versions provide two new functions for retrieving RAS information. Windows 95does not support these functions.

The [**RasEnumDevices**](/windows/desktop/api/Ras/nf-ras-rasenumdevicesa) function returns the name and type of the RAS-capable devices that are configured on the local computer.

The [**RasConnectionNotification**](/windows/desktop/api/Ras/nf-ras-rasconnectionnotificationa) function specifies an event object that the system signals when a RAS connection is created or terminated.

 

 




