---
description: Represents the configured state of the guest service interface component.
ms.assetid: 82B58459-9819-4F51-BEE5-AB57E444CF55
title: Msvm_GuestServiceInterfaceComponentSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_GuestServiceInterfaceComponentSettingData
- Msvm_GuestServiceInterfaceComponentSettingData.ElementName
- Msvm_GuestServiceInterfaceComponentSettingData.InstanceID
- Msvm_GuestServiceInterfaceComponentSettingData.ResourceType
- Msvm_GuestServiceInterfaceComponentSettingData.OtherResourceType
- Msvm_GuestServiceInterfaceComponentSettingData.ResourceSubType
- Msvm_GuestServiceInterfaceComponentSettingData.PoolID
- Msvm_GuestServiceInterfaceComponentSettingData.ConsumerVisibility
- Msvm_GuestServiceInterfaceComponentSettingData.HostResource
- Msvm_GuestServiceInterfaceComponentSettingData.AllocationUnits
- Msvm_GuestServiceInterfaceComponentSettingData.VirtualQuantity
- Msvm_GuestServiceInterfaceComponentSettingData.Reservation
- Msvm_GuestServiceInterfaceComponentSettingData.Limit
- Msvm_GuestServiceInterfaceComponentSettingData.Weight
- Msvm_GuestServiceInterfaceComponentSettingData.AutomaticAllocation
- Msvm_GuestServiceInterfaceComponentSettingData.AutomaticDeallocation
- Msvm_GuestServiceInterfaceComponentSettingData.Parent
- Msvm_GuestServiceInterfaceComponentSettingData.Connection
- Msvm_GuestServiceInterfaceComponentSettingData.Address
- Msvm_GuestServiceInterfaceComponentSettingData.MappingBehavior
- Msvm_GuestServiceInterfaceComponentSettingData.EnabledState
- Msvm_GuestServiceInterfaceComponentSettingData.DefaultEnabledStatePolicy
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_GuestServiceInterfaceComponentSettingData class

