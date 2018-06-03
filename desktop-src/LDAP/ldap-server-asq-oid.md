---
title: LDAP\_SERVER\_ASQ\_OID control code
description: Used with an extended LDAP search function to force the query to be based on a specific DN-valued attribute.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: eaaa739a-7982-49d3-9559-2686fa2ce13c
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_ASQ_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_ASQ_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_ASQ\_OID control code

The LDAP\_SERVER\_ASQ\_OID control is used with an extended LDAP search function to force the query to be based on a specific DN-valued attribute. Only one source attribute can be specified with this control and the search request is limited to base object scoped queries.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows.

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_ASQ_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

Pointer to a wide, null-terminated string, LDAP\_SERVER\_ASQ\_OID, defined as "1.2.840.113556.1.4.1504".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies the DN name of the desired attribute used to base the search query on. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_val** to a pointer to a BER-encoded sequence that contains the attribute DN name in UTF-8 format, and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

When this control is returned by the server, the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure contains a BER-encoded enumeration that indicates the status of the search results. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the search results call is critical to your application.

</dd> </dl>

## Remarks

The Attribute Scoped Query (ASQ) control is used with the extended search functions, such as [**ldap\_search\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext), to set the search base to the specified attribute. This control must be exclusively used with a SearchRequest message and is ignored if used otherwise. However, if the criticality field is set to **TRUE** and the control is used with other than the SearchRequest message, the request fails and returns an UnsupportedCriticalExtension error:

The **ldctl\_value** field in the searchRequest message is set to the following BER-encoded sequence:


```C++
Sequence {
  sourceAttribute   OCTET STRING
}
```



The [**ber\_printf**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_printf) function is used to create the sequence data. The *sourceAttribute* field is a UTF-8 string that contains the DN name of the attribute the search request is based on:

The **ldctl\_value** in the SearchResponse message is an Octet String and wraps the BER-encoded version of the following.


```C++
Sequence {
  searchResults    ENUM
}
```



The *searchResult* enumeration is as listed in the following table.



| *searchResult*                           | Description                                                                                                  |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| success \[0\]<br/>                 | Search results are returned for all referenced objects.<br/>                                           |
| invalidAttributeSyntax \[21\]<br/> | Value of the attribute specified for the search are not a proper DN value and cannot be resolved.<br/> |
| unwillingToPerform \[53\]<br/>     | The search scope was not set to base object.<br/>                                                      |
| affectsMultipleDSAs \[71\]<br/>    | Partial results were returned, but not all data was available to the local server.<br/>                |



 

The search results consist of each value of the multi-value DN-valued attribute returned as a result entry with all of the attributes specified in the attribute list of the search request. If any of the attribute values in the search result are not available on the local DSA, the search results include all of the attributes that are locally available, and the *searchResult* return value is set to the affectsMultipleDSAs error code to indicate that some data that might be otherwise available is not present in the results.

> [!Note]  
> For more information about using attribute scoped queries with Active Directory servers, see [Performing an Attribute Scoped Query](https://msdn.microsoft.com/library/aa746418).

 

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



## See also

<dl> <dt>

[**ldap\_search\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> <dt>

[Performing an Attribute Scoped Query](https://msdn.microsoft.com/library/aa746418)
</dt> </dl>

 

 





