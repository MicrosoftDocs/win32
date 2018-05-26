---
title: MSCluster\_DiskToDiskPartition class
description: A dynamic WMI class that represents a list of the disk partitions on a disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47dc7e3f-4635-4da4-8ce1-3d038ac71b47
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_DiskToDiskPartition class
- MSCluster_DiskToDiskPartition class, described
topic_type:
- apiref
api_name:
- MSCluster_DiskToDiskPartition
- MSCluster_DiskToDiskPartition.GroupComponent
- MSCluster_DiskToDiskPartition.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_DiskToDiskPartition class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) that represents a list of the disk partitions on a disk by associating an instance of the [**MSCluster\_Disk**](mscluster-disk.md) class representing a disk resource with instances of the [**MSCluster\_DiskPartition**](mscluster-diskpartition.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{960c49e0-ae52-4888-9136-21441fe642dd}"), AMENDMENT]
class MSCluster_DiskToDiskPartition : CIM_Component
{
  MSCluster_Disk          REF GroupComponent;
  MSCluster_DiskPartition REF PartComponent;
};
```

## Members

The **MSCluster\_DiskToDiskPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_DiskToDiskPartition** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Disk**](mscluster-disk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Provides the disk.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_DiskPartition**](mscluster-diskpartition.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

Provides a partition on this disk.

</dd> </dl>

## Remarks

The [**MSCluster\_ResourceToDisk**](mscluster-resourcetodisk.md) class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

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
</dt> </dl>

 

 





