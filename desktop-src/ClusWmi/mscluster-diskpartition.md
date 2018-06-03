---
title: MSCluster\_DiskPartition class
description: A dynamic WMI class that represents a disk partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 860201b2-ff71-43b3-a0bb-ae450af645d1
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_DiskPartition class
- MSCluster_DiskPartition class, described
topic_type:
- apiref
api_name:
- MSCluster_DiskPartition
- MSCluster_DiskPartition.Caption
- MSCluster_DiskPartition.Description
- MSCluster_DiskPartition.InstallDate
- MSCluster_DiskPartition.Name
- MSCluster_DiskPartition.Status
- MSCluster_DiskPartition.Flags
- MSCluster_DiskPartition.Characteristics
- MSCluster_DiskPartition.Path
- MSCluster_DiskPartition.VolumeLabel
- MSCluster_DiskPartition.SerialNumber
- MSCluster_DiskPartition.MaximumComponentLength
- MSCluster_DiskPartition.FileSystemFlags
- MSCluster_DiskPartition.FileSystem
- MSCluster_DiskPartition.TotalSize
- MSCluster_DiskPartition.FreeSpace
- MSCluster_DiskPartition.PartitionNumber
- MSCluster_DiskPartition.VolumeGuid
- MSCluster_DiskPartition.MountPoints
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_DiskPartition class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a disk partition.

**Windows Server 2008 R2 and Windows Server 2008:  **

Before Windows Server 2012 this class inherited directly from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md). Beginning in Windows Server 2012 it inherits from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md) and does not add any properties of its own.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{A514C185-BE72-4C75-8225-FF1A4FFAA7C8}")]
class MSCluster_DiskPartition : MSCluster_ClusterDiskPartition
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  uint32   Flags;
  uint32   Characteristics;
  string   Path;
  string   VolumeLabel;
  uint32   SerialNumber;
  uint32   MaximumComponentLength;
  uint32   FileSystemFlags;
  string   FileSystem;
  uint32   TotalSize;
  uint32   FreeSpace;
  uint32   PartitionNumber;
  string   VolumeGuid;
  string   MountPoints[];
};
```

## Members

The **MSCluster\_DiskPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_DiskPartition** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the partition.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the partition. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the partition.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**FileSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**FileSystem**](https://msdn.microsoft.com/library/aa368116) property, which is the file system defined for the partition.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**FileSystemFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**FileSystemFlags**](https://msdn.microsoft.com/library/aa368117) property, which is any descriptive flags set for the partition's file system.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

Values include the following:

<dt>

1
</dt> <dd>

The file system supports case-sensitive file names.

</dd> <dt>

2
</dt> <dd>

The file system preserves the case of file names when it places a name on the storage class resource.

</dd> <dt>

4
</dt> <dd>

The file system supports Unicode in file names as they appear on storage class resource.

</dd> <dt>

8
</dt> <dd>

The file system preserves and enforces access control lists (ACLs).

</dd> </dl>

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the flags set for the partition. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**FreeSpace**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the total space available for the partition, in megabytes.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the partition was installed. A lack of a value does not indicate that the partition is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**MaximumComponentLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**MaximumComponentLength**](https://msdn.microsoft.com/library/aa368119) property, which is the maximum file name component length, in characters, allowed by the partition's file system.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**MountPoints**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The mount points of the partition.

**Windows Server 2008 R2 and Windows Server 2008:  **

Due to inheritance restructuring, this property is not available on this class before Windows Server 2012.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Defines the label by which the partition is known.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**PartitionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the partition number of the partition.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Provides the path, including the drive letter if present, of the clustered disk partition.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**SerialNumber**](https://msdn.microsoft.com/library/aa368121) property, which is the partition serial number.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the partition.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> </dl>

</dd> <dt>

**TotalSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the total size for the partition, in megabytes.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the volume **GUID** of the partition.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> <dt>

**VolumeLabel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**VolumeLabel**](https://msdn.microsoft.com/library/aa368122) property, which is the volume label of the partition.

This property is inherited from [**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md).

</dd> </dl>

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

[**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





