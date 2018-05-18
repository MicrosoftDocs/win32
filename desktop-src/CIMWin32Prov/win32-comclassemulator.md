---
Description: 'The Win32\_ComClassEmulator association WMI class relates two versions of a Component Object Model (COM) class.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '33899c1e-911d-49ad-be25-355dcdb8f0c7'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_ComClassEmulator class'
---

# Win32\_ComClassEmulator class

The **Win32\_ComClassEmulator** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates two versions of a Component Object Model (COM) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Association, Dynamic, Provider("CIMWin32"), UUID("{0F73ED5C-8ED9-11d2-B340-00105A1F8569}"), AMENDMENT]
class Win32_ComClassEmulator
{
  Win32_ClassicCOMClass REF NewVersion;
  Win32_ClassicCOMClass REF OldVersion;
};
```

## Members

The **Win32\_ComClassEmulator** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ComClassEmulator** class has these properties.

<dl> <dt>

**NewVersion**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ClassicCOMClass**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_ClassicCOMClass")
</dt> </dl>

Reference to the instance representing the COM component that contains interfaces emulating the older version of the component.

</dd> <dt>

**OldVersion**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ClassicCOMClass**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_ClassicCOMClass")
</dt> </dl>

Reference to the instance representing the COM component with interfaces that can be emulated by the new version of the component.

</dd> </dl>

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

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




