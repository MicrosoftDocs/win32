---
title: LDAP\_SERVER\_DOMAIN\_SCOPE\_OID control code
description: The LDAP\_SERVER\_DOMAIN\_SCOPE\_OID control is used to instruct the LDAP server not to generate any referrals when completing a request.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4179f876-3bf5-4114-9630-ffd3d28ac9d7
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_DOMAIN_SCOPE_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_DOMAIN_SCOPE_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_DOMAIN\_SCOPE\_OID control code

The LDAP\_SERVER\_DOMAIN\_SCOPE\_OID control is used to instruct the LDAP server not to generate any referrals when completing a request. This control also limits any search using it to a single naming context.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_DOMAIN_SCOPE_OID;
struct berval ldctl_value = {0, NULL};
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_DOMAIN\_SCOPE\_OID, which is defined as "1.2.840.113556.1.4.1339".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

No data for this control. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_len** to zero and **bv\_val** to **NULL**.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the referral limitation is critical to your application.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



 

 





