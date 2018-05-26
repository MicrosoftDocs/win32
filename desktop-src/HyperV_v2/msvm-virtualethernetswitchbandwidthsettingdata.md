---
Description: Represents the bandwidth settings for a virtual switch.
ms.assetid: bc6f8cd3-f74a-4f4a-9ffe-a88def3966d9
title: Msvm\_VirtualEthernetSwitchBandwidthSettingData class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_VirtualEthernetSwitchBandwidthSettingData class

Represents the bandwidth settings for a virtual switch.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), UUID("3EB2B8E8-4ABF-4DBF-9071-16DD47481FBE"), ExtensionId("11EC6134-128A-4A23-B12F-164184B48348"), InterfaceVersion("1"), InterfaceRevision("0"), DisplayName("Ethernet Switch Bandwidth Settings"), AMENDMENT]
class Msvm_VirtualEthernetSwitchBandwidthSettingData : Msvm_EthernetSwitchFeatureSettingData
{
  string InstanceID = "Microsoft:Definition\GUID\Default";
  string Caption = "Ethernet Switch Bandwidth Settings";
  string Description = "Represents the switch bandwidth settings.";
  string ElementName = "Ethernet Switch Bandwidth Settings";
  UINT64 DefaultFlowReservation = 0;
  UINT64 DefaultFlowWeight = 0;
};
```

## Members

The **Msvm\_VirtualEthernetSwitchBandwidthSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualEthernetSwitchBandwidthSettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from the [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218) class and is always set to "Ethernet Switch Bandwidth Settings".

</dd> <dt>

**DefaultFlowReservation**
</dt> <dd> <dl> <dt>

Data type: **UINT64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (1), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

Specifies the absolute bandwidth reservation for unclassified flows on the underlying adapter.

</dd> <dt>

**DefaultFlowWeight**
</dt> <dd> <dl> <dt>

Data type: **UINT64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (2), **InterfaceVersion** (1), **InterfaceRevision** (0)
</dt> </dl>

Specifies the bandwidth reservation in weight for unclassified flows on the underlying adapter.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218), and it is always set to "Represents the switch bandwidth settings.".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911), and it is always set to "Ethernet Switch Bandwidth Settings".

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) and is always set to "Microsoft:Definition\\*GUID*\\Default".

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

 




