---
title: LDAP\_SERVER\_LAZY\_COMMIT\_OID control code
description: Used to instruct the server to return the results of a DS modification command, such as add, delete, or replace, after it has been completed in memory, but before it has been committed to disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 315c393e-0179-4281-b3eb-3deb28d0c637
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_LAZY_COMMIT_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_LAZY_COMMIT_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_SERVER\_LAZY\_COMMIT\_OID control code

The LDAP\_SERVER\_LAZY\_COMMIT\_OID control is used to instruct the server to return the results of a DS modification command, such as add, delete, or replace, after it has been completed in memory, but before it has been committed to disk. The server can then return results quickly, and save the data to disk without holding the client.

To use this control, set the members of the [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_LAZY_COMMIT_OID;
struct berval ldctl_value = {0, NULL};
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_LAZY\_COMMIT\_OID, which is defined as "1.2.840.113556.1.4.619".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

No data for this control. In the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure, set **bv\_len** to zero and **bv\_val** to **NULL**.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether LAZY commit is critical to the application.

</dd> </dl>

## Remarks

> \[!Caution\]  
> As with any caching scheme, using this control presents the risk of data loss if the server abnormally terminates, due to a power loss or other unrecoverable error, before the requested changes are written to disk.

 

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

[**LDAPMessage**](/windows/previous-versions/Winldap/ns-winldap-ldapmsg?branch=master)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





