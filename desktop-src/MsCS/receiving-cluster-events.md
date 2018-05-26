---
title: Receiving Cluster Events
description: An application or resource DLL can monitor events occurring within the cluster by creating a notification port.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6d69cdd8-b29a-40c5-94c6-908b9bea22ef
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- events Failover Cluster
- events Failover Cluster ,receiving
- events Failover Cluster
- events,(See also events Failover Cluster )
- notification ports Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Receiving Cluster Events

An application or [resource DLL](resource-dlls.md) can monitor events occurring within the [*cluster*](c-gly.md#-wolf-cluster-gly) by creating a notification port. A notification port stores information about events as a queue of notifications (messages). Once a notification port has been created, an application typically spawns a thread to monitor the port, periodically retrieving event data and taking appropriate action in response to the events.

An application can create multiple notification ports, but this is usually unnecessary. One notification port per application per cluster is sufficient in most cases to monitor any events of interest, and it requires only one thread.

Note that the [Cluster Automation Server](https://msdn.microsoft.com/library/aa372940) does not support event monitoring at this time.

For information on how to use notification ports, see the following sections:

-   [Creating a Notification Port](creating-a-notification-port.md)
-   [Adding Events to a Notification Port](adding-events-to-a-notification-port.md)
-   [Retrieving Events from a Notification Port](retrieving-events-from-a-notification-port.md)
-   [Closing a Notification Port](closing-a-notification-port.md)
-   [Notification Port Example](notification-port-example.md)

 

 




