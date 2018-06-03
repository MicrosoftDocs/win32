---
title: LDAP\_TTL\_EXTENDED\_OP\_OID control code
description: The LDAP\_TTL\_EXTENDED\_OP\_OID can be present in the supportedExtensions attribute of the rootDSE of an Active Directory server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8b4bf2b7-1c88-4e00-b338-1ee18bab1e6a
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_TTL_EXTENDED_OP_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_TTL_EXTENDED_OP_OID
api_location:
- Winldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_TTL\_EXTENDED\_OP\_OID control code

The LDAP\_TTL\_EXTENDED\_OP\_OID can be present in the supportedExtensions attribute of the rootDSE of an Active Directory server. If present, it indicates that the Active Directory server provides support for dynamic objects as defined in RFC 2589. It can also be sent to an Active Directory server to refresh a specific Dynamic Object that has already been created. For more information about using this feature of Active Directory, see [Dynamic Objects](https://msdn.microsoft.com/library/ms676291).

To use this extended operation, set the arguments of the call to [**ldap\_extended\_operation\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_extended_operation_sa) as shown in the following code example.

``` syntax
LDAP* ld,
PCHAR Oid = LDAP_TTL_EXTENDED_OP_OID,
struct berval* Data,
PLDAPControl* ServerControls = NULL,
PLDAPControl* ClientControls = NULL,
PCHAR* ReturnedOid = NULL,
struct berval** ReturnedData
```

## Members

<dl> <dt>

**ld**
</dt> <dd>

A pointer to the session handle.

</dd> <dt>

**Oid**
</dt> <dd>

A pointer to the LDAP\_TTL\_EXTENDED\_OP\_OID string, defined as "1.3.6.1.4.1.1466.101.119.1".

</dd> <dt>

**Data**
</dt> <dd>

A value that specifies a BER-encoded sequence of parameters that specifies both the dynamic object name and the desired TTL refresh period. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_val** to a pointer to the sequence that contains the dynamic object name and the TTL refresh period, and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ServerControls**
</dt> <dd>

Set to **NULL**.

</dd> <dt>

**ClientControls**
</dt> <dd>

Set to **NULL**.

</dd> <dt>

**ReturnedOid**
</dt> <dd>

Set to **NULL**.

</dd> <dt>

**ReturnedData**
</dt> <dd>

A pointer to a pointer to a berval structure used to hold returned data.

</dd> </dl>

## Remarks

The LDAP\_TTL\_EXTENDED\_OP\_OID is used to refresh an Active Directory dynamic object. For more information about creating and refreshing dynamic objects, see [Dynamic Objects](https://msdn.microsoft.com/library/ms676291).

To refresh a specific dynamic object, a BER-encoded sequence of parameters that specifies the object must be created per RFC 2589 as follows.


```C++
Sequence {
  entryName         OCTET STRING
  requestTtl        INTEGER
}
```



<dl> <dt>

<span id="entryName"></span><span id="entryname"></span><span id="ENTRYNAME"></span>**entryName**
</dt> <dd>

This is an OCTET STRING that specifies the Distinguished Name of the dynamic object. It is encoded in UTF-8 format.

</dd> <dt>

<span id="requestTtl"></span><span id="requestttl"></span><span id="REQUESTTTL"></span>**requestTtl**
</dt> <dd>

This is an INTEGER that expresses, in seconds, the desired TTL (range is from 1 to 31557600) of the dynamic object. Servers are not required to accept this value and may return a different TTL value to the client. Clients must be able to use a returned server-dictated TTL value in place of the one submitted.

</dd> </dl>

If a new TTL value is returned by a server in response to a client's LDAP\_TTL\_EXTENDED\_OP\_OID extended operation request, the value will be returned as a BER-encoded sequence as follows.


```C++
Sequence {
  responseTTL       INTEGER
}
```



<dl> <dt>

<span id="responseTTL"></span><span id="responsettl"></span><span id="RESPONSETTL"></span>**responseTTL**
</dt> <dd>

This is an INTEGER that expresses the server-dictated TTL value in seconds of the dynamic object. It will be equal to or greater than the client-requested value under normal circumstances. However, servers are permitted to reduce a large client-requested TTL value in order to prevent clients from abusing the dynamic extensions. In this later case the minimum value that a server can reduce a TTL value is down to 86400 seconds (24 hours).

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winldap.h</dt> </dl> |



 

 





