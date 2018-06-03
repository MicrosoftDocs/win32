---
Description: The Win32\_TokenPrivileges abstract WMI class represents information about a set of privileges for an access token.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae46ccdf-4be4-4eb6-ac50-b08aaa9e7554
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_TokenPrivileges class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_TokenPrivileges class

The **Win32\_TokenPrivileges** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) represents information about a set of privileges for an access token.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{3559D159-47E8-4458-9B7E-5FD16D260B8D}"), AMENDMENT]
class Win32_TokenPrivileges
{
  Win32_LUIDandAttributes Privileges[];
  uint32                  PrivilegeCount;
};
```

## Members

The **Win32\_TokenPrivileges** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TokenPrivileges** class has these properties.

<dl> <dt>

**PrivilegeCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of entries in the **Privilege** array.

</dd> <dt>

**Privileges**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LUIDandAttributes** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A [**Win32\_LUIDandAttributes**](win32-luidandattributes.md) that specifies an array of LUIDs and attributes.

</dd> </dl>

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

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




