---
Description: The CIM\_ComputerSystemResource class represents an association between a computer system and its available system resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 365a3cc2-89f9-4fbd-aa70-a89608fc3c1f
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_ComputerSystemResource class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ComputerSystemResource class

The **CIM\_ComputerSystemResource** class represents an association between a computer system and its available system resources.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{9B81340A-E3D3-11d2-8601-0000F8102E5F}"), AMENDMENT]
class CIM_ComputerSystemResource : CIM_SystemComponent
{
  CIM_SystemResource REF PartComponent;
  CIM_ComputerSystem REF GroupComponent;
};
```

## Members

The **CIM\_ComputerSystemResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ComputerSystemResource** class has these properties.

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

Data type: **CIM\_SystemResource**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

A [**CIM\_SystemResource**](cim-systemresource.md) that describes a system resource of the computer system.

</dd> </dl>

## Remarks

The **CIM\_ComputerSystemResource** class is derived from [**CIM\_SystemComponent**](cim-systemcomponent.md).

WMI does not implement this class. For more information about classes derived from **CIM\_ComputerSystemResource**, see [Win32 Classes](win32-provider.md).

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

 

 




