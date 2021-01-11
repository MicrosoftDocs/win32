---
description: Represents the switch hardware offload status.
ms.assetid: 77a34df7-e3c4-4d91-af5a-91a03dd8246d
title: Msvm_EthernetSwitchHardwareOffloadData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_EthernetSwitchHardwareOffloadData
- Msvm_EthernetSwitchHardwareOffloadData.InstanceID
- Msvm_EthernetSwitchHardwareOffloadData.Caption
- Msvm_EthernetSwitchHardwareOffloadData.Description
- Msvm_EthernetSwitchHardwareOffloadData.ElementName
- Msvm_EthernetSwitchHardwareOffloadData.SystemCreationClassName
- Msvm_EthernetSwitchHardwareOffloadData.SystemName
- Msvm_EthernetSwitchHardwareOffloadData.CreationClassName
- Msvm_EthernetSwitchHardwareOffloadData.Name
- Msvm_EthernetSwitchHardwareOffloadData.IovVfCapacity
- Msvm_EthernetSwitchHardwareOffloadData.IovVfUsage
- Msvm_EthernetSwitchHardwareOffloadData.VmqCapacity
- Msvm_EthernetSwitchHardwareOffloadData.VmqUsage
- Msvm_EthernetSwitchHardwareOffloadData.IPsecSACapacity
- Msvm_EthernetSwitchHardwareOffloadData.IPsecSAUsage
- Msvm_EthernetSwitchHardwareOffloadData.IovQueuePairCapacity
- Msvm_EthernetSwitchHardwareOffloadData.IovQueuePairUsage
- Msvm_EthernetSwitchHardwareOffloadData.PacketDirectInUse
- Msvm_EthernetSwitchHardwareOffloadData.DefaultQueueVmmqQueuePairs
- Msvm_EthernetSwitchHardwareOffloadData.DefaultQueueVrssIndependentHostSpreading
- Msvm_EthernetSwitchHardwareOffloadData.DefaultQueueVrssExcludePrimaryProcessor
- Msvm_EthernetSwitchHardwareOffloadData.DefaultQueueVrssQueueSchedulingMode
- Msvm_EthernetSwitchHardwareOffloadData.DefaultQueueVrssMinQueuePairs
- Msvm_EthernetSwitchHardwareOffloadData.DefaultQueueVmmqEnabled
- Msvm_EthernetSwitchHardwareOffloadData.DefaultQueueVrssEnabled
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_EthernetSwitchHardwareOffloadData class

