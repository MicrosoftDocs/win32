---
description: The System Event Notification Service works with the COM+ Event System.
ms.assetid: c51d1f61-6087-4480-b989-31241829781b
title: SENS Architecture
ms.topic: article
ms.date: 05/31/2018
---

# SENS Architecture

The System Event Notification Service works with the COM+ Event System. SENS is an event publisher for the classes of events that it monitors: network, logon, and power/battery events. The application receiving a notification is called an event subscriber.

When an application subscribes to receive notifications, it can also specify filters associated with the subscribed events. SENS and COM+ Events use the filters to further determine when the application should be notified.

Notifications are asynchronous, so the application receiving the notification does not have to be active when the notification is sent. When an application subscribes to receive notifications, it can specify whether it should be activated when the event occurs or notified later when it is active.

The subscription can be transient and valid only until the application stops running, or it can be persistent and valid until the application is removed from the system.

A COM+ Events data store contains information about the event publisher (SENS), event subscribers, and filters. SENS also predefines an outgoing interface for each event class in a type library.



| Event class    | GUID                          | Interface    |
|----------------|-------------------------------|--------------|
| Network events | SENSGUID\_EVENTCLASS\_NETWORK | ISensNetwork |
| Logon events   | SENSGUID\_EVENTCLASS\_LOGON   | ISensLogon   |
| Power events   | SENSGUID\_EVENTCLASS\_ONNOW   | ISensOnNow   |



 

To receive notifications for any of these events, your application must do two things:

-   Subscribe to the SENS events that interest you. To subscribe to an event, use the **IEventSubscription** and **IEventSystem** interfaces in COM+ Events. You need to supply an identifier for the event classes and the SENS publisher identifier, SENSGUID\_PUBLISHER. Subscriptions are on a per event level so the subscribing application must also specify which events within the class are of interest. Each event corresponds to a method in the interface corresponding to its event class.
-   Create a sink object with an implementation for each interface that you handle. See [**ISensNetwork**](/windows/desktop/api/Sensevts/nn-sensevts-isensnetwork), [**ISensLogon**](/windows/desktop/api/Sensevts/nn-sensevts-isenslogon), and [**ISensOnNow**](/windows/desktop/api/Sensevts/nn-sensevts-isensonnow) for more information about these interfaces and the events supported in each one.

When one of the monitored events occurs, SENS processes each subscription with any associated filters and notifies the subscribers through the COM+ Event system.

 

 



