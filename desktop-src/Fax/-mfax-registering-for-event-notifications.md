---
Description: A fax client that uses the extended Component Object Model (COM) client model can register for server events.
ms.assetid: a02d2bc4-bbee-4eb5-8e19-6032957155ce
title: Registering for Event Notifications
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering for Event Notifications

A fax client that uses the extended Component Object Model (COM) client model can register for server events. Server events include notification of changes to the fax server configuration, incoming and outgoing job queues and archives, and activity. You can register for notifications sent by the fax server for various server events. A fax client can filter for events for which it requires notification. Notifications are implemented using a connection point interface. For more information about connection point interfaces, see [Connection Points](http://msdn.microsoft.com/library/en-us/vccore/html/_core_Connection_Points.asp).

**Pre-Windows Vista**

To receive the notifications, use the [**IFaxServer::ListenToServerEvents**](-mfax-faxserver-cpp-mfax-faxserver-listentoserverevents-cpp.md) method. This method receives values from the [**FAX\_SERVER\_EVENTS\_TYPE\_ENUM**](-mfax-fax-server-events-type-enum.md) enumeration. Use the values to specify the events for which you want to register.

After you register for events, implement the corresponding event handler functions of [**IFaxServerNotify**](-mfax-ifaxservernotify.md). When the event occurs, the event handler will be called, and your code in the event handler function will run.

If you do not want the server to receive notifications, call [**IFaxServer::ListenToServerEvents**](-mfax-faxserver-cpp-mfax-faxserver-listentoserverevents-cpp.md) using the value [****fsetNONE****](-mfax-fax-server-events-type-enum.md). In this case, the server will not call your event handler function.

For example, if you want to register to be notified when a new job is added to either the incoming or outgoing queue, you would first call `FaxServer.ListenToServerEvents(fsetIN_QUEUE | fsetOUT_QUEUE)`. You would then implement the [**FaxServerNotify.OnIncomingJobAdded**](-mfax-ifaxservernotify-onincomingjobadded.md) and [**FaxServerNotify.OnOutgoingJobAdded**](-mfax-ifaxservernotify-onoutgoingjobadded.md) methods. When an incoming or outgoing job is added to the queue, your code will run so that you can handle the event.

For an example Microsoft Visual Basic program that registers for event notifications, see [Registering for Fax Events](-mfax-registering-for-fax-events.md). For more information about registering for events in Visual Basic, see [Handling an Object's Events](http://msdn.microsoft.com/library/en-us/vbcn7/html/vbconHandlingObjectsEvents.asp).

**Windows Vista**

In Windows Vista, fax account notifications can be received using [**IFaxAccount::ListenToAccountEvents**](-mfax-faxaccount-cpp-mfax-faxaccount-listentoaccountevents-cpp.md) method. This method receives values from the [**FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM**](-mfax-fax-account-events-type-enum.md) enumeration. Use the values to specify the events for which you want to register.

After you register for events, implement the corresponding event handler functions of [**IFaxAccountNotify**](-mfax-ifaxaccountnotify.md). When the event occurs, the event handler will be called, and your code in the event handler function will run.

If you do not want to receive the account notifications, call [**IFaxAccount::ListenToAccountEvents**](-mfax-faxaccount-cpp-mfax-faxaccount-listentoaccountevents-cpp.md) using the value [****faetNONE****](-mfax-fax-account-events-type-enum.md). In this case, your event handler function will not be called.

 

 



