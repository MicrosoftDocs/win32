---
title: MSCluster\_AvailableDisk class
description: A dynamic WMI class that represents an available disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1f5c8a44-dd23-4255-8814-ee5b45dd55d4
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_AvailableDisk class
- MSCluster_AvailableDisk class, described
topic_type:
- apiref
api_name:
- MSCluster_AvailableDisk
- MSCluster_AvailableDisk.Caption
- MSCluster_AvailableDisk.Description
- MSCluster_AvailableDisk.InstallDate
- MSCluster_AvailableDisk.Name
- MSCluster_AvailableDisk.Status
- MSCluster_AvailableDisk.Flags
- MSCluster_AvailableDisk.Characteristics
- MSCluster_AvailableDisk.Id
- MSCluster_AvailableDisk.Signature
- MSCluster_AvailableDisk.GptGuid
- MSCluster_AvailableDisk.ScsiPort
- MSCluster_AvailableDisk.ScsiBus
- MSCluster_AvailableDisk.ScsiTargetID
- MSCluster_AvailableDisk.ScsiLUN
- MSCluster_AvailableDisk.Size
- MSCluster_AvailableDisk.Number
- MSCluster_AvailableDisk.VirtualDiskId
- MSCluster_AvailableDisk.StoragePoolId
- MSCluster_AvailableDisk.Node
- MSCluster_AvailableDisk.ResourceName
- MSCluster_AvailableDisk.ConnectedNodes
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_AvailableDisk class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents an available disk.

**Windows Server 2008 R2 and Windows Server 2008:  **

Before Windows Server 2012 this class inherited directly from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md). Beginning in Windows Server 2012 it inherits from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{A4F69DC3-DD5A-41AB-8108-E7C293E643AD}"), AMENDMENT]
class MSCluster_AvailableDisk : MSCluster_ClusterDisk
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
  string   Node;
  string   ResourceName;
  string   ConnectedNodes[];
};
```

## Members

The **MSCluster\_AvailableDisk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_AvailableDisk** class has these methods.



| Method                                                                         | Description                                                                                                                         |
|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**AddToCluster**](mscluster-availabledisk-addtocluster.md)                   | Adds the available disk to the cluster.<br/>                                                                                  |
| [**CreateStorageResource**](mscluster-availabledisk-createstorageresource.md) | **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/> |



 

### Properties

The **MSCluster\_AvailableDisk** class has these properties.

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

Provides the characteristics of the object. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**ConnectedNodes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The names of the nodes which are connected to the available disk.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

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

Provides access to the flags set for the object. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

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

The Name property defines the label by which the disk is known. When subclassed, the Name property can be overridden to be a Key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Node**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node which provided the disk information.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**Number**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The disk number on the node hosting the disk.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

**Windows Server 2008 R2 and Windows Server 2008:  **

Due to inheritance restructuring, this property is not available on this class before Windows Server 2012.

</dd> <dt>

**ResourceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource name to try when adding the disk to the cluster.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

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

The physical size of the disk.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

**Windows Server 2008 R2 and Windows Server 2008:  **

Due to inheritance restructuring, this property is not available on this class before Windows Server 2012.

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

**StoragePoolId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the storage pool ID for MBR disks. For GPT disks, this property is not populated.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

</dd> <dt>

**VirtualDiskId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The id of the virtual disk.

This property is inherited from [**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md).

**Windows Server 2008 R2 and Windows Server 2008:  **

Due to inheritance restructuring, this property is not available on this class before Windows Server 2012.

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

 

 





