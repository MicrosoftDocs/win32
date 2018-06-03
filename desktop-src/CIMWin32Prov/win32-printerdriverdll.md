---
Description: The Win32\_PrinterDriverDll association WMI class relates a local printer and its driver file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: decbd1de-8091-47f7-94a1-42862070b920
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_PrinterDriverDll class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PrinterDriverDll class

The **Win32\_PrinterDriverDll** association [WMI class](https://msdn.microsoft.com/windows/desktop/cfe4bcca-692e-45cd-a840-93ebfe4ae267) relates a local printer and its driver file.

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

Qualifiers: [**Key**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e)
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

Qualifiers: [**Key**](https://msdn.microsoft.com/windows/desktop/671ea769-f68d-4788-96f5-c4f86ab3b00e)
</dt> </dl>

Reference to the [**Win32\_Printer**](win32-printer.md) instance.

This property is inherited from [**CIM\_Dependency**](cim-dependency.md).

</dd> </dl>

## Remarks

The **Win32\_PrinterDriverDll** class is derived from [**CIM\_Dependency**](cim-dependency.md).

## Requirements



|                                     |                                                                                               |
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

 

 




