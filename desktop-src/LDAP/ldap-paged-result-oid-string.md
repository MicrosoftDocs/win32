---
title: LDAP\_PAGED\_RESULT\_OID\_STRING control code
description: The LDAP\_PAGED\_RESULT\_OID\_STRING control is used internally, with the LDAP paged search API functions, to instruct the server to return the results of a search request in smaller, more manageable packets rather than in one large block.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bd896700-70a9-4568-9f54-8ab56d0eacd8
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_PAGED_RESULT_OID_STRING control code LDAP
topic_type:
- apiref
api_name:
- LDAP_PAGED_RESULT_OID_STRING
api_location:
- Winldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_PAGED\_RESULT\_OID\_STRING control code

The LDAP\_PAGED\_RESULT\_OID\_STRING control is used internally, with the LDAP paged search API functions, to instruct the server to return the results of a search request in smaller, more manageable packets rather than in one large block.

To use this control, format the control contents using the [**ldap\_create\_page\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_create_page_control?branch=master) function, or set the members of the [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure as follows.

``` syntax
PWCHAR ldctl_oid = LDAP_PAGED_RESULT_OID_STRING;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_PAGED\_RESULT\_OID\_STRING, which is defined as "1.2.840.113556.1.4.319"

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a BER-encoded sequence of parameters that enables the application to limit the amount of data returned in a single call. The sequence also includes a "cookie" used for subsequent paged results search calls. In the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure, set **bv\_val** to a pointer to the sequence containing the control and cookie data, and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether paging the results is critical to the application.

</dd> </dl>

## Remarks

An important benefit of using the paged control is that it enables applications to receive result sets which contain more entries than permitted by server defined limits. For example, by default, Active Directory limits search results to a maximum of 1000 entries. Using the paged control with a paged size of &lt; 1000, an application can retrieve the complete set of results (more than 1000) in packet sizes that do not exceed the server limit.

Client applications should use the LDAP API functions, such as [**ldap\_create\_page\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_create_page_control?branch=master), [**ldap\_search\_init\_page**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_init_page?branch=master), [**ldap\_parse\_result**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_result?branch=master), [**ldap\_parse\_page\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_page_control?branch=master), and so on, instead of attempting to create and manipulate this control directly.

If the value of the **ldctl\_value** sequence argument is required to be created manually, the sequence data is formatted as follows.

``` syntax
Sequence {
  pageSize     INTEGER
  Cookie       OCTET STRING
}
```

The following table lists the sequence fields.



| Sequence data           | Description                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **pageSize**<br/> | Specifies the requested page size from the client, or the estimated result set size returned by the server.<br/>                       |
| **Cookie**<br/>   | An opaque Octet String that is implementation specific. Initial creation of this control should be a **NULL** string of 0 length.<br/> |



 

This code example shows how to manually format the sequence data for the first call to an extended LDAP search function.


```C++
LDAPControl lControl;
BerElement *pber = NULL;
PBERVAL pldctrl_value = NULL;
ber_int_t iPageSize = 250;
int success = -1;


// Format and encode the SEQUENCE data in a BerElement.
pber = ber_alloc_t(LBER_USE_DER);
if(pber==NULL) return BER_ALLOC_FAILURE_CODE;
ber_printf(pber,"{io}",iPageSize,NULL,0);

// Transfer the encoded data into a BERVAL.
success = ber_flatten(pber,&amp;pldctrl_value);
if(success == 0)
    ber_free(pber,1);
else
{
    printf("ber_flatten failed");
    // Call an error routine.
}

// Copy the BERVAL data to the LDAPControl structure.
lControl.ldctl_oid = LDAP_PAGED_RESULT_OID_STRING;
lControl.ldctl_iscritical = TRUE;
lControl.ldctl_value.bv_val = new char[pldctrl_value->bv_len];
memcpy(lControl.ldctl_value.bv_val, 
       pldctrl_value->bv_val, pldctrl_value->bv_len);
lControl.ldctl_value.bv_len = pldctrl_value->bv_len;

// Clean up temporary berval.
ber_bvfree(pldctrl_value);

// The LDAPControl data is ready for use in ldap_search_ext()
// or another call.
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winldap.h</dt> </dl> |



## See also

<dl> <dt>

[Data Structures](data-structures.md)
</dt> <dt>

[**LDAPMessage**](/windows/previous-versions/Winldap/ns-winldap-ldapmsg?branch=master)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





