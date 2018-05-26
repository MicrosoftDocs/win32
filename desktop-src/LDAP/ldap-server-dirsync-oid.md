---
title: LDAP\_SERVER\_DIRSYNC\_OID control code
description: Enables an application to search the directory for objects changed from a previous state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4cb5809a-61c7-41a1-8042-87909c26aa89
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_DIRSYNC_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_DIRSYNC_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_SERVER\_DIRSYNC\_OID control code

The LDAP\_SERVER\_DIRSYNC\_OID control enables an application to search the directory for objects changed from a previous state. It is also used with the extended LDAP search functions such as [**ldap\_search\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext?branch=master).

To use this control, set the members of the [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_DIRSYNC_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical = TRUE;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_DIRSYNC\_OID, defined as "1.2.840.113556.1.4.841".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a BER-encoded sequence of parameters that enables the application to limit the amount of data to be returned in a single call. The sequence also includes a "cookie" used for subsequent search calls. In the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure, set **bv\_val** to a pointer to the sequence that contains the control and cookie data and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

**TRUE**

</dd> </dl>

## Remarks

The LDAP\_SERVER\_DIRSYNC\_OID control is used with the extended search functions, such as [**ldap\_search\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext?branch=master), to search a directory for objects changed since a previous request. This control must be exclusively used with a **SearchRequest** message and is ignored if used otherwise. However, if the criticality field is set to **TRUE** and the control is used with other than the **SearchRequest** message, the request fails and returns an **UnsupportedCriticalExtension** error.

On the first call to an extended LDAP search function that uses this control, the **ldctl\_value** is a BER-encoded version of the following.


```C++
Sequence {
  Flags                INTEGER
  maxAttributeCount    INTEGER
  Cookie               OCTET STRING
}
```



<dl> <dt>

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>**Flags**
</dt> <dd>

Contains optional flags for use with the LDAP\_SERVER\_DIRSYNC\_OID control. This can be zero or a combination of one or more of the values listed in the following list.



| Value                                      | Description                                                                                                                                                                                                                                         |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LDAP\_DIRSYNC\_OBJECT\_SECURITY**        | **Windows Server 2003:  **<br/>                                                                                                                                                                                                               |
| **LDAP\_DIRSYNC\_ANCESTORS\_FIRST\_ORDER** | Return parent objects before child objects, when parent objects would otherwise appear later in the replication stream.<br/>                                                                                                                  |
| **LDAP\_DIRSYNC\_PUBLIC\_DATA\_ONLY**      | Do not return private data in the search results.<br/>                                                                                                                                                                                        |
| **LDAP\_DIRSYNC\_INCREMENTAL\_VALUES**     | **Windows Server 2003:** If this flag is not present, all of the values, up to a server-specified limit, in a multi-valued attribute are returned when any value changes. If this flag is present, only the changed values are returned.<br/> |



 

</dd> <dt>

<span id="maxAttributeCount"></span><span id="maxattributecount"></span><span id="MAXATTRIBUTECOUNT"></span>**maxAttributeCount**
</dt> <dd>

Specifies the maximum number of bytes to return, subject to server limits.

The minimum value accepted in this field is 0x100000. This minimum value is used if a lower value is specified in this field.

The maximum value is the number of bytes it takes to accommodate the number of objects specified in MaxPageSize setting in the [lDAPAdminLimits](https://msdn.microsoft.com/library/windows/desktop/ms676827.aspx) attribute, which is 1000 objects by default. This maximum limit is used if a larger value is specified in this field.

</dd> <dt>

<span id="Cookie"></span><span id="cookie"></span><span id="COOKIE"></span>**Cookie**
</dt> <dd>

An opaque Octet String that is implementation specific. It is updated during each SearchRequest by the directory and enables the DirSync control to incrementally read changes from the directory. Initial creation of this control should be a **NULL** string of 0 length.

</dd> </dl>

The result of a search with the LDAP\_SERVER\_DIRSYNC\_OID control is an [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure that contains a BER-encoded version of the following data in the **ldctl\_value** member.


```C++
Sequence {
  Flag                INTEGER
  maxAttributeCount   INTEGER
  Cookie              OCTET STRING
}
```



<dl> <dt>

<span id="Flag"></span><span id="flag"></span><span id="FLAG"></span>**Flag**
</dt> <dd>

Contains a nonzero value if there is more data to retrieve or zero if there is no more data to retrieve. If this member contains a nonzero value, a subsequent search should be performed with the **Cookie** of this data to retrieve the next block of results.

</dd> <dt>

<span id="maxAttributeCount"></span><span id="maxattributecount"></span><span id="MAXATTRIBUTECOUNT"></span>**maxAttributeCount**
</dt> <dd>

Specifies the maximum number of bytes to return, subject to server limits.

The minimum value accepted in this field is 0x100000. This minimum value is used if a lower value is specified in this field.

The maximum value is the number of bytes it takes to accommodate the number of objects specified in MaxPageSize setting in the [lDAPAdminLimits](https://msdn.microsoft.com/library/windows/desktop/ms676827.aspx) attribute, which is 1000 objects by default. This maximum limit is used if a larger value is specified in this field.

</dd> <dt>

<span id="Cookie"></span><span id="cookie"></span><span id="COOKIE"></span>**Cookie**
</dt> <dd>

Contain an opaque Octet string that is implementation specific. This value is returned by the server for use in subsequent searches by the client.

</dd> </dl>

Subsequent calls to the LDAP extended search functions should pass the returned **Cookie** data back in order to return any additional search results as indicated by the **Flag** data.

For more information about specific access rights required to use this control with an Active Directory server, see [Polling\_for\_Changes\_Using\_the\_DirSync\_Control](https://msdn.microsoft.com/library/ms677626).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



 

 





