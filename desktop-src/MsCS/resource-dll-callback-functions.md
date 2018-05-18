---
title: Resource DLL Callback Functions
description: The resource DLL callback functions allow a resource DLL to report status and event information to a Resource Monitor, which then provides the information to the Cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6c7de7e6-a0f5-4308-8cf3-21968bd339a4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource DLL functions Failover Cluster ,callback functions"]
---

# Resource DLL Callback Functions

The resource DLL callback functions allow a [resource DLL](resource-dlls.md) to report status and event information to a [Resource Monitor](resource-monitor.md), which then provides the information to the [Cluster service](cluster-service.md). These callback functions are implemented by a Resource Monitor and invoked by a resource DLL.

For information about create resource DLLs, see [Creating Resource Types](creating-resource-types.md).

## In this section

<dl> <dt>

[*ChangeResourceProcessForDumps*](changeresourceprocessfordumps.md)
</dt> <dd>

The **PCHANGE\_RESOURCE\_PROCESS\_FOR\_DUMPS** type defines a pointer to this function.

</dd> <dt>

[*ChangeResTypeProcessForDumps*](changerestypeprocessfordumps.md)
</dt> <dd>

The **PCHANGE\_RES\_TYPE\_PROCESS\_FOR\_DUMPS** type defines a pointer to this function.

</dd> <dt>

[*EndControlCall*](endcontrolcall.md)
</dt> <dd>

Called when a resource control code operation completes. The **PEND\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*EndTypeControlCall*](endtypecontrolcall.md)
</dt> <dd>

Called when a resource type control code operation completes. The **PEND\_TYPE\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*ExtendControlCall*](extendcontrolcall.md)
</dt> <dd>

Extends the timeout for a call to a resource control code. The **PEXTEND\_RES\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*ExtendResTypeControlCall*](extendtypecontrolcall.md)
</dt> <dd>

Extends the timeout for a call to a resource type control code. The **PEXTEND\_RES\_TYPE\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*LogEvent*](logevent.md)
</dt> <dd>

Records an event in the cluster log.

</dd> <dt>

[*QuorumResourceLost*](quorumresourcelost.md)
</dt> <dd>

Called when control of the [quorum resource](quorum-resource.md) has been lost.

</dd> <dt>

[*RaiseResTypeNotification*](raiserestypenotification.md)
</dt> <dd>

TBD. The **PRAISE\_RES\_TYPE\_NOTIFICATION** type is a pointer to this function.

</dd> <dt>

[*ResourceCallback*](lpresource-callback.md)
</dt> <dd>

TBD

</dd> <dt>

[*ResourceCallbackEx*](lpresource-callback-ex.md)
</dt> <dd>

TBD

</dd> <dt>

[*SetInternalState*](setinternalstate.md)
</dt> <dd>

Sets the internal state of a resource

</dd> <dt>

[*SetResourceInMemoryNodeLocalProperties*](setresourceinmemorynodelocalproperties.md)
</dt> <dd>

TBD

</dd> <dt>

[*SetResourceLockedMode*](setresourcelockedmode.md)
</dt> <dd>

Reports that locked mode was configured for a resource.

</dd> <dt>

[*SetResourceStatus*](setresourcestatus.md)
</dt> <dd>

Called to update the status of a [resource](resources.md).

</dd> <dt>

[*SetResourceStatusEx*](setresourcestatusex.md)
</dt> <dd>

Called to update the status of a [resource](resources.md).

</dd> <dt>

[*SignalFailure*](signalfailure.md)
</dt> <dd>

Reports that there was a failure in a resource instance. The **PSIGNAL\_FAILURE\_ROUTINE** type defines a pointer to this function.

</dd> <dt>

[*WorkerStartRoutine*](pworker-start-routine.md)
</dt> <dd>

Initializes a worker thread with the specified callback routine. The **PWORKER\_START\_ROUTINE** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> </dl>

 

 




