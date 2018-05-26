---
Description: The Win32\_SystemDriverPNPEntity association WMI class relates a Plug and Play device on the computer system running Windows and the driver that supports the Plug and Play device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2696c8e5-3bc3-42e3-807b-a387607c7c09
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SystemDriverPNPEntity class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_SystemDriverPNPEntity class

The **Win32\_SystemDriverPNPEntity** association [WMI class](wmi.retrieving_a_class) relates a Plug and Play device on the computer system running Windows and the driver that supports the Plug and Play device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{0800F074-CB98-11d2-B35D-00104BC97924}"), AMENDMENT]
class Win32_SystemDriverPNPEntity : CIM_Dependency
{
  Win32_PNPEntity    REF Antecedent;
  Win32_SystemDriver REF Dependent;
};
```

## Members

The **Win32\_SystemDriverPNPEntity** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemDriverPNPEntity** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PNPEntity**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](wmi.key_qualifier), [**Override**](wmi.standard_qualifiers) ("Antecedent"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_PNPEntity")
</dt> </dl>

Represents the Plug and Play device controlled by the driver.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SystemDriver**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](wmi.key_qualifier), [**Override**](wmi.standard_qualifiers) ("Dependent"), [**MappingStrings**](wmi.standard_qualifiers) ("WMI\|Win32\_SystemDriver")
</dt> </dl>

A [**Win32\_SystemDriver**](win32-systemdriver.md) that represents the driver that supports the Plug and Play device.

</dd> </dl>

## Remarks

The **Win32\_SystemDriverPNPEntity** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 




