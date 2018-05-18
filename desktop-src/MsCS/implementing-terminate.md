---
title: Implementing Terminate
description: The Terminate entry point function is used to immediately end a process that does not shut down gracefully when the Offline function is called.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'df6edc61-d325-46a5-b486-079a52dfaf77'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster ,implementing Terminate", "Terminate Failover Cluster ,implementing"]
---

# Implementing Terminate

The [**Terminate**](terminate.md) entry point function is used to immediately end a process that does not shut down gracefully when the [**Offline**](offline.md) function is called.

**To implement Terminate**

1.  Required: The [**Terminate**](terminate.md) entry point function can be called concurrently with the [**IsAlive**](isalive.md), [**LooksAlive**](looksalive.md), [**Offline**](offline.md), [**Online**](online.md), [**ResourceControl**](resourcecontrol.md), and [**ResourceTypeControl**](resourcetypecontrol.md) entry point functions. Any resources that are accessed by these entry points must be properly guarded.

2.  Recommended: For optimal performance, return within 300 milliseconds. However, the [Cluster service](cluster-service.md) handles the situation properly if this time limit is exceeded.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




