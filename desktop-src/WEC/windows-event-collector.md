---
title: Windows Event Collector
description: You can subscribe to receive and store events on a local computer (event collector) that are forwarded from a remote computer (event source).
ms.assetid: '7725e06d-4df1-4b3e-9f2f-2b8bdd805cb6'
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Windows Event Collector

You can subscribe to receive and store events on a local computer (event collector) that are forwarded from a remote computer (event source). The [Windows Event Collector functions](windows-event-collector-functions.md) support subscribing to events by using the WS-Management protocol. For more information about WS-Management, see [About Windows Remote Management](/windows/desktop/WinRM/about-windows-remote-management).

## Event Forwarding and Event Collection Architecture

Event collection allows administrators to get events from remote computers and store them in a local event log on the collector computer. The destination log path for the events is a property of the subscription. All data in the forwarded event is saved in the collector computer event log (none of the information is lost). Additional information related to the event forwarding is also added to the event. For more information about how to enable a computer to receive collected events or forward events, see [Configure Computers to Forward and Collect Events](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc748890(v=ws.11)).

## Subscriptions

The following list describes the types of event subscriptions:

-   Source-initiated subscriptions: allows you to define an event subscription on an event collector computer without defining the event source computers. Multiple remote event source computers can then be set up (using a group policy setting) to forward events to the event collector computer. For more information, see [Setting up a Source Initiated Subscription](setting-up-a-source-initiated-subscription.md). This subscription type is useful when you do not know or you do not want to specify all the event sources computers that will forward events.
-   Collector-initiated subscriptions: allows you to create an event subscription if you know all the event source computers that will forward events. You specify all the event sources at the time the subscription is created. For more information, see [Creating a Collector Initiated Subscription](creating-an-event-collector-subscription.md).

## Windows Event Collector Functions

For more information and code examples that use the Event Collector functions, see [Using Windows Event Collector](using-windows-event-collector.md).

For more information about the functions used to collect and forward events, see [Windows Event Collector functions](windows-event-collector-functions.md).

 

 