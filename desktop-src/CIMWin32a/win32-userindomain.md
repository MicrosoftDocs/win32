---
title: Win32\_UserInDomain class
description: The Win32\_UserInDomain association WMI class relates a user account and a Windows domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2e4a8333-b6bf-4555-bb89-e2246ca392ef'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_UserInDomain class", "Win32_UserInDomain class, described"]
topic_type:
- apiref
api_name:
- Win32_UserInDomain
- Win32_UserInDomain.GroupComponent
- Win32_UserInDomain.PartComponent
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# Win32\_UserInDomain class

The **Win32\_UserInDomain** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a user account and a Windows domain.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32a"), UUID("B38813CF-0673-495C-A12F-384D47BDF1ED"), AMENDMENT]
class Win32_UserInDomain : CIM_Component
{
  Win32_NTDomain    REF GroupComponent;
  Win32_UserAccount REF PartComponent;
};
```

## Members

The **Win32\_UserInDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_UserInDomain** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NTDomain**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (GroupComponent), [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_NTDomain")
</dt> </dl>

Reference to the instance that represents the domain in which the user accounts exist. This property is inherited from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_UserAccount**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (PartComponent), [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_UserAccount")
</dt> </dl>

Reference to the instance that represents the user accounts that exist in the domain. This property is inherited from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

</dd> </dl>

## Remarks

The **Win32\_UserInDomain** class is derived from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](https://msdn.microsoft.com/library/aa387218)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





