---
description: Represents the virtual processor settings for a virtual machine.
ms.assetid: 2B299793-E1CD-49D4-898C-AE60B49F44F5
title: Msvm_ProcessorSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ProcessorSettingData
- Msvm_ProcessorSettingData.InstanceID
- Msvm_ProcessorSettingData.Caption
- Msvm_ProcessorSettingData.Description
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
- Msvm_ProcessorSettingData.AddressOnParent
- Msvm_ProcessorSettingData.VirtualQuantityUnits
- Msvm_ProcessorSettingData.LimitCPUID
- Msvm_ProcessorSettingData.HwThreadsPerCore
- Msvm_ProcessorSettingData.LimitProcessorFeatures
- Msvm_ProcessorSettingData.MaxProcessorsPerNumaNode
- Msvm_ProcessorSettingData.MaxNumaNodesPerSocket
- Msvm_ProcessorSettingData.EnableHostResourceProtection
- Msvm_ProcessorSettingData.CpuGroupId
- Msvm_ProcessorSettingData.HideHypervisorPresent
- Msvm_ProcessorSettingData.ExposeVirtualizationExtensions
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ProcessorSettingData class

Represents the virtual processor settings for a virtual machine.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ProcessorSettingData : CIM_ResourceAllocationSettingData
{
  string  InstanceID;
  string  Caption = "Processor";
  string  Description = "A logical processor of the hypervisor running on the host computer system.";
  string  ElementName;
  uint16  ResourceType = 3;
  string  OtherResourceType;
  string  ResourceSubType = "Microsoft:Hyper-V:Processor";
  string  PoolID;
  uint16  ConsumerVisibility;
  string  HostResource[];
  string  AllocationUnits = "percent / 1000";
  uint64  VirtualQuantity = "count";
  uint64  Reservation = 0;
  uint64  Limit = 100000;
  uint32  Weight = 100;
  boolean AutomaticAllocation = True;
  boolean AutomaticDeallocation = True;
  string  Parent;
  string  Connection[];
  string  Address;
  uint16  MappingBehavior;
  string  AddressOnParent;
  string  VirtualQuantityUnits = "count";
  boolean LimitCPUID;
  uint64  HwThreadsPerCore;
  boolean LimitProcessorFeatures;
  uint64  MaxProcessorsPerNumaNode;
  uint64  MaxNumaNodesPerSocket;
  boolean EnableHostResourceProtection;
  string  CpuGroupId;
  boolean HideHypervisorPresent;
  boolean ExposeVirtualizationExtensions;
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

The address of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**AddressOnParent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the address of this resource in the context of the parent. The **Parent** and **AddressOnParent** properties are used to describe the controller relationship as well as the ordering of devices on a controller. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of allocation used by the **Reservation** and **Limit** properties. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**AutomaticAllocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**AutomaticDeallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically de-allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Connection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device to which this resource is connected. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**ConsumerVisibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the consumer's visibility to the allocated resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**CpuGroupId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Cpu Group Id this VM is bound to. When value is 0 it means is not bound to a specific CPU group.

> [!Note]  
> This property was added in Windows 10, version 1703.

 

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)). Changing this property will change the **ElementName** of the associated logical device derivative.

</dd> <dt>

**EnableHostResourceProtection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the VM should enable features that increase the protection of host resources from workload running in the VM.

> [!Note]  
> Added in Windows 10.

 

</dd> <dt>

**ExposeVirtualizationExtensions**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether Hyper-V should expose virtualized hardware virtualization extensions to the VM.

> [!Note]  
> This property was added in Windows 10, version 1703.

 

</dd> <dt>

**HideHypervisorPresent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether Hyper-V should report that a hypervisor is present to the nested guest.

> [!Note]  
> This property was added in Windows 10, version 1703.

 

</dd> <dt>

**HostResource**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Exposes a specific assignment to host or underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata) and it is always set to **Null**.

</dd> <dt>

**HwThreadsPerCore**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the number of SMT threads per core reported to the guest. This reporting is independent of whether the hardware for SMT is present.

> [!Note]  
> This property was added in Windows 10, version 1703.

 

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount of CPU resources that may be consumed by the virtual machine. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

100000

Range: 0 100000

</dd> <dt>

**LimitCPUID**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the virtual machine should lower the CPU identifier. Some older operating systems may require you to limit processor functionality in this way in order to run.

</dd> <dt>

**LimitProcessorFeatures**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the virtual machine should limit the CPU features exposed to the operating system. Limiting the processor features enables the virtual machine to be migrated to different host computer systems with different processors. Migrating virtual machines between computers with processors from different vendors is not supported.

</dd> <dt>

**MappingBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies how this resource maps to underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**MaxNumaNodesPerSocket**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of NUMA nodes that can be observed within the virtual machine as belonging to a single processor socket.

</dd> <dt>

**MaxProcessorsPerNumaNode**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of virtual processors that can be observed within the virtual machine as belonging to a single virtual NUMA node.

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the resource type when a well-defined value is not available and **ResourceType** has the value 1 (Other). This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the resource pool from which this resource was allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of CPU resources that are reserved for use by the virtual machine. These resources are guaranteed to be available for consumption by the virtual machine. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

0

Range: 0 100000

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific sub-type for this resource. For example, this may be used to distinguish different models of the same resource type. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of resource this allocation setting represents. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**VirtualQuantity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of cores in the virtual machine. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**VirtualQuantityUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unit of measurement for this resource allocation. The value of this property must be a legal value of the Programmatic Units qualifier as defined in Annex C.1 of DSP0004 V2.5 or later. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The weight for each virtual machine processor. After all reserves have been met, the remaining physical processor capacity of the hosting platform will be allocated to virtual machines based on their relative weights. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

100

Range: 0 10000

</dd> </dl>

## Remarks

Access to the **Msvm\_ProcessorSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dt>

[**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata)
</dt> <dt>

[Processor Classes](processor-classes.md)
</dt> </dl>

 

