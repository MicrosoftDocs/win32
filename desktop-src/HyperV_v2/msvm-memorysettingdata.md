---
description: Represents the configured state of the memory for a virtual machine.
ms.assetid: 4B6FEE50-1C5F-4F41-B14A-E10B40400A1B
title: Msvm_MemorySettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MemorySettingData
- Msvm_MemorySettingData.InstanceID
- Msvm_MemorySettingData.Caption
- Msvm_MemorySettingData.Description
- Msvm_MemorySettingData.ElementName
- Msvm_MemorySettingData.ResourceType
- Msvm_MemorySettingData.OtherResourceType
- Msvm_MemorySettingData.ResourceSubType
- Msvm_MemorySettingData.PoolID
- Msvm_MemorySettingData.ConsumerVisibility
- Msvm_MemorySettingData.HostResource
- Msvm_MemorySettingData.HugePagesEnabled
- Msvm_MemorySettingData.AllocationUnits
- Msvm_MemorySettingData.VirtualQuantity
- Msvm_MemorySettingData.Reservation
- Msvm_MemorySettingData.Limit
- Msvm_MemorySettingData.Weight
- Msvm_MemorySettingData.AutomaticAllocation
- Msvm_MemorySettingData.AutomaticDeallocation
- Msvm_MemorySettingData.Parent
- Msvm_MemorySettingData.Connection
- Msvm_MemorySettingData.Address
- Msvm_MemorySettingData.MappingBehavior
- Msvm_MemorySettingData.AddressOnParent
- Msvm_MemorySettingData.VirtualQuantityUnits
- Msvm_MemorySettingData.DynamicMemoryEnabled
- Msvm_MemorySettingData.TargetMemoryBuffer
- Msvm_MemorySettingData.IsVirtualized
- Msvm_MemorySettingData.SwapFilesInUse
- Msvm_MemorySettingData.MaxMemoryBlocksPerNumaNode
- Msvm_MemorySettingData.SgxSize
- Msvm_MemorySettingData.SgxEnabled
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm_MemorySettingData class

