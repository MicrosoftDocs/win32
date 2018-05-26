---
title: Win32\_ConnectionShare class
description: The Win32\_ConnectionShare association WMI class relates a shared resource on the computer and the connection made to the shared resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e35831b4-f219-4b0c-b07a-89131424ad5a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ConnectionShare class
- Win32_ConnectionShare class, described
topic_type:
- apiref
api_name:
- Win32_ConnectionShare
- Win32_ConnectionShare.Antecedent
- Win32_ConnectionShare.Dependent
api_location:
- Wmipsess.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_ConnectionShare class

The **Win32\_ConnectionShare** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a shared resource on the computer and the connection made to the shared resource.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("SessionProvider"), AMENDMENT]
class Win32_ConnectionShare : CIM_Dependency
{
  Win32_Share            REF Antecedent;
  Win32_ServerConnection REF Dependent;
};
```

## Members

The **Win32\_ConnectionShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ConnectionShare** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Share**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Antecedent), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the share to which the connection is made.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ServerConnection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Dependent), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the server connection to the shared resource.

</dd> </dl>

## Remarks

The **Win32\_ConnectionShare** class is derived from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

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

 

 





