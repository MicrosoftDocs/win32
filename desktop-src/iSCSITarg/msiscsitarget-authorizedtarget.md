---
title: MSISCSITARGET\_AuthorizedTarget class
description: An association used to tie the MSISCSITARGET\_AuthorizedPrivilege of an identity or role to specific target resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd20e2bac-c2a5-46a8-86dc-31a902605c02'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_AuthorizedTarget class iSCSI Software Target API", "MSISCSITARGET_AuthorizedTarget class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_AuthorizedTarget
- MSISCSITARGET_AuthorizedTarget.Privilege
- MSISCSITARGET_AuthorizedTarget.TargetElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_AuthorizedTarget class

An association used to tie the [**MSISCSITARGET\_AuthorizedPrivilege**](msiscsitarget-authorizedprivilege.md) of an identity or role to specific target resources.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_AuthorizedTarget : CIM_AuthorizedTarget
{
  CIM_AuthorizedPrivilege REF Privilege;
  CIM_ManagedElement      REF TargetElement;
};
```

## Members

The **MSISCSITARGET\_AuthorizedTarget** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_AuthorizedTarget** class has these properties.

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

This property is inherited from [**CIM\_AuthorizedTarget**](cim-authorizedtarget.md).

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

This property is inherited from [**CIM\_AuthorizedTarget**](cim-authorizedtarget.md).

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

[**CIM\_AuthorizedTarget**](cim-authorizedtarget.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedPrivilege**](msiscsitarget-authorizedprivilege.md)
</dt> </dl>

 

 





