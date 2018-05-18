---
title: CIM\_AuthorizedTarget class
description: CIM\_AuthorizedTarget is an association used to tie an Identity's or Role's AuthorizedPrivileges to specific target resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0920cf55-da51-4664-a2e7-fe535f71d1bb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_AuthorizedTarget class iSCSI Software Target API", "CIM_AuthorizedTarget class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_AuthorizedTarget
- CIM_AuthorizedTarget.Privilege
- CIM_AuthorizedTarget.TargetElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_AuthorizedTarget class

CIM\_AuthorizedTarget is an association used to tie an Identity's or Role's AuthorizedPrivileges to specific target resources.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Version("2.8.0"), UMLPackagePath("CIM::User::Privilege")]
class CIM_AuthorizedTarget
{
  CIM_AuthorizedPrivilege REF Privilege;
  CIM_ManagedElement      REF TargetElement;
};
```

## Members

The **CIM\_AuthorizedTarget** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AuthorizedTarget** class has these properties.

<dl> <dt>

**Privilege**
</dt> <dd> <dl> <dt>

Data type: **CIM\_AuthorizedPrivilege**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**CIM\_AuthorizedPrivilege**](cim-authorizedprivilege.md) affecting the target resource.

</dd> <dt>

**TargetElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) containing the target set of resources to which the AuthorizedPrivilege applies.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





