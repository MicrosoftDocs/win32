---
title: LDAP\_SERVER\_TREE\_DELETE\_OID control code
description: Used with an extended LDAP delete function to delete an entire subtree in the directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b47a0f40-7191-40a5-a914-6c4fa78df8cb
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_TREE_DELETE_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_TREE_DELETE_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_TREE\_DELETE\_OID control code

The LDAP\_SERVER\_TREE\_DELETE\_OID control is used with an extended LDAP delete function to delete an entire subtree in the directory.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows.

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_TREE_DELETE_OID;
struct berval ldctl_value = {0, NULL};
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_TREE\_DELETE\_OID, which is defined as "1.2.840.113556.1.4.805".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

No data for this control. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_len** to zero and **bv\_val** to **NULL**.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the operation is critical to your application.

</dd> </dl>

## Remarks

The Tree Delete control is used with the extended delete functions, such as [**ldap\_delete\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_delete_ext), to delete an entire directory subtree. This control must be exclusively used with the LDAP **DelRequest** message and will be ignored if used otherwise. However, if the criticality field is set to **TRUE** and the control is used with other than the **DelRequest** message, the request will fail and return an **LDAP\_UNAVAILABLE\_CRIT\_EXTENSION** error. Server authentication of proper user permissions before completing the operation is required.

### Error Messages

<dl> <dt>

<span id="InsufficientAccessRights__50_"></span><span id="insufficientaccessrights__50_"></span><span id="INSUFFICIENTACCESSRIGHTS__50_"></span>**InsufficientAccessRights** (50)
</dt> <dd>

The authenticated user does not possess the proper permissions to exercise this control.

</dd> <dt>

<span id="UnwillingToPerform__53_"></span><span id="unwillingtoperform__53_"></span><span id="UNWILLINGTOPERFORM__53_"></span>**UnwillingToPerform** (53)
</dt> <dd>

The server is not the authority for the selected tree or the container contains platform specific restraints against deletion.

</dd> <dt>

<span id="AdminLimitExceeded__11_"></span><span id="adminlimitexceeded__11_"></span><span id="ADMINLIMITEXCEEDED__11_"></span>**AdminLimitExceeded** (11)
</dt> <dd>

The limit of the number of objects that can be deleted in one operation is exceeded. However, all objects processed up to the limit will be deleted. The **DelRequest** with the Tree Delete control may be resubmitted until a success response is received.

</dd> </dl>

If a Tree Delete control request fails, it may be retried with no adverse effects.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



## See also

<dl> <dt>

[Data Structures](data-structures.md)
</dt> <dt>

[**LDAPMessage**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapmsg)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





