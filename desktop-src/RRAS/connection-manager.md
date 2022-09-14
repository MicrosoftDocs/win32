---
title: Connection Manager
description: Customers who intend to develop custom dialers using the Remote Access Service API may want to investigate Microsoft Connection Manager and the Connection Manager Administration Kit.
ms.assetid: c3227aea-ba36-44f6-b69d-2c6aa4be360e
ms.topic: article
ms.date: 05/31/2018
---

# Connection Manager

Customers who intend to develop custom dialers using the Remote Access Service API may want to investigate Microsoft Connection Manager and the Connection Manager Administration Kit. Connection Manager is Microsoft's managed remote access client. It allows an administrator to build a remote access configuration package to be distributed to the administrator's remote users. For more information on Connection Manager and the Connection Manager Administration Kit, see the online help for Microsoft Windows 2000 Server and later operating systems.

You can find the source code for a sample Connection Manager custom action in the complete Platform Software Development Kit (SDK). The Platform SDK can be downloaded at the [Microsoft Web site](https://msdn.microsoft.com/windowsserver/bb980924.aspx). After installation, the path to the sample code is %Install Path%\\Microsoft SDK\\Samples\\netds\\Ras\\ConnectionManager, where %Install Path% designates the base installation directory of the Platform SDK (for example, C:\\Program Files).

Custom actions make it possible for the remote access client to take specific actions at various points in the connection process. The custom action demonstrated in the sample automatically adjusts the proxy server configuration for a connection based on the connection's server address. Customers can use this sample as a starting point for creating their own custom actions.

 

 




