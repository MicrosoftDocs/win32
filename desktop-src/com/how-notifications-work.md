---
title: How Notifications Work
description: How Notifications Work
ms.assetid: faf66654-8233-49ac-a0fa-6cae51df0bea
ms.topic: article
ms.date: 05/31/2018
---

# How Notifications Work

Notifications originate in the object application and flow to the container by way of the object handler. If the object is a linked object, the linked object intercepts the notifications from the object handler and notifies the container directly.

An object application must manage registration requests, keeping track of where to send which notifications and sending those notifications when appropriate. OLE provides two component objects to simplify this task: the OleAdviseHolder for compound document notifications and the DataAdviseHolder for data notifications.

Object applications determine the conditions that prompt the sending of each specific notification and the frequency with which each notification should be sent. When it is appropriate for multiple notifications to be sent, it does not matter which notification is sent first; they can be sent in any order.

The timing of notifications affects the performance and coordination between an object application and its containers. Whereas notifications sent too frequently slow processing, notifications sent too infrequently result in an out-of-sync container. Notification frequency can be compared with the rate at which an application repaints. Therefore, using similar logic for the timing of notifications (as is used for repainting) is wise.

## Related topics

<dl> <dt>

[**CreateDataAdviseHolder**](/windows/win32/api/ole2/nf-ole2-createdataadviseholder)
</dt> <dt>

[**CreateOleAdviseHolder**](/windows/desktop/api/Ole2/nf-ole2-createoleadviseholder)
</dt> <dt>

[Notifications](notifications.md)
</dt> </dl>

 

 