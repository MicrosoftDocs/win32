---
title: MSCluster\_AvailableDiskToPartition class
description: Represents a list of the partitions on the available disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7D337B1B-9ABC-4DDC-9D74-EEC5B3E311D5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_AvailableDiskToPartition class", "MSCluster_AvailableDiskToPartition class, described"]
topic_type:
- apiref
api_name:
- MSCluster_AvailableDiskToPartition
- MSCluster_AvailableDiskToPartition.GroupComponent
- MSCluster_AvailableDiskToPartition.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_AvailableDiskToPartition class

Represents a list of the partitions on the available disk.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{BCF05714-EA46-47F8-8F80-1CC9946E0FD6}"), AMENDMENT]
class MSCluster_AvailableDiskToPartition : CIM_Component
{
  MSCluster_AvailableDisk          REF GroupComponent;
  MSCluster_AvailableDiskPartition REF PartComponent;
};
```

## Members

The **MSCluster\_AvailableDiskToPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_AvailableDiskToPartition** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The available disk.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_AvailableDiskPartition**](mscluster-availablediskpartition.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The available disk partition.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)
</dt> <dt>

[**MSCluster\_AvailableDiskPartition**](mscluster-availablediskpartition.md)
</dt> </dl>

 

 





