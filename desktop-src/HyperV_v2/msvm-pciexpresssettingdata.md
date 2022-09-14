---
description: Represents the configured state of a PCI Express port.
ms.assetid: adb03dd7-5a47-47e6-a4e4-28224164150c
title: Msvm_PciExpressSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_PciExpressSettingData
- Msvm_PciExpressSettingData.VirtualFunctions
- Msvm_PciExpressSettingData.VirtualSystemIdentifiers
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_PciExpressSettingData class

Represents the configured state of a PCI Express port.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_PciExpressSettingData : CIM_ResourceAllocationSettingData
{
  uint16 VirtualFunctions[];
  string VirtualSystemIdentifiers[];
};
```

## Members

The **Msvm\_PciExpressSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_PciExpressSettingData** class has these properties.

<dl> <dt>

**VirtualFunctions**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The virtual function number to assign to the VM.

</dd> <dt>

**VirtualSystemIdentifiers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed")
</dt> </dl>

A free-form string array of identifiers of this resource presented to the virtual computer system's operating system. The indexes and values per index are defined on a per resource basis (that is, for each enumerated **ResourceType** value). This property is set to "GUID".

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](/previous-versions/windows/desktop/virtual/modifyvirtualsystemresources-msvm-virtualsystemmanagementservice) method of the sd class.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> </dl>

 

