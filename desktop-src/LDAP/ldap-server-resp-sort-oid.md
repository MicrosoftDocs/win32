---
title: LDAP\_SERVER\_RESP\_SORT\_OID control code
description: Used by the server to indicate the results of a search function initiated using the LDAP\_SERVER\_SORT\_OID control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 33832380-e1c7-40c2-853d-dee0ee55dee9
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_RESP_SORT_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_RESP_SORT_OID
api_location:
- Winldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_RESP\_SORT\_OID control code

The LDAP\_SERVER\_RESP\_SORT\_OID control is used by the server to indicate the results of a search function initiated using the [LDAP\_SERVER\_SORT\_OID](ldap-server-sort-oid.md) control. This control is returned only by the server and should not be sent to the server by a client application.

The server returns results in the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows.

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_RESP_SORT_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical = FALSE;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_RESP\_SORT\_OID, which is defined as "1.2.840.113556.1.4.474".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a BER-encoded sequence that indicates the results of the sorted search request. For more information, see Remarks below.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Returned as **FALSE**.

</dd> </dl>

## Remarks

The Response Sort control returns the status of a sorted search request previously initiated by using the [LDAP\_SERVER\_SORT\_OID](ldap-server-sort-oid.md) control. The returned value is a BER-encoded OCTET STRING that contains the following sequence data.


```C++
Sequence {
  sortResult      ENUMERATED
  attributeType   attributeDescription (optional)
}
```



Client applications should use the [**ldap\_parse\_result**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_result) and [**ldap\_parse\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_sort_control) functions to parse the result fields of this returned control.

The sortResult enumeration elements are listed in the following table.



| sortResult                                 | Description                                                                        |
|--------------------------------------------|------------------------------------------------------------------------------------|
| success \[0\]<br/>                   | results are sorted<br/>                                                      |
| operationsError \[1\]<br/>           | server internal error<br/>                                                   |
| timeLimitExceeded \[3\]<br/>         | time limit reached before sorting was completed<br/>                         |
| strongAuthRequired \[8\]<br/>        | refused to return sorted results by using a protocol that is not secure<br/> |
| adminLimitExceeded \[11\]<br/>       | too many matching entries for the server to sort<br/>                        |
| noSuchAttribute \[16\]<br/>          | unrecognized attribute type in sort key<br/>                                 |
| inappropriateMatching \[18\]<br/>    | unrecognized or inappropriate matching rule in sort key<br/>                 |
| insufficientAccessRights \[50\]<br/> | refused to return sorted results to this client<br/>                         |
| busy \[51\]<br/>                     | too busy to process<br/>                                                     |
| unwillingToPerform \[53\]<br/>       | unable to sort<br/>                                                          |
| other \[80\]<br/>                    |                                                                                    |



 

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

[**LDAPMessage**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapmsg)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





