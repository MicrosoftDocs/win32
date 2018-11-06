---
title: Implementing a Hosted Device
description: The device host with UPnP technology implements the core UPnP protocols discovery, description, control, and eventing.
ms.assetid: ab113d76-5fc9-4be2-a814-8772dd1e9600
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Hosted Device

The device host with UPnP technology implements the core UPnP protocols: discovery, description, control, and eventing. The developer who implements a hosted device only needs to provide:

-   A description of the device and its services.
-   An implementation of the device's functionality.

For example, the developer of a clock device must provide UPnP-based device and service descriptions for it, and an implementation of the clock functions (such as keeping time, setting time, and responding to queries for the current time). The device host:

-   Announces the device according to the UPnP discovery protocol.
-   Responds to queries for the device's description.
-   Routes control requests to the part of the device's code that implements the clock functions.
-   Maintains event subscriptions to services.
-   Sends event notifications to subscribers when the service's state changes.

 

 




