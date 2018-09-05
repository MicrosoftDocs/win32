---
Description: The Win32\_DeviceBus association WMI class relates a system bus and a logical device using the bus. This class is used to discover which devices are on which bus.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2d7d83a5-c058-40c0-aab3-7700f4067a16
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32_DeviceBus class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_DeviceBus
- Win32_DeviceBus.Dependent
- Win32_DeviceBus.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_DeviceBus class

The **Win32\_DeviceBus** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a system bus and a logical device using the bus. This class is used to discover which devices are on which bus.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C50F-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_DeviceBus : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  Win32_Bus         REF Antecedent;
};
```

## Members

The **Win32\_DeviceBus** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DeviceBus** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Bus**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_Bus")
</dt> </dl>

A [**Win32\_Bus**](win32-bus.md) that describes the properties of the system bus that is used by the logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("CIM\|CIM\_LogicalDevice")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that describes the properties of the logical device that is using the system bus.

</dd> </dl>

## Remarks

The **Win32\_DeviceBus** class is derived from [**CIM\_Dependency**](cim-dependency.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 




