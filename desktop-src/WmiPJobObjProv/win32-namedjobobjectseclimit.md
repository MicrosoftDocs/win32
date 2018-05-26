---
Description: The Win32\_NamedJobObjectSecLimit association WMI class relates a job object and the job object security limit settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5102620a-5515-49be-bcdd-4fcca86b5599
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_NamedJobObjectSecLimit class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_NamedJobObjectSecLimit class

The **Win32\_NamedJobObjectSecLimit** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a job object and the job object security limit settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("CIMWin32a"), Dynamic, UUID("{08E31939-FAAB-4a3b-9B10-50151D1B9D24}"), AMENDMENT]
class Win32_NamedJobObjectSecLimit : CIM_CollectionSetting
{
  Win32_NamedJobObject                REF Collection;
  Win32_NamedJobObjectSecLimitSetting REF Setting;
};
```

## Members

The **Win32\_NamedJobObjectSecLimit** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObjectSecLimit** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NamedJobObject**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Collection), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance that represents a job object.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NamedJobObjectSecLimitSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Setting), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance that represents security limit settings for a job object.

</dd> </dl>

## Remarks

The **Win32\_NamedJobObjectSecLimit** is derived from [**CIM\_CollectionSetting**](https://msdn.microsoft.com/library/aa387216).

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

[**CIM\_CollectionSetting**](https://msdn.microsoft.com/library/aa387216)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




