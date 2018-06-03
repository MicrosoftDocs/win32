---
title: LDAP\_CONTROL\_VLVREQUEST control code
description: Used to request virtual list view support from the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9f00ca19-544e-4616-a70a-e7e62fa84f53
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_CONTROL_VLVREQUEST control code LDAP
topic_type:
- apiref
api_name:
- LDAP_CONTROL_VLVREQUEST
api_location:
- Winldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_CONTROL\_VLVREQUEST control code

The LDAP\_CONTROL\_VLVREQUEST control is used to request virtual list view support from the server.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_CONTROL_VLVREQUEST;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_CONTROL\_VLVREQUEST which is defined as "2.16.840.1.113730.3.4.9".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a **controlValue** that is an OCTET string whose value is a BER-encoded sequence of parameters that the application uses to specify the LDAP\_CONTROL\_VLVREQUEST control. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_val** to a pointer to the sequence that contains the virtual list view data, and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the search call is critical to your application.

</dd> </dl>

## Remarks

If this control is included in a SearchRequest message, a server-side sorting request control must also be present in the message. The **ldctl\_value** field is set to the following BER-encoded sequence.


```C++
Sequence {
  beforeCount  INTEGER (0..maxInt),
  afterCount   INTEGER (0..maxInt),
  CHOICE {
    byoffset [0]            SEQUENCE {
      offset                  INTEGER (0 .. maxInt),
      contentCount            INTEGER (0 .. maxInt) },
    greaterThanOrEqual [1]  AssertionValue },
  contextID              OCTET STRING OPTIONAL }
```



The following table lists the sequence fields.



| Sequence data                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **beforeCount**<br/>                 | Indicates the number of entries before the target entry that the client requests the server to send.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **afterCount**<br/>                  | Indicates the number of entries after the target entry that the client requests the server to send.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **offset** and **contentCount**<br/> | Identifies the target entry. For more information, see [**LDAPVLVInfo**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapvlvinfo).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **greaterThanOrEqual**<br/>          | An attribute assertion value defined in LDAP 3. If present, this value is used to determine the target entry by comparing it to the values of the attribute specified in the **sk\_attrtype** member of the [**LDAPSortKey**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapsortkeya) structure. The first list entry that has a value that is more than the value is the target entry. When the sort order is reversed, using the **sk\_reverseorder** member of the **LDAPSortKey** structure, then to be the target entry, this value must be less than or equal to the value of the attribute specified by **sk\_attrtype**.<br/> |
| **contextID**<br/>                   | If present, this field contains the context ID for the session sent by the server in the last [LDAP\_CONTROL\_VLVRESPONSE](ldap-control-vlvresponse.md) control. Because the context ID is valid only on the server that sent it, the client should never submit a context ID received from another connection, a closed connection, or a different server.<br/>                                                                                                                                                                                                                              |



 

Use the [**ldap\_create\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_create_sort_control) function to create a sort control to pass to the server along with the LDAP\_CONTROL\_VLVREQUEST control, instead of attempting to format this control manually.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winldap.h</dt> </dl> |



## See also

<dl> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