Represents the configured state of the memory for a virtual machine.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MemorySettingData : CIM_ResourceAllocationSettingData
{
  string  InstanceID;
  string  Caption = "Memory Default Settings";
  string  Description = "Describes the default settings for the memory resources.";
  string  ElementName;
  uint16  ResourceType = 4;
  string  OtherResourceType;
  string  ResourceSubType = "Microsoft:Hyper-V:Memory";
  string  PoolID;
  uint16  ConsumerVisibility;
  string  HostResource[];
  boolean HugePagesEnabled;
  string  AllocationUnits = "byte * 2^20";
  uint64  VirtualQuantity;
  uint64  Reservation;
  uint64  Limit;
  uint32  Weight;
  boolean AutomaticAllocation = True;
  boolean AutomaticDeallocation = True;
  string  Parent;
  string  Connection[];
  string  Address;
  uint16  MappingBehavior;
  string  AddressOnParent;
  string  VirtualQuantityUnits = "byte * 2^20";
  boolean DynamicMemoryEnabled;
  uint32  TargetMemoryBuffer;
  boolean IsVirtualized = True;
  boolean SwapFilesInUse;
  uint64  MaxMemoryBlocksPerNumaNode;
  uint64  SgxSize;
  boolean SgxEnabled;
};
```

## Members

The **Msvm_MemorySettingData** class has these types of members:

* [Properties](#properties)

### Properties

The **Msvm_MemorySettingData** class has these properties.

#### Address

Data type: **string**

Access type: read-only

The address of the resource. For example, the MAC address of an Ethernet port. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### AddressOnParent

Data type: **string**

Access type: read-only

Describes the address of this resource in the context of the parent. The **Parent** and **AddressOnParent** properties are used to describe the controller relationship as well as the ordering of devices on a controller. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### AllocationUnits

Data type: **string**

Access type: read-only

The units of allocation used by the **Reservation** and **Limit** properties. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### AutomaticAllocation

Data type: **boolean**

Access type: read-only

Indicates whether the resource will be automatically allocated. For example, when this property is set to **True** and the consuming virtual machine is powered on, this resource would be allocated. A value of **False** indicates the resource must be explicitly allocated. For example, the setting may represent removable media (such as a CD-ROM or a floppy disk) where at startup, the media is not present. An explicit operation is required to allocate the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### AutomaticDeallocation

Data type: **boolean**

Access type: read-only

Indicates whether the resource will be automatically allocated. For example when this property is set to **True** and the consuming virtual machine is powered on, this resource would be allocated. When this property is **False**, the resource must be explicitly allocated. For example, the setting may represent removable media (such as a CD-ROM or a floppy disk) where at startup, the media is not present. An explicit operation is required to allocate the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### Caption

Data type: **string**

Access type: read-only

Qualifiers: **MaxLen** (64)

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

#### Connection

Data type: **string** array

Access type: read-only

The device to which this resource is connected. For example, a named network or switch port. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### ConsumerVisibility

Data type: **uint16**

Access type: read-only

Describes the consumers visibility to the allocated resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### Description

Data type: **string**

Access type: read-only

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

#### DynamicMemoryEnabled

Data type: **boolean**

Access type: read-only

Indicates whether dynamic memory is enabled for the virtual machine.

#### ElementName

Data type: **string**

Access type: read-only

A display name for the object. This property is inherited from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)).

#### HostResource

Data type: **string** array

Access type: read-only

The first element of this array contains a reference to the underlying host resource to be assigned. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata), but it is not used.

#### HugePagesEnabled

Data type: **boolean**

Access type: read-only

Whether the memory is backed by 1GB pages or not.

#### InstanceID

Data type: **string**

Access type: read-only

Qualifiers: **Key**

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

#### IsVirtualized

Data type: **boolean**

Access type: read-only

Indicates whether this device is virtualized or passed through. When set to **False**, the underlying or host resource is used. At least one item should be present in the **DeviceID** property. When set to **True**, the resource is virtualized and may not map directly to an underlying/host resource. Some implementations may support specific assignment for virtualized resources, in which case the host resources are exposed by using the **DeviceID** property. This property is always set to **True**.

#### Limit

Data type: **uint64**

Access type: read-only

The maximum amount of memory that may be consumed by the virtual machine. For a virtual machine with dynamic memory enabled, this represents the maximum memory setting. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### MappingBehavior

Data type: **uint16**

Access type: read-only

Specifies how this resource maps to underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### MaxMemoryBlocksPerNumaNode

Data type: **uint64**

Access type: read-only

The maximum amount of memory that can be observed within the virtual machine as belonging to a single NUMA node.

#### OtherResourceType

Data type: **string**

Access type: read-only

A string that describes the resource type when a well-defined value is not available and **ResourceType** has the value "Other". This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### Parent

Data type: **string**

Access type: read-only

The parent of the resource. For example, a controller for the current allocation. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### PoolID

Data type: **string**

Access type: read-only

The identifier of the resource pool from which this resource was allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### Reservation

Data type: **uint64**

Access type: read-only

Specifies the amount of memory guaranteed to be available for this virtual machine. For a virtual machine with dynamic memory enabled, this represents the minimum memory setting. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### ResourceSubType

Data type: **string**

Access type: read-only

A string that describes an implementation specific subtype for this resource. For example, this may be used to distinguish different models of the same resource type. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### ResourceType

Data type: **uint16**

Access type: read-only

The type of resource that this allocation setting represents. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata), and it is always set to 4 (Memory).

#### SgxEnabled

Data type: **boolean**

Access type: read-only

Indicates if SGX is enabled.

> [!NOTE]
> This property was added in Windows 10, version 1703.

#### SgxSize

Data type: **uint64**

Access type: read-only

The amount of SGX memory to allocate for the VM, in MB.

> [!NOTE]  
> This property was added in Windows 10, version 1703.

#### SwapFilesInUse

Data type: **boolean**

Access type: read-only

**true** if second level paging is active; otherwise, **false**.

#### TargetMemoryBuffer

Data type: **uint32**

Access type: read-only

Defines the amount of extra memory that should be reserved for a virtual machine at runtime, as a percentage of the total memory that the virtual machine is thought to need. This only applies to virtual machines with dynamic memory enabled.

This property can be in the range of 5 to 2000.

#### VirtualQuantity

Data type: **uint64**

Access type: read-only

The total amount of RAM in the virtual machine, as seen by the guest operating system. For a virtual machine with dynamic memory enabled, this represents the initial memory available at startup. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### VirtualQuantityUnits

Data type: **string**

Access type: read-only

Specifies the unit of measurement for this resource allocation. The value of this property must be a legal value of the Programmatic Units qualifier as defined in Annex C.1 of DSP0004 V2.5 or later. This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

#### Weight

Data type: **uint32**

Access type: read-only

Defines the memory allocation weighting value for each virtual machine. After all reserves have been met, the remaining memory of the hosting platform will be allocated to virtual machines based on their relative weights (not to exceed the value specified by the **Limit** property). This property is inherited from [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

## Remarks

Access to the **Msvm_MemorySettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

```powershell
function WaitForResult
{
  param($result)
  if ($result.ReturnValue -eq 4096)
  {
    while($true)
    {
      $result.Job
      if ($result.Job -ne $null)
      {
        if ($result.Job.JobState -gt 4)
        {
          return $result.Job.ErrorCode
        }
      }
      start-sleep 1
    }
  }
  else
  {
    return $result.ReturnValue
  }
}

if ($($args.count) -ne 2)
{
  Write-Host "EnableHugePages.ps1 VMName SizeInMB"
  return
}

$vmName = $args[0]
$sizeInMB = $args[1]
 
$namespace = "root\virtualization\v2"
$vm = Get-WmiObject -class MSVM_ComputerSystem -filter "ElementName='$vmName'" -namespace $namespace
$settings = Get-WmiObject -query "Associators of {$vm} where ResultClass = Msvm_VirtualSystemSettingData" -namespace $namespace
$vmSettings = $settings | ? VirtualSystemType -eq "Microsoft:Hyper-V:System:Realized"
$memorySettings = Get-WmiObject -query "Associators of {$vmSettings} where ResultClass = Msvm_MemorySettingData" -namespace $namespace

$memorySettings.MaxMemoryBlocksPerNumaNode = $sizeInMB
$memorySettings.Reservation = $sizeInMB
$memorySettings.Limit = $sizeInMB
$memorySettings.VirtualQuantity = $sizeInMB
$memorySettings.HugePagesEnabled = $True

$vmSvc = Get-WmiObject -class Msvm_VirtualSystemManagementService -namespace $namespace
$res = $vmSvc.ModifyResourceSettings($memorySettings.GetText(2))
if (WaitForResult($res) -ne 0)
{
  Write-Host "Failed."
}
```

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | WindowsVirtualization.V2.mof |
| DLL<br/>                      | Vmms.exe                     |

## See also

* [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
* [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata)
* [Memory classes](memory-classes.md)
