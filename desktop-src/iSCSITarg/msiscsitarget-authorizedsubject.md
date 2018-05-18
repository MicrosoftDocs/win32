---
title: MSISCSITARGET\_AuthorizedSubject class
description: Associates a specific MSISCSITARGET\_AuthorizedPrivilege class with specific identities, roles, or collections of them.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd378758f-a5d7-4405-8e3d-c55825a31181'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_AuthorizedSubject class iSCSI Software Target API", "MSISCSITARGET_AuthorizedSubject class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_AuthorizedSubject
- MSISCSITARGET_AuthorizedSubject.Privilege
- MSISCSITARGET_AuthorizedSubject.PrivilegedElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_AuthorizedSubject class

Associates a specific [**MSISCSITARGET\_AuthorizedPrivilege**](msiscsitarget-authorizedprivilege.md) class with specific identities, roles, or collections of them. You should use this class to associate only identities and roles, or collections of identities and roles to [**MSISCSITARGET\_AuthorizedPrivilege**](msiscsitarget-authorizedprivilege.md) classes.

> \[!Important\]  
> Any permissions that are not explicitly granted to a subject should be denied.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_AuthorizedSubject : CIM_AuthorizedSubject
{
  CIM_AuthorizedPrivilege REF Privilege;
  CIM_ManagedElement      REF PrivilegedElement;
};
```

## Members

The **MSISCSITARGET\_AuthorizedSubject** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_AuthorizedSubject** class has these properties.

<dl> <dt>

**Privilege**
</dt> <dd> <dl> <dt>

Data type: **CIM\_AuthorizedPrivilege**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**CIM\_AuthorizedPrivilege**](cim-authorizedprivilege.md) either granted or denied to an Identity, Role or Collection. Whether the privilege is granted or denied is defined by the inherited property, CIM\_Privilege.PrivilegeGranted.

This property is inherited from [**CIM\_AuthorizedSubject**](cim-authorizedsubject.md).

</dd> <dt>

**PrivilegedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) containing the Subject for which AuthorizedPrivileges are granted or denied. Whether the privilege is granted or denied is defined by the property, CIM\_Privilege.PrivilegeGranted.

This property is inherited from [**CIM\_AuthorizedSubject**](cim-authorizedsubject.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_AuthorizedSubject**](cim-authorizedsubject.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedPrivilege**](msiscsitarget-authorizedprivilege.md)
</dt> </dl>

 

 





