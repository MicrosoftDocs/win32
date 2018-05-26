---
title: Internal Resource Control Codes
description: The following lists all of the internal control codes for resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00d6c57a-9a78-48f7-a58f-b9ed3b87df17
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource control codes Failover Cluster ,internal
- control codes Failover Cluster ,resource,internal
- resources Failover Cluster ,control codes,internal
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Internal Resource Control Codes

The following lists all of the internal control codes for resources.

## In this section

<dl> <dt>

[CLUSCTL\_RESOURCE\_NOTIFY\_OWNER\_CHANGE](clusctl-resource-notify-owner-change.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [node](nodes.md) is TBD. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_VALIDATE\_CHANGE\_GROUP](clusctl-resource-validate-change-group.md)
</dt> <dd>

TBD. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_UPGRADE\_COMPLETED](clusctl-resource-upgrade-completed.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a rolling upgrade of the operating system on a cluster is complete. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_PREPARE\_UPGRADE](clusctl-resource-prepare-upgrade.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a rolling upgrade of the operating systems on a cluster has started. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ADD\_DEPENDENCY](clusctl-resource-add-dependency.md)
</dt> <dd>

Internal. Notifies a [resource DLL](resource-dlls.md) that a [dependency](resource-dependencies.md) being added to a [resource](resources.md) managed by the DLL. Resource DLLs receive this [control code](about-control-codes.md) as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ADD\_OWNER](clusctl-resource-add-owner.md)
</dt> <dd>

Internal. Notifies a [resource DLL](resource-dlls.md) that a [node](nodes.md) has been added to the list of [possible owner](p-gly.md#-wolf-possible-owner-gly) nodes for a [resource](resources.md) managed by the DLL. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_CLUSTER\_NAME\_CHANGED](clusctl-resource-cluster-name-changed.md)
</dt> <dd>

Internal. The CLUSCTL\_RESOURCE\_CLUSTER\_NAME\_CHANGED [control code](about-control-codes.md) is reserved for internal use only. It informs the core [network name](network-name.md) resource that the name of the [cluster](c-gly.md#-wolf-cluster-gly) has changed.

</dd> <dt>

[CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED](clusctl-resource-cluster-version-changed.md)
</dt> <dd>

Internal. Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that the cluster version has changed. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_DELETE](clusctl-resource-delete.md)
</dt> <dd>

Internal. Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [resource](resources.md) it is managing is about to be deleted from the [cluster](c-gly.md#-wolf-cluster-gly). Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_EVICT\_NODE](clusctl-resource-evict-node.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [node](nodes.md) is being permanently removed from the [cluster](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly). Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FORCE\_QUORUM](clusctl-resource-force-quorum.md)
</dt> <dd>

Establishes the set of [nodes](nodes.md) that are sufficient to force quorum in a majority-of-nodes cluster. (For more information, see [Quorum Resource](quorum-resource.md).) Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FSWITNESS\_GET\_EPOCH\_INFO](clusctl-resource-fswitness-get-epoch-info.md)
</dt> <dd>

Retrieves the epoch information from the witness file stored on a remote file share.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FSWITNESS\_RELEASE\_LOCK](clusctl-resource-fswitness-release-lock.md)
</dt> <dd>

Releases the lock on the witness file.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FSWITNESS\_SET\_EPOCH\_INFO](clusctl-resource-fswitness-set-epoch-info.md)
</dt> <dd>

Stores the epoch information in the witness file stored on a remote file share.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_OPERATION\_CONTEXT](clusctl-resource-get-operation-context.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that an operation context is being retrieved.

Resource DLLs receive this [control code](about-control-codes.md) as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_INITIALIZE](clusctl-resource-initialize.md)
</dt> <dd>

Used by the resource to initialize any state after it has been created for the first time. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_INSTALL\_NODE](clusctl-resource-install-node.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [node](nodes.md) is being added to the cluster. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_JOINING\_GROUP](clusctl-resource-joining-group.md)
</dt> <dd>

Tells a resource when it is joining a group.

</dd> <dt>

[CLUSCTL\_RESOURCE\_LEAVING\_GROUP](clusctl-resource-leaving-group.md)
</dt> <dd>

Tells a resource when it is leaving a group.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_CREDS\_NOTIFYCAM](clusctl-resource-netname-creds-notifycam.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_NETNAME\_CREDS\_NOTIFYCAM](clusctl-resource-netname-creds-notifycam.md) [control code](about-control-codes.md) is reserved for internal use only.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NOTIFY\_QUORUM\_STATUS](clusctl-resource-notify-quorum-status.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) about the status of a quorum resource.

Resource DLLs receive this [control code](about-control-codes.md) as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_PROVIDER\_STATE\_CHANGE](clusctl-resource-provider-state-change.md)
</dt> <dd>

TBD. Resource DLLs receive this [control code](about-control-codes.md) as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_QUERY\_CSV\_MAINTENANCE\_MODE](clusctl-resource-query-csv-maintenance-mode.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_QUERY\_CSV\_MAINTENANCE\_MODE](clusctl-resource-query-csv-maintenance-mode.md) [control code](about-control-codes.md) is reserved for internal use only.

</dd> <dt>

[CLUSCTL\_RESOURCE\_REMOVE\_DEPENDENCY](clusctl-resource-remove-dependency.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a dependency is being removed from a [resource](resources.md) managed by the DLL. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_REMOVE\_OWNER](clusctl-resource-remove-owner.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that a [node](nodes.md) is being removed from the list of [possible owner](p-gly.md#-wolf-possible-owner-gly) nodes for a [resource](resources.md) managed by the DLL. Resource DLLs receive this [control code](about-control-codes.md) as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_RW\_MODIFY\_NOOP](clusctl-resource-rw-modify-noop.md)
</dt> <dd>

TBD.

Resource DLLs receive this [control code](about-control-codes.md) as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_CLUSTER\_MEMBERSHIP](clusctl-resource-set-cluster-membership.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_SET\_CLUSTER\_MEMBERSHIP](clusctl-resource-set-cluster-membership.md) [control code](about-control-codes.md) is reserved for internal use only.

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_NAME](clusctl-resource-set-name.md)
</dt> <dd>

Used by the [Cluster service](cluster-service.md) to notify a [resource DLL](resource-dlls.md) that the name of a [resource](resources.md) has been changed. Because the [control code](about-control-codes.md) is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_SHARED\_PR\_KEY](clusctl-resource-set-shared-pr-key.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_SET\_SHARED\_PR\_KEY](clusctl-resource-set-shared-pr-key.md) [control code](about-control-codes.md) is reserved for internal use only.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md)
</dt> <dd>

Under certain circumstances, the cluster sends the [CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md) [control code](about-control-codes.md) to a [resource DLL](resource-dlls.md) immediately before calling the [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master) or [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry-point function, providing the DLL with the reason for the state change. Because the control code is internal, applications cannot use it in a control code function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_CSV\_DISK\_INFO](clusctl-resource-storage-get-csv-disk-info.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_STORAGE\_GET\_CSV\_DISK\_INFO](clusctl-resource-storage-get-csv-disk-info.md) [control code](about-control-codes.md) is reserved for internal use only.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_NUMBER](clusctl-resource-storage-get-disk-number.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_NUMBER](clusctl-resource-storage-get-disk-number.md) [control code](about-control-codes.md) is reserved for internal use only.

</dd> </dl>

## Related topics

<dl> <dt>

[Resource Control Codes](resource-control-codes.md)
</dt> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 




