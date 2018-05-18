---
title: MSCluster\_ClusterToAvailableDisk class
description: Represents a list of the available disks contained in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7d4bbde2-638b-41a4-8909-5e3bf93dea5a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ClusterToAvailableDisk class", "MSCluster_ClusterToAvailableDisk class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterToAvailableDisk
- MSCluster_ClusterToAvailableDisk.GroupComponent
- MSCluster_ClusterToAvailableDisk.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ClusterToAvailableDisk class

Represents a list of the available disks contained in a cluster.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{A02673D9-06DF-4CB0-85A3-7D32C2278C16}"), AMENDMENT]
class MSCluster_ClusterToAvailableDisk : CIM_Component
{
  MSCluster_Cluster       REF GroupComponent;
  MSCluster_AvailableDisk REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterToAvailableDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterToAvailableDisk** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Cluster**](mscluster-cluster.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Provides the cluster.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Provides the available disks associated with this cluster.

</dd> </dl>

## Remarks

The **MSCluster\_ClusterToAvailableDisk** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
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

[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)
</dt> </dl>

 

 





