---
title: MSCluster\_AvailableDiskPartition class
description: A dynamic WMI class that represents an available disk partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4F8C2FD7-0426-41D3-BC8C-E1829D6E46DB'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_AvailableDiskPartition class", "MSCluster_AvailableDiskPartition class, described"]
topic_type:
- apiref
api_name:
- MSCluster_AvailableDiskPartition
- MSCluster_AvailableDiskPartition.Caption
- MSCluster_AvailableDiskPartition.Description
- MSCluster_AvailableDiskPartition.InstallDate
- MSCluster_AvailableDiskPartition.Name
- MSCluster_AvailableDiskPartition.Status
- MSCluster_AvailableDiskPartition.Flags
- MSCluster_AvailableDiskPartition.Characteristics
- MSCluster_AvailableDiskPartition.Path
- MSCluster_AvailableDiskPartition.VolumeLabel
- MSCluster_AvailableDiskPartition.SerialNumber
- MSCluster_AvailableDiskPartition.MaximumComponentLength
- MSCluster_AvailableDiskPartition.FileSystemFlags
- MSCluster_AvailableDiskPartition.FileSystem
- MSCluster_AvailableDiskPartition.TotalSize
- MSCluster_AvailableDiskPartition.FreeSpace
- MSCluster_AvailableDiskPartition.PartitionNumber
- MSCluster_AvailableDiskPartition.VolumeGuid
- MSCluster_AvailableDiskPartition.MountPoints
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_AvailableDiskPartition class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents an available disk partition.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{56F929D9-1593-49FB-8D5C-0599B582C44B}")]
class MSCluster_AvailableDiskPartition : MSCluster_ClusterDiskPartition
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

The **MSCluster\_AvailableDiskPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_AvailableDiskPartition** class has these properties.

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

Provides the characteristics of the object. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

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

Provides access to the flags set for the object. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

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

A datetime value indicating when the partition was installed. A lack of a value does not indicate that the partition is not installed.

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

The Name property defines the label by which the partition is known.

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

A string indicating the current status of the object. Various operational and non-operational statuses are defined. Operational statuses are "OK", "Degraded", "Stressed" and "Pred Fail". "Stressed" indicates that the Element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, etc. The condition "Pred Fail" (failure predicted) indicates that an Element is functioning properly but predicting a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses can also be specified. These are "Error", "NonRecover", "Starting", "Stopping" and "Service". "NonRecover" indicates that a non-recoverable error has occurred. "Service" describes an Element being configured, maintained or cleaned, or otherwise administered. This status could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative task. Not all such work is on-line, yet the Element is neither "OK" nor in one of the other states.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





