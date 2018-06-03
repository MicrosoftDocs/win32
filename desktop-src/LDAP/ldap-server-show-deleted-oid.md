---
title: LDAP\_SERVER\_SHOW\_DELETED\_OID control code
description: Used with an extended LDAP search function to specify that the search results include any deleted objects that match the search filter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dba19178-5bc7-4e9e-a472-8cd75166f108
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_SHOW_DELETED_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_SHOW_DELETED_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_SHOW\_DELETED\_OID control code

The LDAP\_SERVER\_SHOW\_DELETED\_OID control is used with an extended LDAP search function to specify that the search results include any deleted objects that match the search filter.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_SHOW_DELETED_OID;
struct berval ldctl_value = {0, NULL};
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_SHOW\_DELETED\_OID, which is defined as "1.2.840.113556.1.4.417".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

No data for this control. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_len** to zero and **bv\_val** to **NULL**.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the search call is critical to the operation.

</dd> </dl>

## Remarks

The Show Deleted control is used with the extended search functions, such as [**ldap\_search\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext), to view deleted objects along with other objects that match the search filter. When an Active Directory object is deleted, a tombstone of the object is preserved in the tombstone container for a configurable period of time known as the garbage collection interval. To view tombstones using the LDAP functions, specify the Show Deleted control. After the garbage collection interval, a tombstone is permanently deleted and can no longer be viewed using this control or otherwise. The relative distinguished name (RDN) of a tombstone is an identifier constructed from the objectGUID of the deleted object. A tombstone has its **isDeleted** attribute set to **TRUE** and contains only a subset of the object attributes. For more information, see the description of searchFlags in [Characteristics of Attributes](https://msdn.microsoft.com/library/ms675578).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



## See also

<dl> <dt>

[Retrieving Deleted Objects](https://msdn.microsoft.com/library/ms677927)
</dt> </dl>

 

 





