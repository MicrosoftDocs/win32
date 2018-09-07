---
Description: The Win32\_MemoryArrayLocation association WMI class relates a logical memory array and the physical memory array on which it exists.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 455daeee-ad67-4599-84d6-fa3f4ac593aa
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32_MemoryArrayLocation class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_MemoryArrayLocation
- Win32_MemoryArrayLocation.Dependent
- Win32_MemoryArrayLocation.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_MemoryArrayLocation class

The **Win32\_MemoryArrayLocation** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a logical memory array and the physical memory array on which it exists.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{B24EF561-BBBE-11d2-ABFB-00805F538618}"), AMENDMENT]
class Win32_MemoryArrayLocation : CIM_Realizes
{
  Win32_MemoryArray         REF Dependent;
  Win32_PhysicalMemoryArray REF Antecedent;
};
```

## Members

The **Win32\_MemoryArrayLocation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_MemoryArrayLocation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PhysicalMemoryArray**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_PhysicalMemoryArray")
</dt> </dl>

A [**Win32\_PhysicalMemoryArray**](win32-physicalmemoryarray.md) that describes the physical memory array that implements the logical memory array.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_MemoryArray**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_MemoryArray")
</dt> </dl>

A [**Win32\_MemoryArray**](win32-memoryarray.md) that describes the logical memory array implemented by the physical memory array.

</dd> </dl>

## Remarks

The **Win32\_MemoryArrayLocation** class is derived from [**CIM\_Realizes**](cim-realizes.md).

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

[**CIM\_Realizes**](cim-realizes.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 




