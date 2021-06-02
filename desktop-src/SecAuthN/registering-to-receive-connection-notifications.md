---
description: After you have created a DLL to receive connection notifications, you must register it with the system.
ms.assetid: 1a389de1-367d-4b07-a420-4af431d48b7f
title: Registering to Receive Connection Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Registering to Receive Connection Notifications

After you have created a DLL to receive connection notifications, you must register it with the system. You do this by adding a **REG\_EXPAND\_SZ** value under the

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**NetworkProvider**\\**Notifyees**

key. This value specifies the path to the DLL that implements the [Connection Notification API](connection-notification-api.md).

The value can have any name. All values under the **Notifyees** key are treated as paths to DLLs that are notified of connection events. It is recommended that you use a name that identifies your DLL. This lessens the chance of a name conflict with other connection notification applications.

For more information about how to create an application that receives connection notifications, see [Receiving Connection Notifications](receiving-connection-notifications.md).

 

 



