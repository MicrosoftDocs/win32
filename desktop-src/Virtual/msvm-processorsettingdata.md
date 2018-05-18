---
title: Msvm\_ProcessorSettingData class
description: Represents the virtual processor settings for a virtual machine (VM).
ms.assetid: '96780b3e-c338-4c79-bf40-a193f5d370be'
keywords: ["Msvm_ProcessorSettingData class Hyper-V", "Msvm_ProcessorSettingData class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_ProcessorSettingData
- Msvm_ProcessorSettingData.Caption
- Msvm_ProcessorSettingData.Description
- Msvm_ProcessorSettingData.InstanceID
- Msvm_ProcessorSettingData.ElementName
- Msvm_ProcessorSettingData.ResourceType
- Msvm_ProcessorSettingData.OtherResourceType
- Msvm_ProcessorSettingData.ResourceSubType
- Msvm_ProcessorSettingData.PoolID
- Msvm_ProcessorSettingData.ConsumerVisibility
- Msvm_ProcessorSettingData.HostResource
- Msvm_ProcessorSettingData.AllocationUnits
- Msvm_ProcessorSettingData.VirtualQuantity
- Msvm_ProcessorSettingData.Reservation
- Msvm_ProcessorSettingData.Limit
- Msvm_ProcessorSettingData.Weight
- Msvm_ProcessorSettingData.AutomaticAllocation
- Msvm_ProcessorSettingData.AutomaticDeallocation
- Msvm_ProcessorSettingData.Parent
- Msvm_ProcessorSettingData.Connection
- Msvm_ProcessorSettingData.Address
- Msvm_ProcessorSettingData.MappingBehavior
- Msvm_ProcessorSettingData.IsVirtualized
- Msvm_ProcessorSettingData.DeviceID
- Msvm_ProcessorSettingData.DeviceIDFormat
- Msvm_ProcessorSettingData.ProcessorsPerSocket
- Msvm_ProcessorSettingData.SocketCount
- Msvm_ProcessorSettingData.ThreadsEnabled
- Msvm_ProcessorSettingData.LimitCPUID
- Msvm_ProcessorSettingData.LimitProcessorFeatures
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_ProcessorSettingData class

Represents the virtual processor settings for a virtual machine (VM).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ProcessorSettingData : CIM_ResourceAllocationSettingData
{
  string  Caption = "Processor";
  string  Description = "Settings for Microsoft Virtual Processor";
  string  InstanceID;
  string  ElementName = "Processor";
  uint16  ResourceType = 3;
  string  OtherResourceType;
  string  ResourceSubType = "Microsoft Processor";
  string  PoolID;
  uint16  ConsumerVisibility;
  string  HostResource[];
  string  AllocationUnits = "Processor Cores";
  uint64  VirtualQuantity;
  uint64  Reservation;
  uint64  Limit;
  uint32  Weight;
  boolean AutomaticAllocation = True;
  boolean AutomaticDeallocation = True;
  string  Parent;
  string  Connection[];
  string  Address;
  uint16  MappingBehavior;
  boolean IsVirtualized = True;
  string  DeviceID = "Microsoft:GUID";
  string  DeviceIDFormat;
  uint16  ProcessorsPerSocket;
  uint16  SocketCount;
  boolean ThreadsEnabled;
  boolean LimitCPUID;
  boolean LimitProcessorFeatures;
};
```

## Members

The **Msvm\_ProcessorSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ProcessorSettingData** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of allocation used by the **Reservation** and **Limit** properties. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to "Processor Cores".

</dd> <dt>

**AutomaticAllocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **True**.

</dd> <dt>

**AutomaticDeallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically de-allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **True**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Processor".

</dd> <dt>

**Connection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device to which this resource is connected. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**ConsumerVisibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the consumer's visibility to the allocated resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Settings for Microsoft Virtual Processor".

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

The format of the corresponding device ID, or the supported device IDs when used to represent a capability. This property is not used.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) and it is set to "Processor". Changing this property will change the **ElementName** of the associated logical device derivative.

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

Exposes specific assignment to host or underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

For instances associated with a virtual system, this will be "Microsoft:*GUID*\\*device-specific data*". For instances which define potential settings for a VM, this will be "Microsoft:Definition\\*GUID*\\*Type*", where *Type* can be one of "Maximum", "Minimum", "Default", or "Increment". This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**IsVirtualized**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this device is virtualized or passed through. When set to **False**, the underlying or host resource is utilized. At least one item shall be present in the **DeviceID** property. When set to **True**, the resource is virtualized and may not map directly to an underlying/host resource. Some implementations may support specific assignment for virtualized resources, in which case the host resource(s) are exposed using the **DeviceID** property. This property is set to **True**.

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount of CPU resources that may be consumed by the VM. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and has a default value of 100000.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

Range: 0–100000

</dd> <dt>

**LimitCPUID**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the VM should lower the CPU identifier. Some older operating systems may require you to limit processor functionality in this way in order to run.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**LimitProcessorFeatures**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the VM should limit the CPU features exposed to the operating system. Limiting the processor features enables the VM to be migrated to different host computer systems with different processors. Migrating VMs between computers with processors from different vendors is not supported.

**Windows Server 2008:** The **LimitProcessorFeatures** property is not supported until Windows Server 2008 R2.

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

A string that describes the resource type when a well-defined value is not available and **ResourceType** has the value 1 (Other). This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to **NULL**.

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

**ProcessorsPerSocket**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of processors, or cores, configured for each socket in the VM.

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of CPU resources that are reserved for use by the VM. These resources are guaranteed to be available for consumption by the VM. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and has a default value of 0.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

Range: 0–100000

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific sub-type for this resource. For example, this may be used to distinguish different models of the same resource type. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to "Microsoft Processor".

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**OtherResourceType**")
</dt> </dl>

The type of resource this allocation setting represents. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and it is always set to 3 (Processor).

</dd> <dt>

**SocketCount**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of processor sockets in the VM. The total number of processors is the value of this property times the value of the **ProcessorsPerSocket** property.

</dd> <dt>

**ThreadsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether hardware threads should be visible to the VM. If the physical processor does not support hardware threads, this value has no effect in the VM.

</dd> <dt>

**VirtualQuantity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of cores in the VM. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The weight for each VM processor. After all reserves have been met, the remaining physical processor capacity of the hosting platform will be allocated to VMs based on their relative weights. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and has a default value of 100.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

Range: 0–100000

</dd> </dl>

## Remarks

Access to the **Msvm\_ProcessorSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dt>

[**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214)
</dt> <dt>

[Processor Classes](processor-classes.md)
</dt> </dl>

 

 





