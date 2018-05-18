---
title: MSCluster\_ClusterSharedVolumeToResource class
description: A cluster shared volume has a resource associated with it. This lists the cluster resource which is the cluster shared volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0321b55e-301e-4558-b648-c271110c7ed4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ClusterSharedVolumeToResource class", "MSCluster_ClusterSharedVolumeToResource class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterSharedVolumeToResource
- MSCluster_ClusterSharedVolumeToResource.GroupComponent
- MSCluster_ClusterSharedVolumeToResource.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ClusterSharedVolumeToResource class

A cluster shared volume has a resource associated with it. This lists the cluster resource which is the cluster shared volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{348a16a2-4d97-4e56-82e6-d08a23fe927a}"), AMENDMENT]
class MSCluster_ClusterSharedVolumeToResource : CIM_Component
{
  MSCluster_ClusterSharedVolume REF GroupComponent;
  MSCluster_Resource            REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterSharedVolumeToResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterSharedVolumeToResource** class has these properties.

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

Data type: **MSCluster\_Resource**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The cluster resource associated with the cluster shared volume.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 





