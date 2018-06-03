---
title: LDAP\_SERVER\_PERMISSIVE\_MODIFY\_OID control code
description: Used to modify the behavior of an extended LDAP modify request such as ldap\_modify\_ext.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 42a7da45-d479-4ca2-8a7a-e5331c5b3ee7
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_PERMISSIVE_MODIFY_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_PERMISSIVE_MODIFY_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_PERMISSIVE\_MODIFY\_OID control code

The LDAP\_SERVER\_PERMISSIVE\_MODIFY\_OID control is used to modify the behavior of an extended LDAP modify request such as [**ldap\_modify\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_modify_ext). An LDAP modify request will normally fail if it attempts to add an attribute that already exists, or if it attempts to delete an attribute that does not exist. With this control, as long as the attribute to be added has the same value as the existing attribute, then the modify will succeed. With this control, deletion of an attribute that does not exist will also succeed.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows.

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_PERMISSIVE_MODIFY_OID;
struct berval ldctl_value = {0, NULL};
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_PERMISSIVE\_MODIFY\_OID, defined as "1.2.840.113556.1.4.1413".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

No data for this control. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_len** to zero and **bv\_val** to **NULL**.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether permissive modify is critical to the application.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



 

 





