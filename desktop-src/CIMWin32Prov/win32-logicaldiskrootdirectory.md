---
Description: The Win32\_LogicalDiskRootDirectory association WMI class relates a logical disk and its directory structure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 860cd28a-2a59-4ce3-be26-8fdc869c70d1
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_LogicalDiskRootDirectory class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_LogicalDiskRootDirectory class

The **Win32\_LogicalDiskRootDirectory** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a logical disk and its directory structure.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{F25FE468-783E-11d2-90BF-0060081A46FD}"), AMENDMENT]
class Win32_LogicalDiskRootDirectory : CIM_Component
{
  Win32_LogicalDisk REF GroupComponent;
  Win32_Directory   REF PartComponent;
};
```

## Members

The **Win32\_LogicalDiskRootDirectory** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LogicalDiskRootDirectory** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalDisk**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_LogicalDisk")
</dt> </dl>

Reference to the instance representing the properties of the logical disk.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Directory**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_Directory")
</dt> </dl>

Reference to the instance representing the properties of the file directory structure.

</dd> </dl>

## Remarks

The **Win32\_LogicalDiskRootDirectory** class is derived from [**CIM\_Component**](cim-component.md).

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

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




