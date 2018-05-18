---
Description: 'The Win32\_NamedJobObjectLimit association WMI class class represents an association between a job object and the job object limit settings.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'be5c5866-d970-4310-b6b7-5e4bfbba4039'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_NamedJobObjectLimit class'
---

# Win32\_NamedJobObjectLimit class

The **Win32\_NamedJobObjectLimit** association [WMI class](https://msdn.microsoft.com/library/aa393244) class represents an association between a job object and the job object limit settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("CIMWin32a"), Dynamic, UUID("{08E31939-FAAB-4a3b-9B10-50151D1B9D24}"), AMENDMENT]
class Win32_NamedJobObjectLimit : CIM_CollectionSetting
{
  Win32_NamedJobObject             REF Collection;
  Win32_NamedJobObjectLimitSetting REF Setting;
};
```

## Members

The **Win32\_NamedJobObjectLimit** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObjectLimit** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NamedJobObject**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Collection), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

This property is a reference to the instance of a job object.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NamedJobObjectLimitSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Setting), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

This property is a reference to the instance that contains limit settings for the job object.

</dd> </dl>

## Remarks

The **Win32\_NamedJobObjectLimit** class is derived from [**CIM\_CollectionSetting**](https://msdn.microsoft.com/library/aa387216).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipjobj.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipjobj.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_CollectionSetting**](https://msdn.microsoft.com/library/aa387216)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




