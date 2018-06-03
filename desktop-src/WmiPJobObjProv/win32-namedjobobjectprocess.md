---
Description: The Win32\_NamedJobObjectProcess association WMI class relates a job object and the process contained in the job object. A job can contain multiple processes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b09e93b7-e11d-49f8-8e99-c75e53f8a4ac
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_NamedJobObjectProcess class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_NamedJobObjectProcess class

The **Win32\_NamedJobObjectProcess** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a job object and the process contained in the job object. A job can contain multiple processes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, SupportsCreate, CreateBy("PutInstance"), Provider("CIMWin32a"), UUID("{486F2A44-D0BF-46c1-9543-68EF5D37F1F9}"), AMENDMENT]
class Win32_NamedJobObjectProcess : CIM_CollectedMSEs
{
  Win32_NamedJobObject REF Collection;
  Win32_Process        REF Member;
};
```

## Members

The **Win32\_NamedJobObjectProcess** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObjectProcess** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NamedJobObject**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Collection"), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance that represents the processes. This property overrides the **Collection** property inherited from [**CIM\_CollectedMSEs**](https://msdn.microsoft.com/library/aa387213).

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Process**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Member"), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance that represents the job object. This property overrides the **Member** property inherited from [**CIM\_CollectedMSEs**](https://msdn.microsoft.com/library/aa387213).

</dd> </dl>

## Remarks

The **Win32\_NamedJobObjectProcess** class is derived from [**CIM\_CollectedMSEs**](https://msdn.microsoft.com/library/aa387213).

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

[**CIM\_CollectedMSEs**](https://msdn.microsoft.com/library/aa387213)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




