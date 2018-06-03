---
title: MSCluster\_ClusterSharedVolumeToNode class
description: A cluster shared volume has a node hosting the resource. This lists the cluster node hosting cluster shared volume resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64f3a9ae-16bf-40d8-9115-17c4cfd42bdd
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterSharedVolumeToNode class
- MSCluster_ClusterSharedVolumeToNode class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterSharedVolumeToNode
- MSCluster_ClusterSharedVolumeToNode.GroupComponent
- MSCluster_ClusterSharedVolumeToNode.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_ClusterSharedVolumeToNode class

A cluster shared volume has a node hosting the resource. This lists the cluster node hosting cluster shared volume resource.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{f6479c77-f61c-49d7-8098-8125baeab8fd}"), AMENDMENT]
class MSCluster_ClusterSharedVolumeToNode : CIM_Component
{
  MSCluster_ClusterSharedVolume REF GroupComponent;
  MSCluster_Node                REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterSharedVolumeToNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterSharedVolumeToNode** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_ClusterSharedVolume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The cluster shared volume.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The cluster node hosting the cluster shared volume resource.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 