Represents the configured state of the guest service interface component. This class derives from the [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_GuestServiceInterfaceComponentSettingData : CIM_ResourceAllocationSettingData
{
  string  ElementName;
  string  InstanceID;
  uint16  ResourceType;
  string  OtherResourceType;
  string  ResourceSubType;
  string  PoolID;
  uint16  ConsumerVisibility;
  string  HostResource[];
  string  AllocationUnits;
  uint64  VirtualQuantity;
  uint64  Reservation;
  uint64  Limit;
  uint32  Weight;
  boolean AutomaticAllocation;
  boolean AutomaticDeallocation;
  string  Parent;
  string  Connection[];
  string  Address;
  uint16  MappingBehavior;
  uint16  EnabledState = 3;
  uint16  DefaultEnabledStatePolicy = 2;
};
```

## Members

The **Msvm\_GuestServiceInterfaceComponentSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_GuestServiceInterfaceComponentSettingData** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the resource. For example, the MAC address of a Ethernet port.

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the units of allocation used by the Reservation and Limit properties. For example, when ResourceType=Processor, AllocationUnits may be set to MHz. When ResourceType=Memory, AllocationUnits may be set to MB

</dd> <dt>

**AutomaticAllocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies if the resource will be automatically allocated. For example when set to true, when the consuming virtual computer system is powered on, this resource would be allocated. A value of false indicates the resource must be explicitly allocated. For example, the setting may represent removable media (that is, cdrom or floppy) where at power on time, the media is not present. An explicit operation is required to allocate the resource.

</dd> <dt>

**AutomaticDeallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies if the resource will be automatically deallocated. For example, when set to true, when the consuming virtual computer system is powered off, this resource would be deallocated. When set to false, the resource will remain allocated and must be explicitly deallocated.

</dd> <dt>

**Connection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The thing to which this resource is connected. For example, a named network or switch port.

</dd> <dt>

**ConsumerVisibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the consumers visibility to the allocated resource.



| Value                                                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                            | Unknown.<br/>                                                                                                                                                                                                                                         |
| <span id="Passed-Through"></span><span id="passed-through"></span><span id="PASSED-THROUGH"></span><dl> <dt>**Passed-Through**</dt> <dt>2</dt> </dl>                | The underlying or host resource is utilized and passed through to the consumer, possibly using partitioning. At least one item shall be present in the DeviceID property.<br/>                                                                        |
| <span id="Virtualized"></span><span id="virtualized"></span><span id="VIRTUALIZED"></span><dl> <dt>**Virtualized**</dt> <dt>3</dt> </dl>                            | The resource is virtualized and may not map directly to an underlying/host resource. Some implementations may support specific assignment for virtualized resources, in which case the host resource(s) are exposed using the DeviceID property.<br/> |
| <span id="Not_represented"></span><span id="not_represented"></span><span id="NOT_REPRESENTED"></span><dl> <dt>**Not represented**</dt> <dt>4</dt> </dl>            | A representation of the resource does not exist within the context of the resource consumer.<br/>                                                                                                                                                     |
| <span id="DMTF_reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF reserved**</dt> <dt>..</dt> </dl>                   |                                                                                                                                                                                                                                                             |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32767..65535</dt> </dl> |                                                                                                                                                                                                                                                             |



 

</dd> <dt>

**DefaultEnabledStatePolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled and disabled states of guest communication services by default.

This is a read-only property, but it can be changed using the [**ModifyResourceSettings**](cim-virtualsystemmanagementservice-modifyresourcesettings.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

> [!Note]  
> Added in Windows 10.

 

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The display name for this instance of SettingData. In addition, the display name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled and disabled states of an element.

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](/previous-versions/windows/desktop/virtual/modifyvirtualsystemresources-msvm-virtualsystemmanagementservice) method (or [**ModifyResourceSettings**](cim-virtualsystemmanagementservice-modifyresourcesettings.md) in Windows 10 or later) of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

Valid values are:

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**HostResource**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property exposes specific assignment to host or underlying resources. The embedded instances shall contain only key properties and be treated as Object Paths. If the virtual resource may be scheduled on a number of underlying resources, this property should remain **NULL**. In that case, the DeviceAllocatedFromPool or ResourceAllocationFromPool associations may be used to determine the pool of host resources on which this virtual resource may be scheduled. If specific assignment is utilized, all underlying resources used by this virtual resource shall be listed in this array. Typically, the array will contain one item, however for aggregate allocations, such as multiple processors, multiple host resources may be specified.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: *OrgID*:*LocalID* Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the *SchemaName*\_*ClassName* structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. For DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to CIM.

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the upper bound, or maximum amount of resource that will be granted for this allocation. For example, a system which supports memory paging may support setting the Limit of a Memory allocation below that of the VirtualQuantity, thus forcing paging to occur for this allocation.

</dd> <dt>

**MappingBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies how this resource maps to underlying resources. If the HostResource array contains any entries, this property reflects how the resource maps to those specific resources.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>**Not Supported** (1)
</dt> <dt>

<span id="Dedicated"></span><span id="dedicated"></span><span id="DEDICATED"></span>**Dedicated** (2)
</dt> <dt>

<span id="Soft_Affinity"></span><span id="soft_affinity"></span><span id="SOFT_AFFINITY"></span>**Soft Affinity** (3)
</dt> <dt>

<span id="Hard_Affinity"></span><span id="hard_affinity"></span><span id="HARD_AFFINITY"></span>**Hard Affinity** (4)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32767..65535)
</dt> </dl>

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the resource type when a well defined value is not available and ResourceType has the value "Other".

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Parent of the resource. For example, a controller for the current allocation.

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies which ResourcePool the resource is currently allocated from, or which ResourcePool the resource will be allocated from when the allocation occurs.

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the amount of resource guaranteed to be available for this allocation. On system which support over-commitment of resources, this value is typically used for admission control to prevent an an allocation from being accepted thus preventing resource depletion.

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string describing an implementation specific sub-type for this resource. For example, this may be used to distinguish different models of the same resource type.

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of resource this allocation setting represents.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Computer_System"></span><span id="computer_system"></span><span id="COMPUTER_SYSTEM"></span>**Computer System** (2)
</dt> <dt>

<span id="Processor"></span><span id="processor"></span><span id="PROCESSOR"></span>**Processor** (3)
</dt> <dt>

<span id="Memory"></span><span id="memory"></span><span id="MEMORY"></span>**Memory** (4)
</dt> <dt>

<span id="IDE_Controller"></span><span id="ide_controller"></span><span id="IDE_CONTROLLER"></span>**IDE Controller** (5)
</dt> <dt>

<span id="Parallel_SCSI_HBA"></span><span id="parallel_scsi_hba"></span><span id="PARALLEL_SCSI_HBA"></span>**Parallel SCSI HBA** (6)
</dt> <dt>

<span id="FC_HBA"></span><span id="fc_hba"></span>**FC HBA** (7)
</dt> <dt>

<span id="iSCSI_HBA"></span><span id="iscsi_hba"></span><span id="ISCSI_HBA"></span>**iSCSI HBA** (8)
</dt> <dt>

<span id="IB_HCA"></span><span id="ib_hca"></span>**IB HCA** (9)
</dt> <dt>

<span id="Ethernet_Adapter"></span><span id="ethernet_adapter"></span><span id="ETHERNET_ADAPTER"></span>**Ethernet Adapter** (10)
</dt> <dt>

<span id="Other_Network_Adapter"></span><span id="other_network_adapter"></span><span id="OTHER_NETWORK_ADAPTER"></span>**Other Network Adapter** (11)
</dt> <dt>

<span id="I_O_Slot"></span><span id="i_o_slot"></span><span id="I_O_SLOT"></span>**I/O Slot** (12)
</dt> <dt>

<span id="I_O_Device"></span><span id="i_o_device"></span><span id="I_O_DEVICE"></span>**I/O Device** (13)
</dt> <dt>

<span id="Floppy_Drive"></span><span id="floppy_drive"></span><span id="FLOPPY_DRIVE"></span>**Floppy Drive** (14)
</dt> <dt>

<span id="CD_Drive"></span><span id="cd_drive"></span><span id="CD_DRIVE"></span>**CD Drive** (15)
</dt> <dt>

<span id="DVD_drive"></span><span id="dvd_drive"></span><span id="DVD_DRIVE"></span>**DVD drive** (16)
</dt> <dt>

<span id="Serial_port"></span><span id="serial_port"></span><span id="SERIAL_PORT"></span>**Serial port** (17)
</dt> <dt>

<span id="Parallel_port"></span><span id="parallel_port"></span><span id="PARALLEL_PORT"></span>**Parallel port** (18)
</dt> <dt>

<span id="USB_Controller"></span><span id="usb_controller"></span><span id="USB_CONTROLLER"></span>**USB Controller** (19)
</dt> <dt>

<span id="Graphics_controller"></span><span id="graphics_controller"></span><span id="GRAPHICS_CONTROLLER"></span>**Graphics controller** (20)
</dt> <dt>

<span id="Storage_Extent"></span><span id="storage_extent"></span><span id="STORAGE_EXTENT"></span>**Storage Extent** (21)
</dt> <dt>

<span id="Disk"></span><span id="disk"></span><span id="DISK"></span>**Disk** (22)
</dt> <dt>

<span id="Tape"></span><span id="tape"></span><span id="TAPE"></span>**Tape** (23)
</dt> <dt>

<span id="Other_storage_device"></span><span id="other_storage_device"></span><span id="OTHER_STORAGE_DEVICE"></span>**Other storage device** (24)
</dt> <dt>

<span id="Firewire_Controller"></span><span id="firewire_controller"></span><span id="FIREWIRE_CONTROLLER"></span>**Firewire Controller** (25)
</dt> <dt>

<span id="Partitionable_Unit"></span><span id="partitionable_unit"></span><span id="PARTITIONABLE_UNIT"></span>**Partitionable Unit** (26)
</dt> <dt>

<span id="Base_Partitionable_Unit"></span><span id="base_partitionable_unit"></span><span id="BASE_PARTITIONABLE_UNIT"></span>**Base Partitionable Unit** (27)
</dt> <dt>

<span id="Power_Supply"></span><span id="power_supply"></span><span id="POWER_SUPPLY"></span>**Power Supply** (28)
</dt> <dt>

<span id="Cooling_Device"></span><span id="cooling_device"></span><span id="COOLING_DEVICE"></span>**Cooling Device** (29)
</dt> <dt>

<span id="DMTF_reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32767..65535)
</dt> </dl>

</dd> <dt>

**VirtualQuantity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the quantity of resources presented to the consumer. For example, when ResourceType=Processor, this property would reflect the number of discrete Processors presented to the virtual computer system. When ResourceType=Memory, this property could reflect the number of MB reported to the virtual computer system.

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies a relative priority for this allocation in relation to other allocations from the same ResourcePool. This property has no unit of measure, and is only relevant when compared to other allocations competing for the same host resources.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dt>

[**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata)
</dt> </dl>

 

