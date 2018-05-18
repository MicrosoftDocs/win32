---
title: CIM\_AuthorizedSubject class
description: CIM\_AuthorizedSubject is an association used to tie specific AuthorizedPrivileges to specific subjects (i.e., Identities, Roles or Collections of these).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2bc93476-c42f-4054-a2a6-76bf7a5cd1e9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_AuthorizedSubject class iSCSI Software Target API", "CIM_AuthorizedSubject class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_AuthorizedSubject
- CIM_AuthorizedSubject.Privilege
- CIM_AuthorizedSubject.PrivilegedElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_AuthorizedSubject class

CIM\_AuthorizedSubject is an association used to tie specific AuthorizedPrivileges to specific subjects (i.e., Identities, Roles or Collections of these). At this time, only Identities and Roles (or Collections of Identities and Roles) should be associated to AuthorizedPrivileges using this relationship. Note that any Privileges not explicitly granted to a subject, SHOULD be denied.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Version("2.8.0"), UMLPackagePath("CIM::User::Privilege")]
class CIM_AuthorizedSubject
{
  CIM_AuthorizedPrivilege REF Privilege;
  CIM_ManagedElement      REF PrivilegedElement;
};
```

## Members

The **CIM\_AuthorizedSubject** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AuthorizedSubject** class has these properties.

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

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





