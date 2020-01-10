---
Description: Event notification is the primary means by which an application gets information from TAPI and the service providers.
ms.assetid: 02160f10-dc3f-484c-9cd3-bcfb07ded822
title: Event Notification
ms.topic: article
ms.date: 05/31/2018
---

# Event Notification

Event notification is the primary means by which an application gets information from TAPI and the service providers. This information may be the status of an asynchronous operation instigated by the application or may concern a process that started outside of the application, such as notifications of new incoming calls.

**TAPI 2.x:** Applications handle notification in one of three ways: Hidden Window, Event Handle, or Completion Port. For additional information on these notification mechanisms, please see the Remarks section for [**lineInitializeEx**](https://msdn.microsoft.com/library/ms735983(v=VS.85).aspx). An application specifies the mechanism by setting the **dwOptions** member of the [**LINEINITIALIZEEXPARAMS**](https://msdn.microsoft.com/library/ms735985(v=VS.85).aspx) structure prior to calling [**lineInitializeEx**](https://msdn.microsoft.com/library/ms735983(v=VS.85).aspx).

The [**lineSetStatusMessages**](https://msdn.microsoft.com/library/ms736108(v=VS.85).aspx) function enables an application to specify which notification messages to receive for events related to status changes for the specified line or any of its addresses.

**TAPI 3.x:** Applications handle general notification using COM standard [connectable objects](https://msdn.microsoft.com/library/ms694379(v=VS.85).aspx). [**ITTAPIEventNotification**](/windows/desktop/api/Tapi3if/nn-tapi3if-ittapieventnotification) is the outgoing interface that must be registered with TAPI's container object, and [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event) is the method TAPI calls to determine the application's response. The [**ITTAPI::put\_EventFilter**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter) method tells TAPI which events are of interest to the application. If an event filter is not entered, the application will not receive notification of any events. The [**ITTAPI::RegisterCallNotifications**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-registercallnotifications) method tells TAPI the media types and addresses for which the application will handle incoming sessions. For additional information on TAPI 3 event handling, see the [Events](events.md) overview or the [Register Events](register-events.md) code example.

Telephony service providers implement [**TSPI\_lineSetDefaultMediaDetection**](https://msdn.microsoft.com/library/ms725601(v=VS.85).aspx) and [**TSPI\_lineSetStatusMessages**](https://msdn.microsoft.com/library/ms725606(v=VS.85).aspx). TAPI calls these functions to indicate the set of all line, address, and media type events requested by applications.

 

 



