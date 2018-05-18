---
title: ClusResGroup.State property
description: Returns the state of a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7eb8662c-a6ca-46e5-99ee-84e0dd6b0961'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["State property Failover Cluster", "State property Failover Cluster , ClusResGroup class", "ClusResGroup class Failover Cluster , State property"]
topic_type:
- apiref
api_name:
- ClusResGroup.State
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroup.State property

\[The **State** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the state of a [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.State As CLUSTER_GROUP_STATE
```



## Property value

The **State** property returns one of the following values.

<dt>

<span id="ClusterGroupStateUnknown"></span><span id="clustergroupstateunknown"></span><span id="CLUSTERGROUPSTATEUNKNOWN"></span>

<span id="ClusterGroupStateUnknown"></span><span id="clustergroupstateunknown"></span><span id="CLUSTERGROUPSTATEUNKNOWN"></span>**ClusterGroupStateUnknown** (-1)


</dt> <dd>

The **State** property has failed; the state of the group is unknown.

</dd> <dt>

<span id="ClusterGroupOnline"></span><span id="clustergrouponline"></span><span id="CLUSTERGROUPONLINE"></span>

<span id="ClusterGroupOnline"></span><span id="clustergrouponline"></span><span id="CLUSTERGROUPONLINE"></span>**ClusterGroupOnline** (0)


</dt> <dd>

All of the resources in the group are [*online*](o-gly.md#-wolf-online-gly).

</dd> <dt>

<span id="ClusterGroupOffline"></span><span id="clustergroupoffline"></span><span id="CLUSTERGROUPOFFLINE"></span>

<span id="ClusterGroupOffline"></span><span id="clustergroupoffline"></span><span id="CLUSTERGROUPOFFLINE"></span>**ClusterGroupOffline** (1)


</dt> <dd>

All of the resources in the group are [*offline*](o-gly.md#-wolf-offline-gly) or there are no resources in the group.

</dd> <dt>

<span id="ClusterGroupFailed"></span><span id="clustergroupfailed"></span><span id="CLUSTERGROUPFAILED"></span>

<span id="ClusterGroupFailed"></span><span id="clustergroupfailed"></span><span id="CLUSTERGROUPFAILED"></span>**ClusterGroupFailed** (2)


</dt> <dd>

At least one [resource](resources.md) in the group has failed.

</dd> <dt>

<span id="ClusterGroupPartialOnline"></span><span id="clustergrouppartialonline"></span><span id="CLUSTERGROUPPARTIALONLINE"></span>

<span id="ClusterGroupPartialOnline"></span><span id="clustergrouppartialonline"></span><span id="CLUSTERGROUPPARTIALONLINE"></span>**ClusterGroupPartialOnline** (3)


</dt> <dd>

At least one resource in the group is online. No resources are [*pending*](p-gly.md#-wolf-pending-gly) or [*failed*](f-gly.md#-wolf-failed-gly).

</dd> <dt>

<span id="ClusterGroupPending"></span><span id="clustergrouppending"></span><span id="CLUSTERGROUPPENDING"></span>

<span id="ClusterGroupPending"></span><span id="clustergrouppending"></span><span id="CLUSTERGROUPPENDING"></span>**ClusterGroupPending** (4)


</dt> <dd>

At least one resource in the group is in a pending state. There are no failed resources.

</dd> </dl>

To retrieve the state of a node or resource, use the **State** property of the appropriate [**ClusNode**](clusnode-object.md) or [**ClusResource**](clusresource-object.md) object.

## Remarks

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**CLUSTER\_GROUP\_STATE**](cluster-group-state.md)
</dt> </dl>

 

 





