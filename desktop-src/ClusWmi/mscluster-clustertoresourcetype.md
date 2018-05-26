---
title: MSCluster\_ClusterToResourceType class
description: A dynamic association WMI class that represents the groups in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b58ea1bd-87c3-45a6-afd2-36506c8cd9c7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterToResourceType class
- MSCluster_ClusterToResourceType class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterToResourceType
- MSCluster_ClusterToResourceType.GroupComponent
- MSCluster_ClusterToResourceType.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ClusterToResourceType class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [groups](https://msdn.microsoft.com/library/aa369645) in the [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{1059D8CA-76CF-46dc-A14B-B7BB546270AD}"), AMENDMENT]
class MSCluster_ClusterToResourceType : CIM_Component
{
  MSCluster_Cluster      REF GroupComponent;
  MSCluster_ResourceType REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterToResourceType** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterToResourceType** class has these properties.

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

Data type: **[**MSCluster\_ResourceType**](mscluster-resourcetype.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The [resource type](https://msdn.microsoft.com/library/aa372279) supported by cluster.

</dd> </dl>

## Remarks

The **MSCluster\_ClusterToResourceType** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
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

[**MSCluster\_ResourceType**](mscluster-resourcetype.md)
</dt> </dl>

 

 





