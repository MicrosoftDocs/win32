---
title: Msvm\_HeartbeatComponentSettingData class
description: Represents the configured state of the heartbeat service.
ms.assetid: 08867111-aba9-4260-90c5-4286f1ca33da
keywords:
- Msvm_HeartbeatComponentSettingData class Hyper-V
- Msvm_HeartbeatComponentSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_HeartbeatComponentSettingData
- Msvm_HeartbeatComponentSettingData.Caption
- Msvm_HeartbeatComponentSettingData.Description
- Msvm_HeartbeatComponentSettingData.InstanceID
- Msvm_HeartbeatComponentSettingData.ElementName
- Msvm_HeartbeatComponentSettingData.ResourceType
- Msvm_HeartbeatComponentSettingData.OtherResourceType
- Msvm_HeartbeatComponentSettingData.ResourceSubType
- Msvm_HeartbeatComponentSettingData.PoolID
- Msvm_HeartbeatComponentSettingData.ConsumerVisibility
- Msvm_HeartbeatComponentSettingData.HostResource
- Msvm_HeartbeatComponentSettingData.AllocationUnits
- Msvm_HeartbeatComponentSettingData.VirtualQuantity
- Msvm_HeartbeatComponentSettingData.Reservation
- Msvm_HeartbeatComponentSettingData.Limit
- Msvm_HeartbeatComponentSettingData.Weight
- Msvm_HeartbeatComponentSettingData.AutomaticAllocation
- Msvm_HeartbeatComponentSettingData.AutomaticDeallocation
- Msvm_HeartbeatComponentSettingData.Parent
- Msvm_HeartbeatComponentSettingData.Connection
- Msvm_HeartbeatComponentSettingData.Address
- Msvm_HeartbeatComponentSettingData.MappingBehavior
- Msvm_HeartbeatComponentSettingData.EnabledState
- Msvm_HeartbeatComponentSettingData.Interval
- Msvm_HeartbeatComponentSettingData.Latency
- Msvm_HeartbeatComponentSettingData.ErrorThreshold
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_HeartbeatComponentSettingData class

Represents the configured state of the heartbeat service.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_HeartbeatComponentSettingData : CIM_ResourceAllocationSettingData
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
  uint16  EnabledState = 2;
  uint32  Interval = 2000;
  uint32  Latency = 1000;
  uint32  ErrorThreshold = 2;
};
```

## Members

The **Msvm\_HeartbeatComponentSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_HeartbeatComponentSettingData** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the resource, for example, the MAC address of a Ethernet port.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
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

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled and disabled states of an element.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An administrator's startup configuration for the enabled state of an element. This property is always set to 2 (Enabled).

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**HostResource**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **HyperVEmbeddedInstance** ("CIM\_LogicalDevice")
</dt> </dl>

An array that contains the assignment of the allocated resources. Each non-null value of this property must be formated as an RFC3986 based URI. If the resource is modeled, then the value should be a WBEM URI.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

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

**Interval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interval between ping attempts, in milliseconds. This is always set to 2000.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Latency**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum expected latency between a request ping and a response, in milliseconds, before a given request is considered dropped. This property is always set to 1000.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount of resource to grant to the allocation. The unit type of this property is specified by the **AllocationUnits** property.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

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

**Not Supported** (1)


</dt> <dd></dd> <dt>

<span id="Dedicated"></span><span id="dedicated"></span><span id="DEDICATED"></span>

**Dedicated** (2)


</dt> <dd></dd> <dt>

<span id="Soft_Affinity"></span><span id="soft_affinity"></span><span id="SOFT_AFFINITY"></span>

**Soft Affinity** (3)


</dt> <dd></dd> <dt>

<span id="Hard_Affinity"></span><span id="hard_affinity"></span><span id="HARD_AFFINITY"></span>

**Hard Affinity** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32766</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32767 65535</dd> </dl>

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
</dt> </dl>

The number of resource that are guaranteed to be available for this allocation. On systems that support over-commitment of resources, this value is typically used for admission control.

The unit type of this property is specified by the **AllocationUnits** property.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
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

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**OtherResourceType**")
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

<span id="I_O_Device"></span><span id="i_o_device"></span><span id="I_O_DEVICE"></span>

**I/O Device** (12)


</dt> <dd></dd> <dt>

<span id="Floppy_Drive"></span><span id="floppy_drive"></span><span id="FLOPPY_DRIVE"></span>

**Floppy Drive** (13)


</dt> <dd></dd> <dt>

<span id="CD_Drive"></span><span id="cd_drive"></span><span id="CD_DRIVE"></span>

**CD Drive** (14)


</dt> <dd></dd> <dt>

<span id="DVD_drive"></span><span id="dvd_drive"></span><span id="DVD_DRIVE"></span>

**DVD drive** (15)


</dt> <dd></dd> <dt>

<span id="Serial_port"></span><span id="serial_port"></span><span id="SERIAL_PORT"></span>

**Serial port** (16)


</dt> <dd></dd> <dt>

<span id="Parallel_port"></span><span id="parallel_port"></span><span id="PARALLEL_PORT"></span>

**Parallel port** (17)


</dt> <dd></dd> <dt>

<span id="USB_Controller"></span><span id="usb_controller"></span><span id="USB_CONTROLLER"></span>

**USB Controller** (18)


</dt> <dd></dd> <dt>

<span id="Graphics_controller"></span><span id="graphics_controller"></span><span id="GRAPHICS_CONTROLLER"></span>

**Graphics controller** (19)


</dt> <dd></dd> <dt>

<span id="Storage_Extent"></span><span id="storage_extent"></span><span id="STORAGE_EXTENT"></span>

**Storage Extent** (20)


</dt> <dd></dd> <dt>

<span id="Disk"></span><span id="disk"></span><span id="DISK"></span>

**Disk** (21)


</dt> <dd></dd> <dt>

<span id="Tape"></span><span id="tape"></span><span id="TAPE"></span>

**Tape** (22)


</dt> <dd></dd> <dt>

<span id="Other_storage_device"></span><span id="other_storage_device"></span><span id="OTHER_STORAGE_DEVICE"></span>

**Other storage device** (23)


</dt> <dd></dd> <dt>

<span id="Firewire_Controller"></span><span id="firewire_controller"></span><span id="FIREWIRE_CONTROLLER"></span>

**Firewire Controller** (24)


</dt> <dd></dd> <dt>

<span id="Partitionable_Unit"></span><span id="partitionable_unit"></span><span id="PARTITIONABLE_UNIT"></span>

**Partitionable Unit** (25)


</dt> <dd></dd> <dt>

<span id="Base_Partitionable_Unit"></span><span id="base_partitionable_unit"></span><span id="BASE_PARTITIONABLE_UNIT"></span>

**Base Partitionable Unit** (26)


</dt> <dd></dd> <dt>

<span id="Power_Supply"></span><span id="power_supply"></span><span id="POWER_SUPPLY"></span>

**Power Supply** (27)


</dt> <dd></dd> <dt>

<span id="Cooling_Device"></span><span id="cooling_device"></span><span id="COOLING_DEVICE"></span>

**Cooling Device** (28)


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
</dt> </dl>

The number of resources presented to the consumer of the resource.

This property is inherited from [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).

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

## Remarks

Access to the **Msvm\_HeartbeatComponentSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dt>

[**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214)
</dt> <dt>

[**Msvm\_HeartbeatComponentSettingData (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850158)
</dt> <dt>

[Integration Services Classes](integration-components-classes.md)
</dt> </dl>

 

 





