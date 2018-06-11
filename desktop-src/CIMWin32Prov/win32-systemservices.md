---
Description: The Win32\_SystemServices association WMI class relates a computer system and a service program that exists on the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b372e696-e1e0-4b1e-9fb8-83af8a75c405
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SystemServices class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SystemServices class

The **Win32\_SystemServices** association [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) relates a computer system and a service program that exists on the system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4F6-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemServices : CIM_SystemComponent
{
  Win32_ComputerSystem REF GroupComponent;
  Win32_Service        REF PartComponent;
};
```

## Members

The **Win32\_SystemServices** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemServices** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("GroupComponent"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the properties of the computer system on which the service exists.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("PartComponent"), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI\|Win32\_Service")
</dt> </dl>

Reference to the instance representing the service that exists on the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemServices** class is derived from [**CIM\_SystemComponent**](cim-systemcomponent.md).

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

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/windows/desktop/D0756D8C-A3D3-4C75-96A3-8C7F05300B39)
</dt> </dl>

 

 




