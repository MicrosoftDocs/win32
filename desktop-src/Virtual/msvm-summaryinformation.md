---
title: Msvm\_SummaryInformation class
description: Used in the GetSummaryInformation method in the Msvm\_VirtualSystemManagementService class to quickly retrieve common information related to a virtual machine or snapshot.
ms.assetid: 91503a84-5899-4f98-b8c9-6bfdddae2003
keywords:
- Msvm_SummaryInformation class Hyper-V
- Msvm_SummaryInformation class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_SummaryInformation
- Msvm_SummaryInformation.Name
- Msvm_SummaryInformation.ElementName
- Msvm_SummaryInformation.EnabledState
- Msvm_SummaryInformation.HealthState
- Msvm_SummaryInformation.Notes
- Msvm_SummaryInformation.NumberOfProcessors
- Msvm_SummaryInformation.ThumbnailImage
- Msvm_SummaryInformation.CreationTime
- Msvm_SummaryInformation.ProcessorLoad
- Msvm_SummaryInformation.ProcessorLoadHistory
- Msvm_SummaryInformation.MemoryUsage
- Msvm_SummaryInformation.MemoryAvailable
- Msvm_SummaryInformation.AvailableMemoryBuffer
- Msvm_SummaryInformation.Heartbeat
- Msvm_SummaryInformation.UpTime
- Msvm_SummaryInformation.GuestOperatingSystem
- Msvm_SummaryInformation.OperationalStatus
- Msvm_SummaryInformation.StatusDescriptions
- Msvm_SummaryInformation.Snapshots
- Msvm_SummaryInformation.AsynchronousTasks
- Msvm_SummaryInformation.AllocatedGPU
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

# Msvm\_SummaryInformation class

Used in the [**GetSummaryInformation**](getsummaryinformation-msvm-virtualsystemmanagementservice.md) method in the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class to quickly retrieve common information related to a virtual machine or snapshot.

The following syntax is simplified Managed Object Format (MOF) code.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SummaryInformation
{
  string                       Name;
  string                       ElementName;
  uint16                       EnabledState;
  uint16                       HealthState;
  string                       Notes;
  uint16                       NumberOfProcessors;
  uint8                        ThumbnailImage[];
  DateTime                     CreationTime;
  uint16                       ProcessorLoad;
  uint16                       ProcessorLoadHistory[];
  uint64                       MemoryUsage;
  sint32                       MemoryAvailable;
  sint32                       AvailableMemoryBuffer;
  uint16                       Heartbeat;
  uint64                       UpTime;
  string                       GuestOperatingSystem;
  uint16                       OperationalStatus[];
  string                       StatusDescriptions[];
  CIM_VirtualSystemSettingData Snapshots[];
  CIM_ConcreteJob              AsynchronousTasks[];
  string                       AllocatedGPU;
};
```

## Members

The **Msvm\_SummaryInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SummaryInformation** class has these properties.

<dl> <dt>

**AllocatedGPU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the physical graphics processing unit (GPU) allocated to this virtual machine (VM). This property only applies to VMs that use RemoteFX.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not supported before Windows Server 2008 R2 with SP1.

</dd> <dt>

**AsynchronousTasks**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ConcreteJob** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

An array of [**Msvm\_ConcreteJob**](msvm-concretejob.md) instances that represent any asynchronous operations related to the virtual system which are currently executing. This property is not valid for instances of **Msvm\_SummaryInformation** that represent a virtual system snapshot.

</dd> <dt>

**AvailableMemoryBuffer**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of available memory buffer for the virtual machine (VM). When dynamic memory is enabled for a VM, this property represents the ratio of available memory buffer to the ideal memory buffer for the VM. The ideal memory buffer size is configured by using the **TargetMemoryBuffer** property of the [**Msvm\_MemorySettingData**](msvm-memorysettingdata.md) class.

This property is not valid for instances of the **Msvm\_SummaryInformation** class that represent virtual machines for which dynamic memory is not enabled.

This property is not valid for instances of the **Msvm\_SummaryInformation** class that represent a virtual system snapshot.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not supported before Windows Server 2008 R2 with SP1.

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time at which the virtual system or snapshot was created.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name for the virtual system or snapshot.

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the virtual system or snapshot.

</dd> <dt>

**GuestOperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the guest operating system, if available. If this information is not available, the value of this property is **NULL**. This property is not valid for instances of **Msvm\_SummaryInformation** that represent a virtual system snapshot.

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health state for the virtual system. This property is not valid for instances of **Msvm\_SummaryInformation** that represent a virtual system snapshot.

</dd> <dt>

**Heartbeat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current heartbeat status for the virtual system. For more information, see the documentation for the [**StatusDescriptions**](msvm-heartbeatcomponent.md) property of the **Msvm\_HeartbeatComponent** class. This property is not valid for instances of **Msvm\_SummaryInformation** that represent a virtual system snapshot.

<dl> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (2)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)
</dt> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)
</dt> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)
</dt> </dl>

</dd> <dt>

**MemoryAvailable**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of the current memory available to the virtual machine (VM). When dynamic memory is enabled for a VM, this property represents the ratio of available memory of the VM to the total physical memory assigned to the VM. When a VM has no available memory, this property will be negative, and it will contain the ratio of memory needed for the VM to the total physical memory assigned to the VM.

This property is not valid for instances of the **Msvm\_SummaryInformation** class that represent virtual machines for which dynamic memory is not enabled.

This property is not valid for instances of the **Msvm\_SummaryInformation** class that represent a virtual system snapshot.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not supported before Windows Server 2008 R2 with SP1.

</dd> <dt>

**MemoryUsage**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current memory usage of the virtual system. This property is not valid for instances of **Msvm\_SummaryInformation** that represent a virtual system snapshot.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique name for the virtual system or snapshot.

</dd> <dt>

**Notes**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The notes associated with the virtual system or snapshot.

</dd> <dt>

**NumberOfProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of virtual processors allocated to the virtual system or snapshot.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The current statuses of the virtual system. This corresponds to the **OperationalStatus** property of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class.

**Windows Server 2008:** This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**ProcessorLoad**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current processor usage of the virtual system. This property is not valid for instances of **Msvm\_SummaryInformation** representing a virtual system snapshot.

</dd> <dt>

**ProcessorLoadHistory**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

An array of the previous 100 samples of the processor usage for the virtual system. This property is not valid for instances of **Msvm\_SummaryInformation** that represent a virtual system snapshot.

</dd> <dt>

**Snapshots**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VirtualSystemSettingData** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

An array of [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) instances representing the snapshots for the virtual system. This property is not valid for instances of **Msvm\_SummaryInformation** that represent a virtual system snapshot.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Strings that describe the corresponding **OperationalStatus** array values. This corresponds to the **StatusDescriptions** property of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class.

**Windows Server 2008:** This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**ThumbnailImage**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

An array that contains a small, thumbnail-sized image of the desktop for the virtual system or snapshot in RGB565 format.

</dd> <dt>

**UpTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of time since the virtual system was last booted. This property is not valid for instances of **Msvm\_SummaryInformation** representing a virtual system snapshot.

</dd> </dl>

## Remarks

Access to the **Msvm\_SummaryInformation** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 





