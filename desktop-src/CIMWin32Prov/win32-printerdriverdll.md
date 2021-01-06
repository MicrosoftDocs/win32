---
description: The Win32\_PrinterDriverDll association WMI class relates a local printer and its driver file.
ms.assetid: decbd1de-8091-47f7-94a1-42862070b920
ms.tgt_platform: multiple
title: Win32_PrinterDriverDll class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PrinterDriverDll
- Win32_PrinterDriverDll.Antecedent
- Win32_PrinterDriverDll.Dependent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_PrinterDriverDll class

The **Win32\_PrinterDriverDll** association [WMI class](../wmisdk/retrieving-a-class.md) relates a local printer and its driver file.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_PrinterDriverDll : CIM_Dependency
{
  CIM_DataFile  REF Antecedent;
  Win32_Printer REF Dependent;
};
```

## Members

The **Win32\_PrinterDriverDll** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PrinterDriverDll** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DataFile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/standard-qualifiers.md)
</dt> </dl>

Reference to the [**CIM\_DataFile**](cim-datafile.md) instance representing the driver file for this Windows-based printer.

This property is inherited from [**CIM\_Dependency**](cim-dependency.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Printer**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/standard-qualifiers.md)
</dt> </dl>

Reference to the [**Win32\_Printer**](win32-printer.md) instance.

This property is inherited from [**CIM\_Dependency**](cim-dependency.md).

</dd> </dl>

## Remarks

The **Win32\_PrinterDriverDll** class is derived from [**CIM\_Dependency**](cim-dependency.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
