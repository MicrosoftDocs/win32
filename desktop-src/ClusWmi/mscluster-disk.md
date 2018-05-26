---
title: MSCluster\_Disk class
description: A dynamic WMI class that represents a disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b311cfa8-7dea-42f1-970e-8cd4b1c8a27f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_Disk class
- MSCluster_Disk class, described
topic_type:
- apiref
api_name:
- MSCluster_Disk
- MSCluster_Disk.Caption
- MSCluster_Disk.Description
- MSCluster_Disk.InstallDate
- MSCluster_Disk.Name
- MSCluster_Disk.Status
- MSCluster_Disk.Flags
- MSCluster_Disk.Characteristics
- MSCluster_Disk.Id
- MSCluster_Disk.Signature
- MSCluster_Disk.GptGuid
- MSCluster_Disk.ScsiPort
- MSCluster_Disk.ScsiBus
- MSCluster_Disk.ScsiTargetID
- MSCluster_Disk.ScsiLUN
- MSCluster_Disk.Size
- MSCluster_Disk.Number
- MSCluster_Disk.VirtualDiskId
- MSCluster_Disk.StoragePoolId
- MSCluster_Disk.UniqueId
- MSCluster_Disk.UniqueIdFormat
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_Disk class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a disk.

**Windows Server 2008 R2 and Windows Server 2008:  **

Before Windows Server 2012 this class inherited directly from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md). Beginning in Windows Server 2012 it inherits from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md) and does not add any properties of its own.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{CE14ADB3-953E-4243-8001-5AF0AA83FD1A}"), AMENDMENT]
class MSCluster_Disk : MSCluster_ClusterDisk
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  uint32   Flags;
  uint32   Characteristics;
  string   Id;
  uint32   Signature;
  string   GptGuid;
  uint32   ScsiPort;
  uint32   ScsiBus;
  uint32   ScsiTargetID;
  uint32   ScsiLUN;
  uint64   Size;
  uint32   Number;
  string   VirtualDiskId;
  string   StoragePoolId;
  string   UniqueId;
  UInt16   UniqueIdFormat;
};
```

## Members

The **MSCluster\_Disk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_Disk** class has these properties.

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

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**GptGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the GUID for GPT disks. For MBR disks, this property is not populated.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

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

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the disk was installed. A lack of a value does not indicate that the disk is not installed.

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

**Windows Server 2008 R2 and Windows Server 2008:  **

Due to inheritance restructuring, this property is not available on this class before Windows Server 2012.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**ScsiBus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI bus of the disk.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**ScsiLUN**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI LUN of the disk.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**ScsiPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI port number of the disk.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**ScsiTargetID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the SCSI target ID of the disk.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**Signature**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the signature for MBR disks. For GPT disks, this property is not populated.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The physical size of the disk.")

**Windows Server 2008 R2 and Windows Server 2008:  **

Due to inheritance restructuring, this property is not available on this class before Windows Server 2012.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

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

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**UniqueId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains the VPD Page 0x83 information that uniquely identifies this disk. The **UniqueIdFormat** property indicates the type of Id used. If the disk is an exposed VirtualDisk, **UniqueId** is used to map the association between the two disks.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

</dd> <dt>

**UniqueIdFormat**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the VPD Page 0x83 descriptor type used to populate the **UniqueId** property.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

<dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific** (0)


</dt> <dd></dd> <dt>

<span id="Vendor_Id"></span><span id="vendor_id"></span><span id="VENDOR_ID"></span>

**Vendor Id** (1)


</dt> <dd></dd> <dt>

<span id="EUI64"></span><span id="eui64"></span>

**EUI64** (2)


</dt> <dd></dd> <dt>

<span id="FCPH_Name"></span><span id="fcph_name"></span><span id="FCPH_NAME"></span>

**FCPH Name** (3)


</dt> <dd></dd> <dt>

<span id="SCSI_Name_String"></span><span id="scsi_name_string"></span><span id="SCSI_NAME_STRING"></span>

**SCSI Name String** (8)


</dt> <dd></dd> </dl>

</dd> <dt>

**VirtualDiskId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The id of the virtual disk.

**Windows Server 2008 R2 and Windows Server 2008:  **

Due to inheritance restructuring, this property is not available on this class before Windows Server 2012.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

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

[**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





