---
title: MSCluster\_ClusterToResourceGroup class
description: A dynamic association WMI class that provides access to the groups in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5dc24a48-15f6-46ec-9352-5e0cf104faad
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterToResourceGroup class
- MSCluster_ClusterToResourceGroup class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterToResourceGroup
- MSCluster_ClusterToResourceGroup.GroupComponent
- MSCluster_ClusterToResourceGroup.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ClusterToResourceGroup class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that provides access to the groups in a [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{191A06A0-4B96-4914-ABD6-6F7E5F73A191}"), AMENDMENT]
class MSCluster_ClusterToResourceGroup : CIM_Component
{
  MSCluster_Cluster       REF GroupComponent;
  MSCluster_ResourceGroup REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterToResourceGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterToResourceGroup** class has these properties.

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

Data type: **[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The group managed by cluster.

</dd> </dl>

## Remarks

The **MSCluster\_ClusterToResourceGroup** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

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

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





