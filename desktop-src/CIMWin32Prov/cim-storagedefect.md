---
Description: The CIM\_StorageDefect aggregation collects the storage errors for a storage extent.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7acd3d25-4691-43cb-badc-662684989345
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_StorageDefect class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_StorageDefect class

The **CIM\_StorageDefect** aggregation collects the storage errors for a storage extent.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{5CC70817-DB31-11d2-85FC-0000F8102E5F}"), Aggregation, Association, AMENDMENT]
class CIM_StorageDefect
{
  CIM_StorageError  REF Error;
  CIM_StorageExtent REF Extent;
};
```

## Members

The **CIM\_StorageDefect** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_StorageDefect** class has these properties.

<dl> <dt>

**Error**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageError**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the error object, which defines the starting and ending addresses that are mapped out of the storage extent.

</dd> <dt>

**Extent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageExtent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the storage extent on which the errors occurred.

</dd> </dl>

## Remarks

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



 

 




