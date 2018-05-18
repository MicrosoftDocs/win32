---
title: Implementing Close
description: The purpose of Close is to remove a resource instance from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b3f99392-1402-4c8d-b16b-e20bda4173da'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster ,implementing Close", "Close Failover Cluster ,implementing"]
---

# Implementing Close

The purpose of [**Close**](close.md) is to remove a resource instance from the [*cluster*](c-gly.md#-wolf-cluster-gly). The [Cluster service](cluster-service.md) prompts the [Resource Monitor](resource-monitor.md) to invoke the **Close** entry point function to remove a [resource](resources.md) instance from the cluster; for example, in response to [**DeleteClusterResource**](deleteclusterresource.md).

**To implement Close**

1.  Required: Make sure the resource is [*offline*](o-gly.md#-wolf-offline-gly). If it is not offline, call [**Terminate**](terminate.md) to forcibly take the resource offline.
2.  Required: Deallocate all structures related to the resource instance.
3.  Optional: Decrement instance counters if necessary.
4.  Recommended: For optimal performance, return a value within 300 milliseconds.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




