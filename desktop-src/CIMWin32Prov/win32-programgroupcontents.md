---
Description: The Win32\_ProgramGroupContents association WMI class relates a program group order and an individual program group or item contained in it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 687794d1-acc1-498a-9886-0c9ac762ebf4
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_ProgramGroupContents class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_ProgramGroupContents class

The **Win32\_ProgramGroupContents** association [WMI class](wmi.retrieving_a_class) relates a program group order and an individual program group or item contained in it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{86E30E83-7DB2-11d2-90CB-0060081A46FD}"), AMENDMENT]
class Win32_ProgramGroupContents : CIM_Component
{
  Win32_LogicalProgramGroup REF GroupComponent;
  Win32_ProgramGroupOrItem  REF PartComponent;
};
```

## Members

The **Win32\_ProgramGroupContents** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProgramGroupContents** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalProgramGroup**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](wmi.key_qualifier), [**Override**](wmi.standard_qualifiers) ("GroupComponent"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_LogicalProgramGroup")
</dt> </dl>

Reference to the instance representing the logical program group for this association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ProgramGroupOrItem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](wmi.key_qualifier), [**Override**](wmi.standard_qualifiers) ("PartComponent"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_ProgramGroupOrItem")
</dt> </dl>

Reference to the instance representing the **Start** menu group or item for this association.

</dd> </dl>

## Remarks

The **Win32\_ProgramGroupContents** class is derived from [**CIM\_Component**](cim-component.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Operating System Classes](wmi.operating_system_classes)
</dt> </dl>

 

 




