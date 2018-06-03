---
title: Win32\_SessionConnection class
description: The Win32\_SessionConnection association WMI class represents an association between a session established with the local server, by a user on a remote computer, and the connections that depend on the session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7b28740f-876e-404a-a6b9-dab0bf0808b0
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_SessionConnection class
- Win32_SessionConnection class, described
topic_type:
- apiref
api_name:
- Win32_SessionConnection
- Win32_SessionConnection.Antecedent
- Win32_SessionConnection.Dependent
api_location:
- Wmipsess.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SessionConnection class

The **Win32\_SessionConnection** association [WMI class](https://msdn.microsoft.com/library/aa393244) represents an association between a session established with the local server, by a user on a remote computer, and the connections that depend on the session.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, provider("SessionProvider"), AMENDMENT]
class Win32_SessionConnection : CIM_Dependency
{
  Win32_ServerSession    REF Antecedent;
  Win32_ServerConnection REF Dependent;
};
```

## Members

The **Win32\_SessionConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionConnection** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ServerSession**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Antecedent), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Antecedent property references the session established to connect to the shared resource.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ServerConnection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Dependent), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Dependent property references a connection made to a shared resource on the local server.

</dd> </dl>

## Remarks

The **Win32\_SessionConnection** class is derived from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipsess.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipsess.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





