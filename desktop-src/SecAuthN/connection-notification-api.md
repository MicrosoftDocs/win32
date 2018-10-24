---
Description: The Multiple Provider Router (MPR) calls the connection notification functions when it connects or disconnects a network resource. To receive such notifications, you can implement these functions in a DLL.
ms.assetid: 62559eab-dd2f-43fa-9b09-5e4d82efc879
title: Connection Notification API
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Connection Notification API

The [*Multiple Provider Router*](https://msdn.microsoft.com/library/windows/desktop/ms721594#-security-multiple-provider-router-gly) (MPR) calls the connection notification functions when it connects or disconnects a network resource. To receive such notifications, you can implement these functions in a DLL.

The MPR calls the [**AddConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-addconnectnotify) function before and after attempting each add-connection operation ([**WNetAddConnection**](https://msdn.microsoft.com/library/windows/desktop/aa385410), [**WNetAddConnection2**](https://msdn.microsoft.com/library/windows/desktop/aa385413), or [**WNetAddConnection3**](https://msdn.microsoft.com/library/windows/desktop/aa385418)). This function is not called when the MPR is automatically restoring network connections.

The MPR calls the [**CancelConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-cancelconnectnotify) function before and after attempting each cancel-connection operation ([**WNetCancelConnection**](https://msdn.microsoft.com/library/windows/desktop/aa385423) or [**WNetCancelConnection2**](https://msdn.microsoft.com/library/windows/desktop/aa385427)).

For more information about WNet functions, see [Windows Networking](https://msdn.microsoft.com/library/windows/desktop/aa385406).

For more information about how to create and register an application that receives network connection notifications, see [Receiving Connection Notifications](receiving-connection-notifications.md) and [Registering to Receive Connection Notifications](registering-to-receive-connection-notifications.md).

 

 



