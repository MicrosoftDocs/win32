---
title: Informational Notifications
description: For the connection states known as running states, no action is required of the notification handler unless an error occurs.
ms.assetid: 3f5ea9e0-f75a-4b02-a0dc-86cb5012c242
ms.topic: article
ms.date: 05/31/2018
---

# Informational Notifications

For the [connection states](connection-states.md) known as running states, no action is required of the notification handler unless an error occurs. Running states occur during the parts of the connection operation that RAS handles automatically, such as connecting to the necessary devices, authenticating the user, and waiting for a callback from the remote server. The notification is simply a progress report to the client.

The client can choose to pass these informational notifications on to the user. In some running states, the client may want to display additional information. For example, a notification handler that receives a RASCS\_ConnectDevice notification can call the [**RasGetConnectStatus**](/windows/desktop/api/Ras/nf-ras-rasgetconnectstatusa) function to get the name and type of the device being connected to. Another example is when the client receives a RASCS\_Projected notification. This occurs when the RAS projection phase of the connection operation has been completed. The client can call the [**RasGetProjectionInfo**](/previous-versions/windows/embedded/ms897107(v=msdn.10)) function to get additional information about the projection. The client can use this information to notify the user as to which network protocols can be used by this connection.

You should avoid writing code that depends on the order or occurrence of particular informational states, because this may vary between platforms.

 

 




