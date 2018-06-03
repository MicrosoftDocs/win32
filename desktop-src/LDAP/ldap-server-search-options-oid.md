---
title: LDAP\_SERVER\_SEARCH\_OPTIONS\_OID control code
description: Used to pass flags to the server to control various search behaviors.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b6cb2c8a-b278-4876-8b18-a877ade01c0d
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_SEARCH_OPTIONS_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_SEARCH_OPTIONS_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_SEARCH\_OPTIONS\_OID control code

The LDAP\_SERVER\_SEARCH\_OPTIONS\_OID control is used to pass flags to the server to control various search behaviors.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_SEARCH_OPTIONS_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_SEARCH\_OPTIONS\_OID, which is defined as "1.2.840.113556.1.4.1340".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a BER-encoded sequence of parameters that enables the application to specify various search flags. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_val** to a pointer to the sequence that contains the flag data and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the search call is critical to the operation.

</dd> </dl>

## Remarks

The Search Options control enables the client to pass flags to control various search behaviors. The **ldctl\_value** field is set to the following BER-encoded sequence.


```C++
Sequence {
  Flags    INTEGER
}
```



The [**ber\_printf**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_printf) routine is used to create the sequence data. The flags portion contains the search options to include, and can contain any of the bit flags listed in the following table.



| Sequence data                                      | Description                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SERVER\_SEARCH\_FLAG\_DOMAIN\_SCOPE**<br/> | Prevents referrals from being generated when the search results are returned. This performs the same function as the [LDAP\_SERVER\_DOMAIN\_SCOPE\_OID](ldap-server-domain-scope-oid.md) control.<br/>                                                                                                                |
| **SERVER\_SEARCH\_FLAG\_PHANTOM\_ROOT**<br/> | Instructs the server to search all NCs that are subordinate to the search base. This will cause the search to be executed over all NCs held on the DC that are subordinate than the search base. This also enables search bases like dc=com, which would cause the server to search all of the NCs that it holds.<br/> |



 

The following example shows how to format the sequence data for the call to an extended LDAP search function.


```C++
LDAPControl lControl;
BerElement *pber = NULL;
PBERVAL pldctrl_value = NULL;
ber_int_t iSearchFlags = SERVER_SEARCH_FLAG_DOMAIN_SCOPE;
int success = -1;


// Format and encode the SEQUENCE data in a BerElement.
pber = ber_alloc_t(LBER_USE_DER);
if(pber==NULL) return BER_ALLOC_FAILURE_CODE;
ber_printf(pber,"{i}",iSearchFlags);

// Transfer the encoded data into a BERVAL.
success = ber_flatten(pber,&amp;pldctrl_value);
if(success == 0)
    ber_free(pber,1);
else
{
    printf("ber_flatten failed");
    // Call error handler here.
}

// Copy the BERVAL data to the LDAPControl structure.
lControl.ldctl_oid = LDAP_SERVER_SEARCH_OPTIONS_OID;
lControl.ldctl_iscritical = TRUE;
lControl.ldctl_value.bv_val = new char[pldctrl_value->bv_len];
memcpy(lControl.ldctl_value.bv_val, 
       pldctrl_value->bv_val, pldctrl_value->bv_len);
lControl.ldctl_value.bv_len = pldctrl_value->bv_len;

// Cleanup temporary berval.
ber_bvfree(pldctrl_value);

// The LDAPControl data is ready for use in ldap_search_ext()
// or other call...
```



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

 

 





