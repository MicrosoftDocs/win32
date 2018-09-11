---
Description: The Win32\_OperatingSystemQFE association WMI class relates an operating system and the product updates applied as represented in Win32\_QuickFixEngineering.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71985759-7e45-44df-82a9-f9a93e3b923e
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32_OperatingSystemQFE class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_OperatingSystemQFE
- Win32_OperatingSystemQFE.Antecedent
- Win32_OperatingSystemQFE.Dependent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_OperatingSystemQFE class

The **Win32\_OperatingSystemQFE** association [WMI class](https://msdn.microsoft.com/en-us/library/Aa393244(v=VS.85).aspx) relates an operating system and the product updates applied as represented in [**Win32\_QuickFixEngineering**](win32-quickfixengineering.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{2CB2C452-C516-11D2-B364-00105A1F77A1}"), AMENDMENT]
class Win32_OperatingSystemQFE : CIM_Dependency
{
  Win32_OperatingSystem     REF Antecedent;
  Win32_QuickFixEngineering REF Dependent;
};
```

## Members

The **Win32\_OperatingSystemQFE** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OperatingSystemQFE** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OperatingSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("Antecedent"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("WMI\|Win32\_OperatingSystem")
</dt> </dl>

Reference to the instance representing the system affected by the product update in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_QuickFixEngineering**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Weak**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("Dependent"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("WMI\|Win32\_QuickFixEngineering")
</dt> </dl>

Reference to the instance representing the object instance applied to the operating system in this association.

</dd> </dl>

## Remarks

The **Win32\_OperatingSystemQFE** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

[Operating System Classes](https://msdn.microsoft.com/en-us/library/Dn792258(v=VS.85).aspx)
</dt> </dl>

 

 




