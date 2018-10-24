---
Description: The Win32\_SystemResources association WMI class relates a system resource and the computer system it resides on.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 90bff0b0-7c1d-44bf-b67e-aefeaa4b4a83
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32_SystemResources class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemResources
- Win32_SystemResources.GroupComponent
- Win32_SystemResources.PartComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_SystemResources class

The **Win32\_SystemResources** association [WMI class](https://msdn.microsoft.com/en-us/library/Aa393244(v=VS.85).aspx) relates a system resource and the computer system it resides on.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4F8-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemResources : CIM_ComputerSystemResource
{
  Win32_ComputerSystem REF GroupComponent;
  CIM_SystemResource   REF PartComponent;
};
```

## Members

The **Win32\_SystemResources** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemResources** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("GroupComponent"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the computer system where the resource is located.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SystemResource**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("PartComponent"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("CIM\|CIM\_SystemResource")
</dt> </dl>

Reference to the instance representing the resource (such as I/O services and memory resources) available on the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemResources** class is derived from [**CIM\_ComputerSystemResource**](cim-computersystemresource.md).

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

[**CIM\_ComputerSystemResource**](cim-computersystemresource.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/en-us/library/Dn792258(v=VS.85).aspx)
</dt> </dl>

 

 




