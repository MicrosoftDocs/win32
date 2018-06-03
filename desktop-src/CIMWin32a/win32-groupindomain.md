---
title: Win32\_GroupInDomain class
description: The Win32\_GroupInDomain association WMI class identifies the group accounts associated with a Windows domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0a420ad1-301b-4e92-a05b-afb896c30e8c
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_GroupInDomain class
- Win32_GroupInDomain class, described
topic_type:
- apiref
api_name:
- Win32_GroupInDomain
- Win32_GroupInDomain.GroupComponent
- Win32_GroupInDomain.PartComponent
api_location:
- Wmipcima.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_GroupInDomain class

The **Win32\_GroupInDomain** association [WMI class](https://msdn.microsoft.com/library/aa393244) identifies the group accounts associated with a Windows domain.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32a"), UUID("C1717231-5F16-4AE6-966F-6CA856B7AAF6"), AMENDMENT]
class Win32_GroupInDomain : CIM_Component
{
  Win32_NTDomain REF GroupComponent;
  Win32_Group    REF PartComponent;
};
```

## Members

The **Win32\_GroupInDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_GroupInDomain** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NTDomain**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (GroupComponent), [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_NTDomain")
</dt> </dl>

Reference to the instance that represents the parent element in the association. This property is inherited from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Group**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (PartComponent), [**key**](https://msdn.microsoft.com/library/aa392157), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_Group")
</dt> </dl>

Reference to the instance that represents the child element in the association. This property is inherited from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

</dd> </dl>

## Remarks

The **Win32\_GroupInDomain** class is derived from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](https://msdn.microsoft.com/library/aa387218)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





