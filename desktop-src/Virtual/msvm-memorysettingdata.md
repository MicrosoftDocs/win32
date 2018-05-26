---
title: Msvm\_MemorySettingData class
description: Represents the configured state of the memory for a virtual system.
ms.assetid: aba388d5-4378-4134-b45e-1883c64f826e
keywords:
- Msvm_MemorySettingData class Hyper-V
- Msvm_MemorySettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_MemorySettingData
- Msvm_MemorySettingData.Caption
- Msvm_MemorySettingData.Description
- Msvm_MemorySettingData.InstanceID
- Msvm_MemorySettingData.ElementName
- Msvm_MemorySettingData.ResourceType
- Msvm_MemorySettingData.OtherResourceType
- Msvm_MemorySettingData.ResourceSubType
- Msvm_MemorySettingData.PoolID
- Msvm_MemorySettingData.ConsumerVisibility
- Msvm_MemorySettingData.HostResource
- Msvm_MemorySettingData.AllocationUnits
- Msvm_MemorySettingData.Reservation
- Msvm_MemorySettingData.Limit
- Msvm_MemorySettingData.Weight
- Msvm_MemorySettingData.MappingBehavior
- Msvm_MemorySettingData.VirtualQuantity
- Msvm_MemorySettingData.AutomaticAllocation
- Msvm_MemorySettingData.AutomaticDeallocation
- Msvm_MemorySettingData.Parent
- Msvm_MemorySettingData.Connection
- Msvm_MemorySettingData.Address
- Msvm_MemorySettingData.IsVirtualized
- Msvm_MemorySettingData.DeviceID
- Msvm_MemorySettingData.DeviceIDFormat
- Msvm_MemorySettingData.DynamicMemoryEnabled
- Msvm_MemorySettingData.TargetMemoryBuffer
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

# Msvm\_MemorySettingData class

Represents the configured state of the memory for a virtual system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MemorySettingData : CIM_ResourceAllocationSettingData
{
  string  Caption = "Memory";
  string  Description = "Settings for Microsoft Virtual Machine Memory";
  string  InstanceID;
  string  ElementName = "Memory";
  uint16  ResourceType = 4;
  string  OtherResourceType;
  string  ResourceSubType = "Microsoft Virtual Machine Memory";
  string  PoolID;
  uint16  ConsumerVisibility;
  string  HostResource[];
  string  AllocationUnits = "MB";
  uint64  Reservation;
  uint64  Limit;
  uint32  Weight;
  uint16  MappingBehavior;
  uint64  VirtualQuantity;
  boolean AutomaticAllocation = True;
  boolean AutomaticDeallocation = True;
  string  Parent;
  string  Connection[];
  string  Address;
  boolean IsVirtualized = True;
  string  DeviceID = "Microsoft:GUID";
  string  DeviceIDFormat;
  boolean DynamicMemoryEnabled;
  uint32  TargetMemoryBuffer;
};
```

## Members

The **Msvm\_MemorySettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MemorySettingData** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the resource. For example, the MAC address of an Ethernet port. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of allocation used by the **Reservation** and **Limit** properties. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to "MB".

</dd> <dt>

**AutomaticAllocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically allocated. For example when set to **True**, when the consuming virtual computer system is powered on, this resource would be allocated. A value of **False** indicates the resource must be explicitly allocated. For example, the setting may represent removable media (such as a CD-ROM or a floppy) where at power on time, the media is not present. An explicit operation is required to allocate the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **True**.

</dd> <dt>

**AutomaticDeallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically allocated. For example when this property is set to **True**, when the consuming virtual computer system is powered on, this resource would be allocated. When this property is **False**, the resource must be explicitly allocated. For example, the setting may represent removable media (such as a CD-ROM or a floppy) where at power on time, the media is not present. An explicit operation is required to allocate the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **True**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Memory".

</dd> <dt>

**Connection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device to which this resource is connected. For example, a named network or switch port. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**ConsumerVisibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the consumers visibility to the allocated resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Settings for Microsoft Virtual Machine Memory".

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address or other identifying information to uniquely name the logical device. This property is always set to "Microsoft:*GUID*".

</dd> <dt>

**DeviceIDFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The format of the corresponding **DeviceID** property, or the supported device IDs when used to represent a capability. This property is not used.

</dd> <dt>

**DynamicMemoryEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether dynamic memory is enabled for the virtual machine.

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

**Windows Server 2008 R2:** Reserved for future use. Note that this behavior has changed with Windows Server 2008 R2 with SP1.

**Windows Server 2008:** The **DynamicMemoryEnabled** property is not available.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) and it is set to "Memory". Changing this property will change the element name of the associated logical device derivative.

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**HostResource**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **HyperVEmbeddedInstance** ("CIM\_LogicalDevice")
</dt> </dl>

This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

For instances associated with a virtual system, this defaults to "Microsoft:*GUID*\\*device-specific data*". For instances which define potential settings for a virtual system, this defaults to "Microsoft:Definition\\*GUID*\\*Type*", where *Type* is "Maximum", "Minimum", "Default", or "Increment". This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**IsVirtualized**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this device is virtualized or passed through. When set to **False**, the underlying or host resource is utilized. At least one item shall be present in the **DeviceID** property. When set to **True**, the resource is virtualized and may not map directly to an underlying/host resource. Some implementations may support specific assignment for virtualized resources, in which case the host resource(s) are exposed using the **DeviceID** property. This property is always set to **True**.

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount of memory that may be consumed by the virtual system. For a virtual system with dynamic memory enabled, this represents the maximum memory setting. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**MappingBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies how this resource maps to underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**ResourceType**")
</dt> </dl>

A string that describes the resource type when a well-defined value is not available and **ResourceType** has the value "Other". This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent of the resource. For example, a controller for the current allocation. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourcePool**](cim-resourcepool.md).**PoolId**")
</dt> </dl>

The identifier of the resource pool from which this resource was allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the amount of memory guaranteed to be available for this VM. For a virtual system with dynamic memory enabled, this represents the minimum memory setting. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific sub-type for this resource. For example, this may be used to distinguish different models of the same resource type. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to "Microsoft Virtual Machine Memory".

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**OtherResourceType**")
</dt> </dl>

The type of resource that this allocation setting represents. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to 4 (Memory).

</dd> <dt>

**TargetMemoryBuffer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the amount of extra memory that should be reserved for a virtual machine at runtime, as a percentage of the total memory that the virtual machine is thought to need. This only applies to virtual systems with dynamic memory enabled.

This property can be in the range of 5 to 2000.

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not supported. Note that this behavior has changed with Windows Server 2008 R2 with SP1.

</dd> <dt>

**VirtualQuantity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total amount of RAM in the virtual system, as seen by the guest operating system. For a virtual system with dynamic memory enabled, this represents the initial memory available at startup. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the memory allocation weighting value for each virtual machine. After all reserves have been met, the remaining memory of the hosting platform will be allocated to virtual systems based on their relative weights (not to exceed the value specified by the **Limit** property). This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

**Windows Server 2008 R2 with SP1:** This property can be in the range of 0 to 10000.

**Windows Server 2008 R2 and Windows Server 2008:** This property can be in the range of 0 to 1000.

This is a read-only property, but it can be changed by using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> </dl>

## Remarks

Access to the **Msvm\_MemorySettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[Memory Classes](memory-classes.md)
</dt> </dl>

 

 





