---
title: Implementing Offline
description: The Offline entry point function should perform cleanup tasks and gracefully shut down the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd6459783-cb94-4fbc-b76d-da811db379ce'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster ,implementing Offline", "Offline Failover Cluster ,implementing"]
---

# Implementing Offline

The [**Offline**](offline.md) entry point function should perform cleanup tasks and gracefully shut down the [resource](resources.md). Keep in mind that the [Cluster service](cluster-service.md) invokes **Offline** during [*failover*](f-gly.md#-wolf-failover-gly) as well as during normal resource shutdown. (For more information, see [Failover](failover.md).) Your implementation of **Offline** should handle both situations while saving state and configuration information and taking any steps necessary to enable the resource to be brought online on another node if necessary.

**To implement Offline**

1.  Required: The [**Offline**](offline.md) entry point function can be called concurrently with the [*Terminate*](terminate.md) entry point function. Any resources that are accessed by both entry points must be properly guarded.

2.  Recommended: For optimal performance, return a value within 300 milliseconds. If you need more time to perform all of the necessary cleanup tasks, have [**Offline**](offline.md) start a worker thread and return **ERROR\_IO\_PENDING** immediately. See [Implementing Pending Operations](implementing-pending-operations.md).

 

 




