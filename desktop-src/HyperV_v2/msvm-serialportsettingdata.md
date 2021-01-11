---
description: Describes the setting data for a virtual serial port.
ms.assetid: 8b257bbf-495a-4eef-86a1-70e31e4a85a5
title: Msvm_SerialPortSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SerialPortSettingData
- Msvm_SerialPortSettingData.DebuggerMode
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SerialPortSettingData class

Describes the setting data for a virtual serial port.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SerialPortSettingData : CIM_ResourceAllocationSettingData
{
  boolean DebuggerMode;
};
```

## Members

The **Msvm\_SerialPortSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SerialPortSettingData** class has these properties.

<dl> <dt>

**DebuggerMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** if the debugger mode is enabled on a virtual serial port; otherwise, **false**. The debugger mode enhances the use of a Microsoft Windows kernel debugger over a virtual serial port.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> </dl>

 

 




