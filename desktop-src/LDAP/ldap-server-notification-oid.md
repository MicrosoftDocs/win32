---
title: LDAP\_SERVER\_NOTIFICATION\_OID control code
description: Used with an extended LDAP asynchronous search function to register the client to be notified when changes are made to an object in Active Directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 97bc53d1-71e4-4f7b-aaa8-d29e7cd9d731
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_NOTIFICATION_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_NOTIFICATION_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_SERVER\_NOTIFICATION\_OID control code

The LDAP\_SERVER\_NOTIFICATION\_OID control is used with an extended LDAP asynchronous search function to register the client to be notified when changes are made to an object in Active Directory.

To use this control, set the members of the [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_NOTIFICATION_OID;
struct berval ldctl_value = {0, NULL};
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_NOTIFICATION\_OID, defined as "1.2.840.113556.1.4.528".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

No data for this control. In the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure, set **bv\_len** to zero and **bv\_val** to **NULL**.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether LDAP notification is critical to the application.

</dd> </dl>

## Remarks

This control is used with an extended LDAP search function such as [**ldap\_search\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext?branch=master) to register a change notification request of the directory objects that match the search filter specified. The control is part of the SearchRequest and SearchResultDone messages in the control fields of [**LDAPMessage**](/windows/previous-versions/Winldap/ns-winldap-ldapmsg?branch=master). A client can register up to five (5) notification requests with this control.

Notifications are asynchronous operations. The server sends SearchEntry responses, that contain the modified objects, to the client using the [**LDAPMessage**](/windows/previous-versions/Winldap/ns-winldap-ldapmsg?branch=master) ID of the original notification request. Notifications from this control may be canceled using the [**ldap\_abandon**](/windows/previous-versions/Winldap/nf-winldap-ldap_abandon?branch=master) function. For more information about Notifications in Active Directory, see [Change Notifications in Active Directory](https://msdn.microsoft.com/library/aa772153).

Limitations of the Server Notification Control include:

-   The filter, (objectclass = \*), is the only filter allowed on a persistent search.
-   Base, one-level, and subtree searches are allowed, but subtree searches must be rooted on a Naming Context.

Using a filter other than (objectclass =\*) and attempting a subtree level search on a container that is not the root of a Naming Context will return the **UnwillingToPerform (53)** error message.

The user application must have the proper directory service access rights to successfully use this control. The user application must have permission to read the objects that fall within the scope of the search function using this control. Any object that is not accessed with the proper permission will not generate a change notification when its contents are modified.

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

 

 





