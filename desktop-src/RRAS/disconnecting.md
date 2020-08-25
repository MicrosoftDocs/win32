---
title: Disconnecting
description: When a RAS client application starts a connection operation, the RasDial call receives an HRASCONN connection handle to identify the connection.
ms.assetid: a0fddc69-44bb-4bb0-ae57-ebecbe85cbe9
ms.topic: article
ms.date: 05/31/2018
---

# Disconnecting

When a RAS client application starts a connection operation, the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call receives an **HRASCONN** connection handle to identify the connection. If the returned handle is not **NULL**, the client must eventually call the [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa) function to end the connection. If an error occurs during the connection operation, the client must call **RasHangUp** even though the connection was never established.

The application that calls [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa) should not exit immediately because the Remote Access Connection Manager needs time to properly terminate the connection. Instead, the application should wait until the [**RasGetConnectStatus**](/windows/desktop/api/Ras/nf-ras-rasgetconnectstatusa) function returns ERROR\_INVALID\_HANDLE, indicating that the connection has been deleted.

A RAS client application might need to end a connection even though it does not have the handle returned by [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala). For example, the application that called **RasDial** might have exited after the connection was successfully established. In this case, the disconnecting application can use the [**RasEnumConnections**](/windows/desktop/api/Ras/nf-ras-rasenumconnectionsa) function to get all the current connections. For each connection, **RasEnumConnections** returns a [**RASCONN**](/previous-versions/windows/desktop/legacy/aa376725(v=vs.85)) structure that contains the **HRASCONN** connection handle and the phone-book entry name or phone number specified when the connection operation was started. This information can be used to display a list of connections from which the user can select the connection to end.

 

 