---
title: MSCluster\_ClusterSharedVolumeToPartition class
description: A cluster shared volume has a partition. This lists the cluster shared volume partition information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 99fbc217-0703-4c14-bfd8-2e1cd8ca02ac
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterSharedVolumeToPartition class
- MSCluster_ClusterSharedVolumeToPartition class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterSharedVolumeToPartition
- MSCluster_ClusterSharedVolumeToPartition.GroupComponent
- MSCluster_ClusterSharedVolumeToPartition.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_ClusterSharedVolumeToPartition class

A cluster shared volume has a partition. This lists the cluster shared volume partition information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{6e861fe6-2f66-4361-ab71-90b87aef3a79}"), AMENDMENT]
class MSCluster_ClusterSharedVolumeToPartition : CIM_Component
{
  MSCluster_ClusterSharedVolume REF GroupComponent;
  MSCluster_DiskPartition       REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterSharedVolumeToPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterSharedVolumeToPartition** class has these properties.

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

Data type: **MSCluster\_DiskPartition**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The cluster shared volume partition.

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

 

 





