---
Description: The CIM\_HostedFileSystem association represents a link between the computer system and the file system hosted on the computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1027fc6b-588b-4da8-8b3f-0c4c3328534a
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_HostedFileSystem class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_HostedFileSystem
- CIM_HostedFileSystem.PartComponent
- CIM_HostedFileSystem.GroupComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_HostedFileSystem class

The **CIM\_HostedFileSystem** association represents a link between the computer system and the file system hosted on the computer system.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{A2EFC898-E3D3-11d2-8601-0000F8102E5F}"), AMENDMENT]
class CIM_HostedFileSystem : CIM_SystemComponent
{
  CIM_FileSystem     REF PartComponent;
  CIM_ComputerSystem REF GroupComponent;
};
```

## Members

The **CIM\_HostedFileSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedFileSystem** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

A [**CIM\_ComputerSystem**](cim-computersystem.md) that describes the computer system.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_FileSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A [**CIM\_FileSystem**](cim-filesystem.md) that describes the file system owned by the computer system.

</dd> </dl>

## Remarks

The **CIM\_HostedFileSystem** class is derived from [**CIM\_SystemComponent**](cim-systemcomponent.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

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

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> </dl>

 

 




