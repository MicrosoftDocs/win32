---
description: One of the most common ways to receive an event is through a running application, such as a management application that collects and displays events to a user.
ms.assetid: 380ac556-ba0a-4fae-8b76-0645d99e8583
ms.tgt_platform: multiple
title: Receiving Events for the Duration of Your Application
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Events for the Duration of Your Application

One of the most common ways to receive an event is through a running application, such as a management application that collects and displays events to a user. Such applications are called "temporary" because a temporary consumer does not receive event notifications when shut down.

A temporary consumer calls [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) in script or [**IWbemServices.ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) in C++ to subscribe to events in a namespace. The identity associated with this subscription is the caller.

A temporary event consumer can receive notifications either asynchronously or semisynchronously in both scripts and C++.

> [!Note]  
> For security reasons, it is important to note that asynchronous event notifications are not recommended. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md). Event consumers have special security concerns. For more information, see [Securing WMI Events](securing-wmi-events.md).

 

For more information about receiving asynchronous and semisynchronous event notifications, see [Receiving Asynchronous Event Notifications](receiving-asynchronous-event-notifications.md) and [Receiving Semisynchronous Event Notifications](receiving-synchronous-and-semisynchronous-event-notifications.md).

 

 



