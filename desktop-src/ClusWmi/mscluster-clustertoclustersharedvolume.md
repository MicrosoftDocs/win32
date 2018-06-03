---
title: MSCluster\_ClusterToClusterSharedVolume class
description: Represents a list of the available cluster shared volumes contained in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e6e74ca9-82fe-42d6-a725-adfda7491699
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterToClusterSharedVolume class
- MSCluster_ClusterToClusterSharedVolume class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterToClusterSharedVolume
- MSCluster_ClusterToClusterSharedVolume.GroupComponent
- MSCluster_ClusterToClusterSharedVolume.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_ClusterToClusterSharedVolume class

Represents a list of the available cluster shared volumes contained in a cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{74e21b21-e651-42e8-8312-13cab5db7844}"), AMENDMENT]
class MSCluster_ClusterToClusterSharedVolume : CIM_Component
{
  MSCluster_Cluster             REF GroupComponent;
  MSCluster_ClusterSharedVolume REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterToClusterSharedVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterToClusterSharedVolume** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Cluster**](mscluster-cluster.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The cluster.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_ClusterSharedVolume**](mscluster-clustersharedvolume.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The shared volume resource associate with this cluster.

</dd> </dl>

## Remarks

The **MSCluster\_ClusterToClusterSharedVolume** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> <dt>

[**MSCluster\_ClusterSharedVolume**](mscluster-clustersharedvolume.md)
</dt> </dl>

 

 





