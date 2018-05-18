---
Description: 'The Win32\_NamedJobObject&\#32;WMI class represents a kernel object that is used to group processes for controlling the life cycle and resources of the processes within the job object. Only the job objects that are named are instrumented.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '52f3520e-550b-4f96-8c4a-6ae5d2705302'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_NamedJobObject class'
---

# Win32\_NamedJobObject class

The **Win32\_NamedJobObject** [WMI class](https://msdn.microsoft.com/library/aa393244) represents a kernel object that is used to group processes for controlling the life cycle and resources of the processes within the job object. Only the job objects that are named are instrumented.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("NamedJobObjectProv"), UUID("{7552EF7F-7CC8-4022-9049-3B5E1B4B3852}"), AMENDMENT]
class Win32_NamedJobObject : CIM_CollectionOfMSEs
{
  string Caption;
  string Description;
  uint32 BasicUIRestrictions;
  string CollectionID;
};
```

## Members

The **Win32\_NamedJobObject** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObject** class has these properties.

<dl> <dt>

**BasicUIRestrictions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Bitvalues**](https://msdn.microsoft.com/library/aa393650) ("Desktop", "Display Settings", "Exit Windows", "Global Atoms", "Handles", "Read Clipboard", "System Parameters", "Write Clipboard")
</dt> </dl>

Restrictions on a job regarding the user interface.

<dt>

1 (0x1)
</dt> <dd>

Desktop

</dd> <dt>

2 (0x2)
</dt> <dd>

Display Settings

</dd> <dt>

4 (0x4)
</dt> <dd>

Exit Windows

</dd> <dt>

8 (0x8)
</dt> <dd>

Global Atoms

</dd> <dt>

16 (0x10)
</dt> <dd>

Handles

</dd> <dt>

32 (0x20)
</dt> <dd>

Read Clipboard

</dd> <dt>

64 (0x40)
</dt> <dd>

System Parameters

</dd> <dt>

128 (0x80)
</dt> <dd>

Write Clipboard

</dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object.

This property is inherited from [**CIM\_CollectionOfMSEs**](https://msdn.microsoft.com/library/aa387214).

</dd> <dt>

**CollectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("CollectionId")
</dt> </dl>

Number that identifies a job object. Because they are kernel objects, job object names are case sensitive. However, Windows Management Instrumentation (WMI) keys are case insensitive and must be decorated to distinguish case. To indicate a capital letter, precede the letter by using a backslash. For example, "A" and "a" are lowercase and "\\A" and "\\a" are uppercase. This property overrides the **CollectionID** property in [**CIM\_CollectionOfMSEs**](https://msdn.microsoft.com/library/aa387214).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_CollectionOfMSEs**](https://msdn.microsoft.com/library/aa387214).

</dd> </dl>

## Remarks

The **Win32\_NamedJobObject** class is derived from [**CIM\_CollectionOfMSEs**](https://msdn.microsoft.com/library/aa387214).

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

[**CIM\_CollectionOfMSEs**](https://msdn.microsoft.com/library/aa387214)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




