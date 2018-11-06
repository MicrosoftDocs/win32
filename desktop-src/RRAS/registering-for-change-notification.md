---
title: Registering for Change Notification
description: A client can register to receive notification of changes to routing information that is stored in the routing table manager. This request can only be made after a client has registered with the routing table manager.
ms.assetid: 90dc98eb-0d0b-4450-848b-c7cedab75a52
ms.topic: article
ms.date: 05/31/2018
---

# Registering for Change Notification

A client can register to receive notification of changes to routing information that is stored in the routing table manager. This request can only be made after a client has registered with the routing table manager.

To register for change notification, a client must call [**RtmRegisterForChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmregisterforchangenotification), specifying the types of changes for which the client must receive notification. If the client must be notified of change to specific destinations, the client calls [**RtmMarkDestForChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmmarkdestforchangenotification) once for each destination.

The client can stop receiving change notifications by calling [**RtmDeregisterFromChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmderegisterfromchangenotification).

For sample code that shows how to use these functions, see [Register For Change Notification](register-for-change-notification.md).

 

 




