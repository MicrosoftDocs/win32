---
title: LDAP\_SERVER\_VERIFY\_NAME\_OID control code
description: Used with extended LDAP add and modify requests to instruct the DC accepting the update which DC it should verify with, the existence of any DN attribute values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'bb2f605a-2fb0-4e5c-9b26-edeace202c58'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["LDAP_SERVER_VERIFY_NAME_OID control code LDAP"]
topic_type:
- apiref
api_name:
- LDAP_SERVER_VERIFY_NAME_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
---

# LDAP\_SERVER\_VERIFY\_NAME\_OID control code

The LDAP\_SERVER\_VERIFY\_NAME\_OID control is used with extended LDAP add and modify requests to instruct the DC accepting the update which DC it should verify with, the existence of any DN attribute values.

To use this control, set the members of the [**LDAPControl**](ldapcontrol.md) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_VERIFY_NAME_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

A pointer to a wide, null-terminated string, LDAP\_SERVER\_VERIFY\_NAME\_OID, which is defined as "1.2.840.113556.1.4.1338".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a BER-encoded sequence of parameters that enables the application to specify a server to verify the existence of an object. In the [**berval**](berval.md) structure, set **bv\_val** to a pointer to the sequence that contains the flag and server name data and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the extended search function is critical to your application.

</dd> </dl>

## Remarks

The Verify Name control is used with [**ldap\_modify\_ext**](ldap-modify-ext.md) or [**ldap\_add\_ext**](ldap-add-ext.md) to specify the specific server used to verify the existence of an object. The **ldctl\_value** field is set to the following BER-encoded sequence:


```C++
Sequence {
  Flags        INTEGER
  ServerName   OCTET STRING \\Unicode server string
}
```



The [**ber\_printf**](ber-printf.md) function is used to create the sequence data. The flags portion is set to 0, and the *ServerName* is a Unicode string that contains the fully qualified DNS name of the server to contact for verification.

When a DN valued attribute is updated with new values, the DC on which the update occurs verifies that an object with the new DN exists somewhere in the forest. The DC will first verify that the object is held locally, and failing that, the DC will find a GC and ask the GC if it knows about an object with the new DN.

Applications will sometimes need to create an object and at the same time update an attribute on another existing object to add a reference to the newly created object. If both object are on same DC, the application can create the new object and then modify the second object attribute, adding a reference to the first object, without having to consider replication update times.

However, if the two objects are in different domains and therefore held on two different DCs, when the application attempts to modify the attribute of the second object to add a reference to the first newly created object, it is impossible for the application to recognize that sufficient time has passed for the newly created object to replicate to the GC used by the second object. The LDAP\_SERVER\_VERIFY\_NAME\_OID control enables the application to specify the DN of the newly created object so the verification, performed by the attribute update call of the second object, does not fail due to replication update lag.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



## See also

<dl> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





