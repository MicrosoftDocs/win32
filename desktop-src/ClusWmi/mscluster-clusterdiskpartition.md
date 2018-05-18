---
title: MSCluster\_ClusterDiskPartition class
description: The base class which provides the common properties for cluster disk partitions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '71FC6737-FB98-4A42-ACEB-6B8A8131B988'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ClusterDiskPartition class", "MSCluster_ClusterDiskPartition class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterDiskPartition
- MSCluster_ClusterDiskPartition.Caption
- MSCluster_ClusterDiskPartition.Description
- MSCluster_ClusterDiskPartition.InstallDate
- MSCluster_ClusterDiskPartition.Name
- MSCluster_ClusterDiskPartition.Status
- MSCluster_ClusterDiskPartition.Flags
- MSCluster_ClusterDiskPartition.Characteristics
- MSCluster_ClusterDiskPartition.Path
- MSCluster_ClusterDiskPartition.VolumeLabel
- MSCluster_ClusterDiskPartition.SerialNumber
- MSCluster_ClusterDiskPartition.MaximumComponentLength
- MSCluster_ClusterDiskPartition.FileSystemFlags
- MSCluster_ClusterDiskPartition.FileSystem
- MSCluster_ClusterDiskPartition.TotalSize
- MSCluster_ClusterDiskPartition.FreeSpace
- MSCluster_ClusterDiskPartition.PartitionNumber
- MSCluster_ClusterDiskPartition.VolumeGuid
- MSCluster_ClusterDiskPartition.MountPoints
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ClusterDiskPartition class

The base class which provides the common properties for cluster disk partitions. This is the parent class of the [**MSCluster\_DiskPartition**](mscluster-diskpartition.md) and [**MSCluster\_AvailableDiskPartition**](mscluster-availablediskpartition.md) classes.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Provider("MS_CLUSTER_PROVIDER"), UUID("{1C6677C6-B636-4A27-9831-4FBCB3582F8A}"), AMENDMENT]
class MSCluster_ClusterDiskPartition : MSCluster_LogicalElement
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  uint32   Flags;
  uint32   Characteristics;
  string   Path;
  string   VolumeLabel;
  uint32   SerialNumber;
  uint32   MaximumComponentLength;
  uint32   FileSystemFlags;
  string   FileSystem;
  uint32   TotalSize;
  uint32   FreeSpace;
  uint32   PartitionNumber;
  string   VolumeGuid;
  string   MountPoints[];
};
```

## Members

The **MSCluster\_ClusterDiskPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterDiskPartition** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the disk partition.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the disk partition. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the disk partition.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**FileSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**FileSystem**](https://msdn.microsoft.com/library/aa368116) property, which is the file system defined for the partition.

</dd> <dt>

**FileSystemFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**FileSystemFlags**](https://msdn.microsoft.com/library/aa368117) property, which is any descriptive flags set for the partition's file system.

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

Provides access to the flags set for the disk partition. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**FreeSpace**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the total space available for the partition, in megabytes.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the disk partition was installed. A lack of a value does not indicate that the disk partition is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**MaximumComponentLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**MaximumComponentLength**](https://msdn.microsoft.com/library/aa368119) property, which is the maximum file name component length, in characters, allowed by the partition's file system.

</dd> <dt>

**MountPoints**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The mount points of the partition.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Defines the label by which the disk partition is known. When subclassed, the Name property can be overridden to be a Key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**PartitionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the partition number of the partition.

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

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**SerialNumber**](https://msdn.microsoft.com/library/aa368121) property, which is the partition serial number.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the disk partition.

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

</dd> <dt>

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the volume **GUID** of the partition.

</dd> <dt>

**VolumeLabel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the [**VolumeLabel**](https://msdn.microsoft.com/library/aa368122) property, which is the volume label of the partition.

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

[**MSCluster\_LogicalElement**](mscluster-logicalelement.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





