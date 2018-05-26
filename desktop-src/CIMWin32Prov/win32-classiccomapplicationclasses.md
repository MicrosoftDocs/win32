---
Description: The Win32\_ClassicCOMApplicationClasses association WMI class relates a COM application and a COM component grouped under it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 77f24461-9ca0-4fc3-8728-4a4b9a1edbc3
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_ClassicCOMApplicationClasses class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_ClassicCOMApplicationClasses class

The **Win32\_ClassicCOMApplicationClasses** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a COM application and a COM component grouped under it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{0F73ED54-8ED9-11d2-B340-00105A1F8569}"), AMENDMENT]
class Win32_ClassicCOMApplicationClasses : Win32_COMApplicationClasses
{
  Win32_ClassicCOMClass REF PartComponent;
  Win32_DCOMApplication REF GroupComponent;
};
```

## Members

The **Win32\_ClassicCOMApplicationClasses** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ClassicCOMApplicationClasses** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DCOMApplication**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_DCOMApplication")
</dt> </dl>

A [**Win32\_DCOMApplication**](win32-dcomapplication.md) that represents a DCOM application containing or using the COM component.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ClassicCOMClass**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_ClassicCOMClass")
</dt> </dl>

A [**Win32\_ClassicCOMClass**](win32-classiccomclass.md) that represents the COM component existing in or used by the DCOM application.

</dd> </dl>

## Remarks

The **Win32\_ClassicCOMApplicationClasses** class is derived from [**Win32\_COMApplicationClasses**](win32-comapplicationclasses.md).

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

[**Win32\_COMApplicationClasses**](win32-comapplicationclasses.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




