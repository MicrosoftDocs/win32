---
title: CIM\_StorageAllocationSettingData class
description: Represents settings for the allocation of virtual storage.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec1d5f3b-b7f1-4e1f-933a-1cd923e0cdd0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_StorageAllocationSettingData class
- CIM_StorageAllocationSettingData class, described
topic_type:
- apiref
api_name:
- CIM_StorageAllocationSettingData
- CIM_StorageAllocationSettingData.Caption
- CIM_StorageAllocationSettingData.Description
- CIM_StorageAllocationSettingData.InstanceID
- CIM_StorageAllocationSettingData.ElementName
- CIM_StorageAllocationSettingData.ResourceType
- CIM_StorageAllocationSettingData.OtherResourceType
- CIM_StorageAllocationSettingData.ResourceSubType
- CIM_StorageAllocationSettingData.PoolID
- CIM_StorageAllocationSettingData.ConsumerVisibility
- CIM_StorageAllocationSettingData.HostResource
- CIM_StorageAllocationSettingData.AllocationUnits
- CIM_StorageAllocationSettingData.Weight
- CIM_StorageAllocationSettingData.AutomaticAllocation
- CIM_StorageAllocationSettingData.AutomaticDeallocation
- CIM_StorageAllocationSettingData.Parent
- CIM_StorageAllocationSettingData.Connection
- CIM_StorageAllocationSettingData.Address
- CIM_StorageAllocationSettingData.MappingBehavior
- CIM_StorageAllocationSettingData.AddressOnParent
- CIM_StorageAllocationSettingData.VirtualResourceBlockSize
- CIM_StorageAllocationSettingData.VirtualQuantity
- CIM_StorageAllocationSettingData.VirtualQuantityUnits
- CIM_StorageAllocationSettingData.Access
- CIM_StorageAllocationSettingData.HostResourceBlockSize
- CIM_StorageAllocationSettingData.Reservation
- CIM_StorageAllocationSettingData.Limit
- CIM_StorageAllocationSettingData.HostExtentStartingAddress
- CIM_StorageAllocationSettingData.HostExtentName
- CIM_StorageAllocationSettingData.HostExtentNameFormat
- CIM_StorageAllocationSettingData.OtherHostExtentNameFormat
- CIM_StorageAllocationSettingData.HostExtentNameNamespace
- CIM_StorageAllocationSettingData.OtherHostExtentNameNamespace
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_StorageAllocationSettingData class

