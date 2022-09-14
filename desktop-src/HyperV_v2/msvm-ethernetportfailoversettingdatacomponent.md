---
description: An association used to establish relationships between one instance of an Msvm\_EmulatedEthernetPortSettingData and one or more instances of an Msvm\_EthernetSwitchFeatureSettingData.
ms.assetid: A2929D81-ED86-4C5A-9280-276204EDE89B
title: Msvm_EthernetPortFailoverSettingDataComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_EthernetPortFailoverSettingDataComponent
- Msvm_EthernetPortFailoverSettingDataComponent.GroupComponent
- Msvm_EthernetPortFailoverSettingDataComponent.PartComponent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_EthernetPortFailoverSettingDataComponent class

An association used to establish relationships between one instance of an [**Msvm\_EmulatedEthernetPortSettingData**](msvm-emulatedethernetportsettingdata.md) and one or more instances of an [**Msvm\_EthernetSwitchFeatureSettingData**](msvm-ethernetswitchfeaturesettingdata.md).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_EthernetPortFailoverSettingDataComponent : CIM_Component
{
  CIM_ResourceAllocationSettingData      REF GroupComponent;
  Msvm_FailoverNetworkAdapterSettingData REF PartComponent;
};
```

## Members

The **Msvm\_EthernetPortFailoverSettingDataComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetPortFailoverSettingDataComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent"), [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

A reference to an instance of the [**Msvm\_EmulatedEthernetPortSettingData**](msvm-emulatedethernetportsettingdata.md) or [**Msvm\_SyntheticEthernetPortSettingData**](msvm-syntheticethernetportsettingdata.md) class that represents the Ethernet port.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_FailoverNetworkAdapterSettingData**](msvm-failovernetworkadaptersettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

A reference to an instance of the [**Msvm\_FailoverNetworkAdapterSettingData**](msvm-failovernetworkadaptersettingdata.md) class that represents the guest network adapter configuration.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

