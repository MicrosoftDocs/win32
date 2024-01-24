---
description: The System Event Notification Service enables mobile-aware applications to receive notifications from system events that SENS monitors. When the requested event occurs, SENS notifies the application.
ms.assetid: 19311dec-4611-4104-b6e4-ff8f7c8af0e7
title: Notifications (System Event Notification Service)
ms.topic: article
ms.date: 05/31/2018
---

# Notifications (System Event Notification Service)

The System Event Notification Service enables mobile-aware applications to receive notifications from system events that SENS monitors. When the requested event occurs, SENS notifies the application.

SENS can notify applications about three classes of system events:

-   TCP/IP network events, such as the status of a TCP/IP network connection or the quality of the connection.
-   User logon events.
-   Battery and AC power events.

For example, an application can subscribe to any of the following system events:

-   Establishment of network connectivity
-   Notification when a specified destination can be reached within specified Quality of Connection (QOC) parameters
-   The computer has switched to battery power
-   The percentage of remaining battery power is within a specified parameter
-   Scheduled events using Synchronization Manager occur

**Windows Server 2008 R2 and Windows 7:** The subscriber has a maximum of 3 minutes to respond to a notification on the [**ISensLogon**](/windows/desktop/api/Sensevts/nn-sensevts-isenslogon) and [**ISensLogon2**](/windows/desktop/api/Sensevts/nn-sensevts-isenslogon2) interfaces. After 3 minutes, SENS cancels the call to subscribers and unblocks the notification thread. If a lengthy operation is required to respond to the notification, return from **ISensLogon** or **ISensLogon2** as quickly as possible and open another thread for processing.

 

 