Represents settings for the allocation of virtual storage.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Core::Resource")]
class CIM_StorageAllocationSettingData : CIM_ResourceAllocationSettingData
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  uint16  ResourceType;
  string  OtherResourceType;
  string  ResourceSubType;
  string  PoolID;
  uint16  ConsumerVisibility;
  string  HostResource[];
  string  AllocationUnits;
  uint32  Weight;
  boolean AutomaticAllocation;
  boolean AutomaticDeallocation;
  string  Parent;
  string  Connection[];
  string  Address;
  uint16  MappingBehavior;
  string  AddressOnParent;
  uint64  VirtualResourceBlockSize;
  uint64  VirtualQuantity;
  string  VirtualQuantityUnits = "count(fixed size block)";
  uint16  Access;
  uint64  HostResourceBlockSize;
  uint64  Reservation;
  uint64  Limit;
  uint64  HostExtentStartingAddress;
  string  HostExtentName;
  uint16  HostExtentNameFormat;
  string  OtherHostExtentNameFormat;
  uint16  HostExtentNameNamespace;
  string  OtherHostExtentNameNamespace;
};
```

## Members

The **CIM\_StorageAllocationSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_StorageAllocationSettingData** class has these properties.

<dl> <dt>

**Access**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**Access**")
</dt> </dl>

The read/write support of the storage allocation.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>

**Readable** (1)


</dt> <dd></dd> <dt>

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>

**Writeable** (2)


</dt> <dd></dd> <dt>

<span id="Read_Write_Supported"></span><span id="read_write_supported"></span><span id="READ_WRITE_SUPPORTED"></span>

**Read/Write Supported** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 65535</dd> </dl>

</dd> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the resource, for example, the MAC address of a Ethernet port.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**AddressOnParent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of this resource from the context of the parent. This property is used to describe a controller relationship and the ordering of devices on a controller. For example, if the parent is a PCI Controller, this property would specify the PCI slot of this child device.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**Reservation**", "**CIM\_ResourceAllocationSettingData**.**Limit**"), **IsPUnit**
</dt> </dl>

The allocation units used by the **Reservation** and **Limit** properties.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**AutomaticAllocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to automatically allocate the resource; otherwise, **false**.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**AutomaticDeallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to automatically deallocate the resource; otherwise, **false**.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Connection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that indicates the objects connected to the resource, such as a named network or switch port.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**ConsumerVisibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The consumers visibility to the allocated resource.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Passed-Through"></span><span id="passed-through"></span><span id="PASSED-THROUGH"></span>

**Passed-Through** (2)


</dt> <dd></dd> <dt>

<span id="Virtualized"></span><span id="virtualized"></span><span id="VIRTUALIZED"></span>

**Virtualized** (3)


</dt> <dd></dd> <dt>

<span id="Not_represented"></span><span id="not_represented"></span><span id="NOT_REPRESENTED"></span>

**Not represented** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF reserved**


</dt> <dd>5 32766</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32767 65535</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for an instance of this class. In addition, the user-friendly name can be used as an index for a search or query. The name does not have to be unique within a namespace.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**HostExtentName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostExtentNameFormat**", "**CIM\_StorageAllocationSettingData**.**HostExtentNameNamespace**", "[**CIM\_StorageExtent**](cim-storageextent.md).**Name**")
</dt> </dl>

A unique identifier of the host storage extent.

</dd> <dt>

**HostExtentNameFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostExtentName**", "**CIM\_StorageAllocationSettingData**.**OtherHostExtentNameFormat**", "[**CIM\_StorageExtent**](cim-storageextent.md).**NameFormat**")
</dt> </dl>

The format that of the **HostExtentName** property value.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="SNVM"></span><span id="snvm"></span>

**SNVM** (7)


</dt> <dd></dd> <dt>

<span id="NAA"></span><span id="naa"></span>

**NAA** (9)


</dt> <dd></dd> <dt>

<span id="EUI64"></span><span id="eui64"></span>

**EUI64** (10)


</dt> <dd></dd> <dt>

<span id="T10VID"></span><span id="t10vid"></span>

**T10VID** (11)


</dt> <dd></dd> <dt>

<span id="OS_Device_Name"></span><span id="os_device_name"></span><span id="OS_DEVICE_NAME"></span>

**OS Device Name** (12)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>13 65535</dd> </dl>

</dd> <dt>

**HostExtentNameNamespace**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostExtentName**", "**CIM\_StorageAllocationSettingData**.**OtherHostExtentNameNamespace**", "**CIM\_StorageAllocationSettingData**.**HostExtentNameFormat**", "[**CIM\_StorageExtent**](cim-storageextent.md).**Namespace**")
</dt> </dl>

The naming format for the **Name** property.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="VPD83Type3"></span><span id="vpd83type3"></span><span id="VPD83TYPE3"></span>

**VPD83Type3** (2)


</dt> <dd></dd> <dt>

<span id="VPD83Type2"></span><span id="vpd83type2"></span><span id="VPD83TYPE2"></span>

**VPD83Type2** (3)


</dt> <dd></dd> <dt>

<span id="VPD83Type1"></span><span id="vpd83type1"></span><span id="VPD83TYPE1"></span>

**VPD83Type1** (4)


</dt> <dd></dd> <dt>

<span id="VPD80"></span><span id="vpd80"></span>

**VPD80** (5)


</dt> <dd></dd> <dt>

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>

**NodeWWN** (6)


</dt> <dd></dd> <dt>

<span id="SNVM"></span><span id="snvm"></span>

**SNVM** (7)


</dt> <dd></dd> <dt>

<span id="OS_Device_Namespace"></span><span id="os_device_namespace"></span><span id="OS_DEVICE_NAMESPACE"></span>

**OS Device Namespace** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9 65535</dd> </dl>

</dd> <dt>

**HostExtentStartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostResourceBlockSize**", "[**CIM\_BasedOn**](cim-basedon.md).**StartingAddress**")
</dt> </dl>

The starting address on the host storage extent. A NULL val;ue indicates that there is no direct mapping between the virtual storage extent and the host storage extent.

</dd> <dt>

**HostResource**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**ConsumerVisibility**", "**CIM\_ResourceAllocationSettingData**.**MappingBehavior**")
</dt> </dl>

An array that contains the assignment of the allocated resources. Each non-null value of this property must be formated as an RFC3986 based URI. If the resource is modeled, then the value should be a WBEM URI.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**HostResourceBlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**BlockSize**"), **PUnit** ("byte")
</dt> </dl>

The size, in bytes, of the blocks that are allocated on the host for the storage allocation. If the block size is variable, then the maximum block size in bytes should be specified. If the block size is unknown or if a block concept does not apply, then the value "1" (unknown) should be used.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> -   *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID** property, or be a registered ID that is assigned by a recognized global authority.
> -   *OrgID* must not contain a colon. The first colon in **InstanceID** must be between the *OrgID* and*LocalID*.
> -   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
> -   If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
> -   For DMTF defined instances, the pattern must be used with the *OrgID* set to "CIM".

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Limit"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostResourceBlockSize**")
</dt> </dl>

The maximum amount of blocks that will be granted for the storage resource allocation on the host. The block size is specified by the **HostResourceBlockSize** property.

</dd> <dt>

**MappingBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the resource maps to underlying resources.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

**Not Supported** (2)


</dt> <dd></dd> <dt>

<span id="Dedicated"></span><span id="dedicated"></span><span id="DEDICATED"></span>

**Dedicated** (3)


</dt> <dd></dd> <dt>

<span id="Soft_Affinity"></span><span id="soft_affinity"></span><span id="SOFT_AFFINITY"></span>

**Soft Affinity** (4)


</dt> <dd></dd> <dt>

<span id="Hard_Affinity"></span><span id="hard_affinity"></span><span id="HARD_AFFINITY"></span>

**Hard Affinity** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32766</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32767 65535</dd> </dl>

</dd> <dt>

**OtherHostExtentNameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostExtentNameFormat**")
</dt> </dl>

The format of the **HostExtentName** property if the property is set to "1" (other).

</dd> <dt>

**OtherHostExtentNameNamespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostExtentNameNamespace**")
</dt> </dl>

A string that describes the namespace of the **HostExtentName** property if the value of the **HostExtentNameNamespace** property is "1" (other).

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**ResourceType**")
</dt> </dl>

A description of the resource type when the **ResourceType** property is set to 1 (other).

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent of the resource, for example, a controller for the current allocation.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourcePool**](cim-resourcepool.md).**PoolId**")
</dt> </dl>

The ID of the resource pool that generated the resource.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Reservation"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**HostResourceBlockSize**")
</dt> </dl>

The amount of blocks that are guaranteed to be available for the storage resource allocation on the host. The block size is specified by the **HostResourceBlockSize** property.

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**ResourceType**")
</dt> </dl>

An implementation specific sub-type for this resource. For example, this may be used to distinguish different models of the same resource type.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**OtherResourceType**", "**CIM\_ResourceAllocationSettingData**.**ResourceSubType**")
</dt> </dl>

The type of resource that is represented by the allocation settings.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Computer_System"></span><span id="computer_system"></span><span id="COMPUTER_SYSTEM"></span>

**Computer System** (2)


</dt> <dd></dd> <dt>

<span id="Processor"></span><span id="processor"></span><span id="PROCESSOR"></span>

**Processor** (3)


</dt> <dd></dd> <dt>

<span id="Memory"></span><span id="memory"></span><span id="MEMORY"></span>

**Memory** (4)


</dt> <dd></dd> <dt>

<span id="IDE_Controller"></span><span id="ide_controller"></span><span id="IDE_CONTROLLER"></span>

**IDE Controller** (5)


</dt> <dd></dd> <dt>

<span id="Parallel_SCSI_HBA"></span><span id="parallel_scsi_hba"></span><span id="PARALLEL_SCSI_HBA"></span>

**Parallel SCSI HBA** (6)


</dt> <dd></dd> <dt>

<span id="FC_HBA"></span><span id="fc_hba"></span>

**FC HBA** (7)


</dt> <dd></dd> <dt>

<span id="iSCSI_HBA"></span><span id="iscsi_hba"></span><span id="ISCSI_HBA"></span>

**iSCSI HBA** (8)


</dt> <dd></dd> <dt>

<span id="IB_HCA"></span><span id="ib_hca"></span>

**IB HCA** (9)


</dt> <dd></dd> <dt>

<span id="Ethernet_Adapter"></span><span id="ethernet_adapter"></span><span id="ETHERNET_ADAPTER"></span>

**Ethernet Adapter** (10)


</dt> <dd></dd> <dt>

<span id="Other_Network_Adapter"></span><span id="other_network_adapter"></span><span id="OTHER_NETWORK_ADAPTER"></span>

**Other Network Adapter** (11)


</dt> <dd></dd> <dt>

<span id="I_O_Slot"></span><span id="i_o_slot"></span><span id="I_O_SLOT"></span>

**I/O Slot** (12)


</dt> <dd></dd> <dt>

<span id="I_O_Device"></span><span id="i_o_device"></span><span id="I_O_DEVICE"></span>

**I/O Device** (13)


</dt> <dd></dd> <dt>

<span id="Floppy_Drive"></span><span id="floppy_drive"></span><span id="FLOPPY_DRIVE"></span>

**Floppy Drive** (14)


</dt> <dd></dd> <dt>

<span id="CD_Drive"></span><span id="cd_drive"></span><span id="CD_DRIVE"></span>

**CD Drive** (15)


</dt> <dd></dd> <dt>

<span id="DVD_drive"></span><span id="dvd_drive"></span><span id="DVD_DRIVE"></span>

**DVD drive** (16)


</dt> <dd></dd> <dt>

<span id="Disk_Drive"></span><span id="disk_drive"></span><span id="DISK_DRIVE"></span>

**Disk Drive** (17)


</dt> <dd></dd> <dt>

<span id="Tape_Drive"></span><span id="tape_drive"></span><span id="TAPE_DRIVE"></span>

**Tape Drive** (18)


</dt> <dd></dd> <dt>

<span id="Storage_Extent"></span><span id="storage_extent"></span><span id="STORAGE_EXTENT"></span>

**Storage Extent** (19)


</dt> <dd></dd> <dt>

<span id="Other_storage_device"></span><span id="other_storage_device"></span><span id="OTHER_STORAGE_DEVICE"></span>

**Other storage device** (20)


</dt> <dd></dd> <dt>

<span id="Serial_port"></span><span id="serial_port"></span><span id="SERIAL_PORT"></span>

**Serial port** (21)


</dt> <dd></dd> <dt>

<span id="Parallel_port"></span><span id="parallel_port"></span><span id="PARALLEL_PORT"></span>

**Parallel port** (22)


</dt> <dd></dd> <dt>

<span id="USB_Controller"></span><span id="usb_controller"></span><span id="USB_CONTROLLER"></span>

**USB Controller** (23)


</dt> <dd></dd> <dt>

<span id="Graphics_controller"></span><span id="graphics_controller"></span><span id="GRAPHICS_CONTROLLER"></span>

**Graphics controller** (24)


</dt> <dd></dd> <dt>

<span id="IEEE_1394_Controller"></span><span id="ieee_1394_controller"></span><span id="IEEE_1394_CONTROLLER"></span>

**IEEE 1394 Controller** (25)


</dt> <dd></dd> <dt>

<span id="Partitionable_Unit"></span><span id="partitionable_unit"></span><span id="PARTITIONABLE_UNIT"></span>

**Partitionable Unit** (26)


</dt> <dd></dd> <dt>

<span id="Base_Partitionable_Unit"></span><span id="base_partitionable_unit"></span><span id="BASE_PARTITIONABLE_UNIT"></span>

**Base Partitionable Unit** (27)


</dt> <dd></dd> <dt>

<span id="Power"></span><span id="power"></span><span id="POWER"></span>

**Power** (28)


</dt> <dd></dd> <dt>

<span id="Cooling_Capacity"></span><span id="cooling_capacity"></span><span id="COOLING_CAPACITY"></span>

**Cooling Capacity** (29)


</dt> <dd></dd> <dt>

<span id="Ethernet_Switch_Port"></span><span id="ethernet_switch_port"></span><span id="ETHERNET_SWITCH_PORT"></span>

**Ethernet Switch Port** (30)


</dt> <dd></dd> <dt>

<span id="Logical_Disk"></span><span id="logical_disk"></span><span id="LOGICAL_DISK"></span>

**Logical Disk** (31)


</dt> <dd></dd> <dt>

<span id="Storage_Volume"></span><span id="storage_volume"></span><span id="STORAGE_VOLUME"></span>

**Storage Volume** (32)


</dt> <dd></dd> <dt>

<span id="Ethernet_Connection"></span><span id="ethernet_connection"></span><span id="ETHERNET_CONNECTION"></span>

**Ethernet Connection** (33)


</dt> <dd></dd> <dt>

<span id="DMTF_reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF reserved**


</dt> <dd>34 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 35535</dd> </dl>

</dd> <dt>

**VirtualQuantity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("VirtualQuantity"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**NumberOfBlocks**", "**CIM\_StorageAllocationSettingData**.**VirtualQuantityUnits**")
</dt> </dl>

The number of blocks that the storage allocation presents to the consumer.

> [!Note]  
> The **VirtualQuantity** property can specify a block size of "1", even if **VirtualResourceBlockSize** is unknown.

 

</dd> <dt>

**VirtualQuantityUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("VirtualQuantityUnits"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_StorageAllocationSettingData**.**VirtualQuantity**"), **IsPUnit**
</dt> </dl>

The units used by the **VirtualQuantity** property. This value shall should be set to "count(fixed size block)" or "byte". The default value, "count(fixed size block)" should be used for a fixed block size, and "byte" should be used for an unknown or variable block size.

</dd> <dt>

**VirtualResourceBlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**BlockSize**"), **PUnit** ("byte")
</dt> </dl>

The size, in bytes, of the blocks that form the storage allocation request. If the block size is variable, then the maximum block size should be specified. If the block size is unknown or if a block concept does not apply, then the block size should be "1" (unknown).

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative priority for this allocation in relation to other allocations from the same resource pool.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