Represents the switch hardware offload status.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), UUID("1C37E01C-0CD6-496F-9076-90C131033DC2"), ExtensionId("11EC6134-128A-4A23-B12F-164184B48348"), InterfaceVersion("4"), InterfaceRevision("0"), DisplayName("Ethernet Switch Offload Resource Status"), AMENDMENT]
class Msvm_EthernetSwitchHardwareOffloadData : Msvm_EthernetSwitchData
{
  string  InstanceID;
  string  Caption = Ethernet Switch Offload Resource Status;
  string  Description = Represents the switch hardware offload status.;
  string  ElementName = Ethernet Switch Offload Resource Status;
  string  SystemCreationClassName = "Msvm_VirtualEthernetSwitch";
  string  SystemName;
  string  CreationClassName = "Msvm_EthernetSwitchHardwareOffloadData";
  string  Name;
  uint32  IovVfCapacity = 0;
  uint32  IovVfUsage = 0;
  uint32  VmqCapacity = 0;
  uint32  VmqUsage = 0;
  uint32  IPsecSACapacity = 0;
  uint32  IPsecSAUsage = 0;
  uint32  IovQueuePairCapacity = 0;
  uint32  IovQueuePairUsage = 0;
  boolean PacketDirectInUse = FALSE;
  uint32  DefaultQueueVmmqQueuePairs = 0;
  boolean DefaultQueueVrssIndependentHostSpreading = TRUE;
  boolean DefaultQueueVrssExcludePrimaryProcessor = FALSE;
  uint32  DefaultQueueVrssQueueSchedulingMode = 0;
  uint32  DefaultQueueVrssMinQueuePairs = 0;
  boolean DefaultQueueVmmqEnabled = FALSE;
  boolean DefaultQueueVrssEnabled = FALSE;
};
```

## Members

The **Msvm\_EthernetSwitchHardwareOffloadData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetSwitchHardwareOffloadData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256)
</dt> </dl>

The name of the class or subclass used in the creation of this instance. This property is inherited from [**Msvm\_EthernetSwitchData**](msvm-ethernetswitchdata.md).

</dd> <dt>

**DefaultQueueVmmqEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11), **InterfaceVersion** (3), **InterfaceRevision** (0)
</dt> </dl>

The current VMMQ setting for default queue

> [!Note]  
> Property added in Windows 10, version 1703.

 

</dd> <dt>

**DefaultQueueVmmqQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (12), **InterfaceVersion** (3), **InterfaceRevision** (0)
</dt> </dl>

The current number of queues allocated for the default queue

> [!Note]  
> Property added in Windows 10, version 1703.

 

</dd> <dt>

**DefaultQueueVrssEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10), **InterfaceVersion** (3), **InterfaceRevision** (0)
</dt> </dl>

The current VRss setting for default queue

> [!Note]  
> Property added in Windows 10, version 1703.

 

</dd> <dt>

**DefaultQueueVrssExcludePrimaryProcessor**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (15), **InterfaceVersion** (4), **InterfaceRevision** (0)
</dt> </dl>

Indicates whether the primary VMQ CPU is excluded from the VRSS/VMMQ indirection table.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**DefaultQueueVrssIndependentHostSpreading**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (16), **InterfaceVersion** (4), **InterfaceRevision** (0)
</dt> </dl>

Indicates whether to always do VRSS spreading for default queue, regardless of the RSS state of the external vPort.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**DefaultQueueVrssMinQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (13), **InterfaceVersion** (4), **InterfaceRevision** (0)
</dt> </dl>

Indicates minimum number of queues used for VRSS/VMMQ.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**DefaultQueueVrssQueueSchedulingMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (14), **InterfaceVersion** (4), **InterfaceRevision** (0)
</dt> </dl>

Indicates how VRSS/VMMQ queues are steered to different host processors.

> [!Note]  
> Added in Windows 10, version 1709.

 

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

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

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

**IovQueuePairCapacity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The maximum number of queue pairs supported by the switch.

</dd> <dt>

**IovQueuePairUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The current number of queue pairs being used by the switch.

</dd> <dt>

**IovVfCapacity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The maximum number of virtual functions supported by the switch.

</dd> <dt>

**IovVfUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The current number of virtual functions being used by the switch.

</dd> <dt>

**IPsecSACapacity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The maximum number of IPsec security association offloads supported by the switch.

</dd> <dt>

**IPsecSAUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The current number of IPsec security association offloads being used by the switch.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**, **MaxLen** (256)
</dt> </dl>

The unique name of the resource. This property is inherited from [**Msvm\_EthernetSwitchData**](msvm-ethernetswitchdata.md).

</dd> <dt>

**PacketDirectInUse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9), **InterfaceVersion** (2), **InterfaceRevision** (0)
</dt> </dl>

Indicates if packet direct is being used by the switch

> [!Note]  
> Property added in Windows 10.

 

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256)
</dt> </dl>

The hosting system's creation class name. This property is inherited from [**Msvm\_EthernetSwitchData**](msvm-ethernetswitchdata.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256)
</dt> </dl>

The name of the virtual switch to which the associated resource instance is bound. This property is inherited from [**Msvm\_EthernetSwitchData**](msvm-ethernetswitchdata.md).

</dd> <dt>

**VmqCapacity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The maximum number of virtual machine queue offloads supported by the switch.

</dd> <dt>

**VmqUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The current number of virtual machine queue offloads being used by the switch.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

