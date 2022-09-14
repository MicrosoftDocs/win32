---
title: Retrieving Changes
description: Once a client has registered for notification of certain changes and one or more of these changes occurs, the client receives a notification from the routing table manager.
ms.assetid: 5ddebf2d-e3cb-451c-b082-708d2c7d0f79
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Changes

Once a client has registered for notification of certain changes and one or more of these changes occurs, the client receives a notification from the routing table manager. The routing table manager uses the [**RTM\_EVENT\_CALLBACK**](/windows/win32/api/rtmv2/nc-rtmv2-_event_callback) callback that was supplied in a previous call to [**RtmRegisterEntity**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmregisterentity). The routing table manager indicates that a RTM\_CHANGE\_NOTIFICATION event has occurred.

For sample code that shows how to use these functions, see [Use the Event Notification Callback](use-the-event-notification-callback.md).

 

 




