---
title: Resource DLL Callback Functions
description: The resource DLL callback functions allow a resource DLL to report status and event information to a Resource Monitor, which then provides the information to the Cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c7de7e6-a0f5-4308-8cf3-21968bd339a4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLL functions Failover Cluster ,callback functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resource DLL Callback Functions

The resource DLL callback functions allow a [resource DLL](resource-dlls.md) to report status and event information to a [Resource Monitor](resource-monitor.md), which then provides the information to the [Cluster service](cluster-service.md). These callback functions are implemented by a Resource Monitor and invoked by a resource DLL.

For information about create resource DLLs, see [Creating Resource Types](creating-resource-types.md).

## In this section

<dl> <dt>

[*ChangeResourceProcessForDumps*](/windows/previous-versions/ResApi/nc-resapi-pchange_resource_process_for_dumps?branch=master)
</dt> <dd>

The **PCHANGE\_RESOURCE\_PROCESS\_FOR\_DUMPS** type defines a pointer to this function.

</dd> <dt>

[*ChangeResTypeProcessForDumps*](/windows/previous-versions/ResApi/nc-resapi-pchange_res_type_process_for_dumps?branch=master)
</dt> <dd>

The **PCHANGE\_RES\_TYPE\_PROCESS\_FOR\_DUMPS** type defines a pointer to this function.

</dd> <dt>

[*EndControlCall*](/windows/previous-versions/ResApi/nc-resapi-pend_control_call?branch=master)
</dt> <dd>

Called when a resource control code operation completes. The **PEND\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*EndTypeControlCall*](/windows/previous-versions/ResApi/nc-resapi-pend_type_control_call?branch=master)
</dt> <dd>

Called when a resource type control code operation completes. The **PEND\_TYPE\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*ExtendControlCall*](/windows/previous-versions/ResApi/nc-resapi-pextend_res_control_call?branch=master)
</dt> <dd>

Extends the timeout for a call to a resource control code. The **PEXTEND\_RES\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*ExtendResTypeControlCall*](/windows/previous-versions/ResApi/nc-resapi-pextend_res_type_control_call?branch=master)
</dt> <dd>

Extends the timeout for a call to a resource type control code. The **PEXTEND\_RES\_TYPE\_CONTROL\_CALL** type defines a pointer to this function.

</dd> <dt>

[*LogEvent*](/windows/previous-versions/ResApi/nc-resapi-plog_event_routine?branch=master)
</dt> <dd>

Records an event in the cluster log.

</dd> <dt>

[*QuorumResourceLost*](/windows/previous-versions/ResApi/nc-resapi-pquorum_resource_lost?branch=master)
</dt> <dd>

Called when control of the [quorum resource](quorum-resource.md) has been lost.

</dd> <dt>

[*RaiseResTypeNotification*](/windows/previous-versions/ResApi/nc-resapi-praise_res_type_notification?branch=master)
</dt> <dd>

TBD. The **PRAISE\_RES\_TYPE\_NOTIFICATION** type is a pointer to this function.

</dd> <dt>

[*ResourceCallback*](/windows/previous-versions/ResApi/nc-resapi-lpresource_callback?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[*ResourceCallbackEx*](/windows/previous-versions/ResApi/nc-resapi-lpresource_callback_ex?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[*SetInternalState*](/windows/previous-versions/ResApi/nc-resapi-pset_internal_state?branch=master)
</dt> <dd>

Sets the internal state of a resource

</dd> <dt>

[*SetResourceInMemoryNodeLocalProperties*](/windows/previous-versions/ResApi/nc-resapi-pset_resource_inmemory_nodelocal_properties_routine?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[*SetResourceLockedMode*](/windows/previous-versions/ResApi/nc-resapi-pset_resource_locked_mode_routine?branch=master)
</dt> <dd>

Reports that locked mode was configured for a resource.

</dd> <dt>

[*SetResourceStatus*](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master)
</dt> <dd>

Called to update the status of a [resource](resources.md).

</dd> <dt>

[*SetResourceStatusEx*](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine_ex?branch=master)
</dt> <dd>

Called to update the status of a [resource](resources.md).

</dd> <dt>

[*SignalFailure*](/windows/previous-versions/ResApi/nc-resapi-psignal_failure_routine?branch=master)
</dt> <dd>

Reports that there was a failure in a resource instance. The **PSIGNAL\_FAILURE\_ROUTINE** type defines a pointer to this function.

</dd> <dt>

[*WorkerStartRoutine*](/windows/previous-versions/ResApi/nc-resapi-pworker_start_routine?branch=master)
</dt> <dd>

Initializes a worker thread with the specified callback routine. The **PWORKER\_START\_ROUTINE** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> </dl>

 

 




