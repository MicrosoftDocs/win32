---
Description: The CIM\_SoftwareElementActions association identifies the actions for a software element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2f8a584c-dff0-48f8-bc5f-2b833b5c0b18
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_SoftwareElementActions class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SoftwareElementActions class

The **CIM\_SoftwareElementActions** association identifies the actions for a software element.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{4B82D255-E3CD-11d2-8601-0000F8102E5F}"), Association, Aggregation, Abstract, AMENDMENT]
class CIM_SoftwareElementActions
{
  CIM_Action          REF Action;
  CIM_SoftwareElement REF Element;
};
```

## Members

The **CIM\_SoftwareElementActions** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SoftwareElementActions** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Action**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (0), [**Max**](https://msdn.microsoft.com/library/aa393650) (FALSE), [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to a [**CIM\_Action**](cim-action.md) instance.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to a [**CIM\_SoftwareElement**](cim-softwareelement.md) instance.

</dd> </dl>

## Remarks

WMI does not implement this class. For WMI classes derived from **CIM\_SoftwareElementActions**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

 




