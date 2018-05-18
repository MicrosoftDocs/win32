---
title: Implementing IsAlive
description: Once the resource is online, the Resource Monitor polls the resource periodically to determine its status. The Resource Monitor uses the LooksAlive and IsAlive entry point functions to accomplish this.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f552b41e-d587-4028-9b6e-394c071d0994'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster ,implementing IsAlive", "IsAlive Failover Cluster ,implementing"]
---

# Implementing IsAlive

Once the [resource](resources.md) is [*online*](o-gly.md#-wolf-online-gly), the [Resource Monitor](resource-monitor.md) polls the resource periodically to determine its status. The Resource Monitor uses the [**LooksAlive**](looksalive.md) and [**IsAlive**](isalive.md) entry point functions to accomplish this.

The [**IsAlive**](isalive.md) entry point function is used for more thorough resource status evaluation and is regularly polled by the Resource Monitor at a rate governed by the [**IsAlivePollInterval**](resources-isalivepollinterval.md) property. Unlike [**LooksAlive**](looksalive.md) polling, **IsAlive** polling cannot be turned off.

**To implement IsAlive**

1.  Required: Perform a complete check of the resource to see if it is functioning properly. The set of procedures you need to use depends on your resource. For example, a database resource should check to see that the database can write to the disk, perform queries and updates to the disk, and so forth.

2.  Required: If the resource has definitely failed, return **FALSE**. The Resource Monitor immediately sets the status of the resource to **ClusterResourceFailed**, an enumerator from the [**CLUSTER\_RESOURCE\_STATE**](cluster-resource-state.md) enumeration, and calls the [**Terminate**](terminate.md) entry point function.

3.  Required: The [**IsAlive**](isalive.md) entry point function can be called concurrently with the [*Terminate*](terminate.md) entry point function. Any resources that are accessed by both entry points must be properly guarded.

4.  Recommended: Take no more than 300 milliseconds to complete; ideally, it should finish in less than 50 milliseconds. However, if your implementation must take longer than 300 milliseconds, perform the following steps:

    1.  Have a separate thread dedicated to perform the polling operation.
    2.  Return the result of the last poll performed by the separate thread.

When using separate threads to check the health of resources, take steps to ensure synchronization. For example, you might maintain a monitor thread that is independent of the [**IsAlive**](isalive.md) thread. The two threads could share a common data block, synchronized through a critical section, that contains the last reported status. If the monitor thread detects a failure, it tries to correct it. If that fails, it updates the status in the block. The next time **IsAlive** runs, it sees an error status and takes appropriate action.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

## Related topics

<dl> <dt>

[Detecting Resource Failure](detecting-resource-failure.md)
</dt> </dl>

 

 




