---
title: Notification Handlers
description: An asynchronous RasDial call must specify a notification handler.
ms.assetid: 6d23d6ac-08ad-4fe2-a4af-021e4d384079
ms.topic: article
ms.date: 05/31/2018
---

# Notification Handlers

An asynchronous [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call must specify a notification handler. During an asynchronous connection operation, the Remote Access Connection Manager uses the notification handler to inform the RAS client whenever the [connection state](connection-states.md) changes or an error occurs.

The actions performed by a notification handler can be divided into the following categories:

-   [Handling errors](handling-ras-errors.md).
-   Providing feedback to the user as the connection operation proceeds through the various connection states. See [Informational Notifications](informational-notifications.md).
-   Handling [paused states](paused-states.md).
-   Signaling the RAS client application when the connection operation has been completed. See [Completion Notifications](completion-notifications.md).

There are three types of notification handlers, each of which receives the same basic information: the current connection state and an error code that is nonzero only if an error has occurred.



| Value                                | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RasDialFunc**](/windows/desktop/api/Ras/nc-ras-rasdialfunc)   | A callback function prototype that receives only the current connection state and error code information.                                                                                                                                                                                                                                                                                                                                                                                    |
| [**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1) | A callback function prototype that receives the **HRASCONN** connection handle and extended error information in addition to the basic information. The connection handle parameter makes [**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1) useful for client applications that support multiple simultaneous connection operations. This allows the client to specify the same callback function for all operations, and enables the callback function to determine which connection is changing states. |
| [**RasDialFunc2**](/windows/desktop/api/Ras/nc-ras-rasdialfunc2) | A callback function similar to [**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1). However, [**RasDialFunc2**](/windows/desktop/api/Ras/nc-ras-rasdialfunc2) is enhanced to support multilink connections.                                                                                                                                                                                                                                                                                                                             |
| Window handle                        | A window handle to which RAS sends [**WM\_RASDIALEVENT**](wm-rasdialevent.md) messages containing the current connection state and error code information. Use this method if your source code must be compatible with 16-bit Windows, because 16-bit Windows does not support either of the callback functions.                                                                                                                                                                            |



 

The Remote Access Connection Manager suspends the connection operation until the notification handler returns. For this reason, the handler should return as soon as possible unless an error has occurred.

The [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function should not be called from within a notification handler. The other remote access functions ( [**RasGetConnectStatus**](/windows/desktop/api/Ras/nf-ras-rasgetconnectstatusa), [**RasEnumEntries**](/windows/desktop/api/Ras/nf-ras-rasenumentriesa), [**RasEnumConnections**](/windows/desktop/api/Ras/nf-ras-rasenumconnectionsa), [**RasGetErrorString**](/windows/desktop/api/Ras/nf-ras-rasgeterrorstringa), and [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa)) can be called from within a handler.

 

 




