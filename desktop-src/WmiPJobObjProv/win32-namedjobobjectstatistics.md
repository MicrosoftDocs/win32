---
Description: The Win32\_NamedJobObjectStatistics association WMI class relates a job object and the job object I/O accounting information class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 77ee3129-7e4c-4097-af21-683198eaa12d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_NamedJobObjectStatistics class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_NamedJobObjectStatistics class

The **Win32\_NamedJobObjectStatistics** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a job object and the job object I/O accounting information class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("CIMWin32a"), Dynamic, UUID("{C741E1B8-2F7F-4f2b-9A0C-57FCFD89F5C8}"), AMENDMENT]
class Win32_NamedJobObjectStatistics : Win32_CollectionStatistics
{
  Win32_NamedJobObject         REF Collection;
  Win32_NamedJobObjectActgInfo REF Stats;
};
```

## Members

The **Win32\_NamedJobObjectStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObjectStatistics** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NamedJobObject**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to an instance of [**Win32\_NamedJobObject**](win32-namedjobobject.md) that represents a job object.

</dd> <dt>

**Stats**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NamedJobObjectActgInfo**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance of [**Win32\_NamedJobObjectActgInfo**](win32-namedjobobjectactginfo.md) that represents statistical information about a job object.

</dd> </dl>

## Remarks

The **Win32\_NamedJobObjectStatistics** class is derived from [**Win32\_CollectionStatistics**](https://msdn.microsoft.com/library/aa394092).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipjobj.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipjobj.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_CollectionStatistics**](https://msdn.microsoft.com/library/aa394092)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




