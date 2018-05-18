---
title: MSCluster\_ClusterDisk class
description: A dynamic WMI class that represents a disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8EFE9D7A-1990-4B89-B703-00B6AB5E5F1A'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ClusterDisk class", "MSCluster_ClusterDisk class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterDisk
- MSCluster_ClusterDisk.Caption
- MSCluster_ClusterDisk.Description
- MSCluster_ClusterDisk.InstallDate
- MSCluster_ClusterDisk.Name
- MSCluster_ClusterDisk.Status
- MSCluster_ClusterDisk.Flags
- MSCluster_ClusterDisk.Characteristics
- MSCluster_ClusterDisk.Id
- MSCluster_ClusterDisk.Signature
- MSCluster_ClusterDisk.GptGuid
- MSCluster_ClusterDisk.ScsiPort
- MSCluster_ClusterDisk.ScsiBus
- MSCluster_ClusterDisk.ScsiTargetID
- MSCluster_ClusterDisk.ScsiLUN
- MSCluster_ClusterDisk.Size
- MSCluster_ClusterDisk.Number
- MSCluster_ClusterDisk.VirtualDiskId
- MSCluster_ClusterDisk.StoragePoolId
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ClusterDisk class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a disk. This is the parent class for the [**MSCluster\_Disk**](mscluster-disk.md) and [**MSCluster\_AvailableDisk**](mscluster-availabledisk.md) classes.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Provider("MS_CLUSTER_PROVIDER"), UUID("{53C7E15E-E185-4A74-929A-568F5FAF8103}"), AMENDMENT]
class MSCluster_ClusterDisk : MSCluster_LogicalElement
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  uint32   Flags;
  uint32   Characteristics;
  string   Id;
  uint32   Signature;
  string   GptGuid;
  uint32   ScsiPort;
  uint32   ScsiBus;
  uint32   ScsiTargetID;
  uint32   ScsiLUN;
  uint64   Size;
  uint32   Number;
  string   VirtualDiskId;
  string   StoragePoolId;
};
```

## Members

The **MSCluster\_ClusterDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterDisk** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the disk.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the disk. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

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

Provides a textual description of the disk.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the flags set for the disk. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**GptGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the GUID for GPT disks. For MBR disks, this property is not populated.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Provides the ID of the disk. For virtual disks, the property value is "Space Id". For non-virtual disks, the property value contains the same value as either the **GptGuid** property (for GPT disks) or the **Signature** property (for MBR disks).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A datetime value indicating when the disk was installed. A lack of a value does not indicate that the disk is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Defines the label by which the disk is known.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Number**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The disk number on the node hosting the disk.

</dd> <dt>

**ScsiBus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI bus of the disk.

</dd> <dt>

**ScsiLUN**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI LUN of the disk.

</dd> <dt>

**ScsiPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI port number of the disk.

</dd> <dt>

**ScsiTargetID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI target ID of the disk.

</dd> <dt>

**Signature**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the signature for MBR disks. For GPT disks, this property is not populated.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The physical size of the disk.")

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the disk.

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

**StoragePoolId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the storage pool ID for MBR disks. For GPT disks, this property is not populated.

</dd> <dt>

**VirtualDiskId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The id of the virtual disk.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_LogicalElement**](mscluster-logicalelement.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Disk**](mscluster-disk.md)
</dt> <dt>

[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)
</dt> </dl>

 

 





