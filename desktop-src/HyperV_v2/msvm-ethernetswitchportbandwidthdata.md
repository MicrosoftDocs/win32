---
description: Represents the port bandwidth feature status data.
ms.assetid: 1f7be0dd-3d2f-49ef-aff0-cb162389194a
title: Msvm_EthernetSwitchPortBandwidthData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_EthernetSwitchPortBandwidthData
- Msvm_EthernetSwitchPortBandwidthData.InstanceID
- Msvm_EthernetSwitchPortBandwidthData.Caption
- Msvm_EthernetSwitchPortBandwidthData.Description
- Msvm_EthernetSwitchPortBandwidthData.ElementName
- Msvm_EthernetSwitchPortBandwidthData.SystemCreationClassName
- Msvm_EthernetSwitchPortBandwidthData.SystemName
- Msvm_EthernetSwitchPortBandwidthData.DeviceCreationClassName
- Msvm_EthernetSwitchPortBandwidthData.DeviceID
- Msvm_EthernetSwitchPortBandwidthData.CreationClassName
- Msvm_EthernetSwitchPortBandwidthData.Name
- Msvm_EthernetSwitchPortBandwidthData.CurrentBandwidthReservationPercentage
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_EthernetSwitchPortBandwidthData class

Represents the port bandwidth feature status data.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), UUID("24AD3CE1-69BD-4978-B2AC-DAAD389D699C"), ExtensionId("11EC6134-128A-4A23-B12F-164184B48348"), InterfaceVersion("1"), InterfaceRevision("0"), DisplayName("Ethernet Switch Port Bandwidth Feature Status"), AMENDMENT]
class Msvm_EthernetSwitchPortBandwidthData : Msvm_EthernetPortData
{
  string InstanceID;
  string Caption = "Ethernet Switch Port Bandwidth Feature Status";
  string Description = "Represents the port bandwidth feature status data.";
  string ElementName = "Ethernet Switch Port Bandwidth Feature Status";
  string SystemCreationClassName = "Msvm_VirtualEthernetSwitch";
  string SystemName;
  string DeviceCreationClassName = "Msvm_EthernetSwitchPort";
  string DeviceID;
  string CreationClassName = "Msvm_EthernetSwitchPortBandwidthData";
  string Name;
  uint32 CurrentBandwidthReservationPercentage = 0;
};
```

## Members

The **Msvm\_EthernetSwitchPortBandwidthData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetSwitchPortBandwidthData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Ethernet Switch Port Bandwidth Feature Status".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

The name of the subclass used in the creation of this port data instance. This property is inherited from [**Msvm\_EthernetPortData**](msvm-ethernetportdata.md), and it is always set to "Msvm\_EthernetSwitchPortBandwidthData".

</dd> <dt>

**CurrentBandwidthReservationPercentage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (1), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

The current percentage of bandwidth reserved for this port.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Represents the port bandwidth feature status data.".

</dd> <dt>

**DeviceCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

The scoping system's creation class name. This property is inherited from [**Msvm\_EthernetPortData**](msvm-ethernetportdata.md), and it is always set to "Msvm\_EthernetSwitchPort".

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 64 )
</dt> </dl>

The Device ID of the port that scopes this port data instance. This property is inherited from [**Msvm\_EthernetPortData**](msvm-ethernetportdata.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Ethernet Switch Port Bandwidth Feature Status".

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

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

A string that uniquely identifies this port data instance within the scope of the switch and port. This property is inherited from [**Msvm\_EthernetPortData**](msvm-ethernetportdata.md).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256)
</dt> </dl>

The scoping system's creation class name. This property is inherited from [**Msvm\_EthernetPortData**](msvm-ethernetportdata.md), and it is always set to "Msvm\_VirtualEthernetSwitch".

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

The name of the virtual switch that scopes this port data instance. This property is inherited from [**Msvm\_EthernetPortData**](msvm-ethernetportdata.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

