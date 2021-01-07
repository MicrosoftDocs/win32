---
description: The Multiple Provider Router (MPR) calls the connection notification functions when it connects or disconnects a network resource. To receive such notifications, you can implement these functions in a DLL.
ms.assetid: 62559eab-dd2f-43fa-9b09-5e4d82efc879
title: Connection Notification API
ms.topic: article
ms.date: 05/31/2018
---

# Connection Notification API

The [*Multiple Provider Router*](/windows/desktop/SecGloss/m-gly) (MPR) calls the connection notification functions when it connects or disconnects a network resource. To receive such notifications, you can implement these functions in a DLL.

The MPR calls the [**AddConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-addconnectnotify) function before and after attempting each add-connection operation ([**WNetAddConnection**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnectiona), [**WNetAddConnection2**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnection2a), or [**WNetAddConnection3**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnection3a)). This function is not called when the MPR is automatically restoring network connections.

The MPR calls the [**CancelConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-cancelconnectnotify) function before and after attempting each cancel-connection operation ([**WNetCancelConnection**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetcancelconnectiona) or [**WNetCancelConnection2**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetcancelconnection2a)).

For more information about WNet functions, see [Windows Networking](/windows/desktop/WNet/windows-networking-wnet-).

For more information about how to create and register an application that receives network connection notifications, see [Receiving Connection Notifications](receiving-connection-notifications.md) and [Registering to Receive Connection Notifications](registering-to-receive-connection-notifications.md).

 

 
