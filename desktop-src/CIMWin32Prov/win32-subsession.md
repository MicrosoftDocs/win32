---
Description: The Win32\_SubSession association defines relationships between sessions where one session is a part of or utilizes another session for example where a Terminal session uses a Logon Session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2269de22-b086-4f71-8b19-bc53e1c88dc7
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SubSession class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_SubSession class

The Win32\_SubSession association defines relationships between sessions where one session is a part of or utilizes another session for example where a Terminal session uses a Logon Session.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class Win32_SubSession : CIM_Dependency
{
  Win32_Session REF Antecedent;
  Win32_Session REF Dependent;
};
```

## Members

The **Win32\_SubSession** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SubSession** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Session**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](wmi.standard_qualifiers) (Antecedent)
</dt> </dl>

A [**Win32\_Session**](win32-session.md) that describes the session that has a subsession.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Session**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](wmi.standard_qualifiers) (Dependent)
</dt> </dl>

A [**Win32\_Session**](win32-session.md) that describes the session that is the subsession.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CimWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Cimwin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 




