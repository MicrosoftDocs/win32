---
title: LDAP\_CONTROL\_VLVRESPONSE control code
description: Used to pass virtual list view (VLV) data from the server to the client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bd7906bd-9e2d-4941-9a63-3e530cb9583b
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_CONTROL_VLVRESPONSE control code LDAP
topic_type:
- apiref
api_name:
- LDAP_CONTROL_VLVRESPONSE
api_location:
- Winldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_CONTROL\_VLVRESPONSE control code

The LDAP\_CONTROL\_VLVRESPONSE control is used to pass virtual list view (VLV) data from the server to the client.

This control cannot be sent; it can only be received. The [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure will have its members set to the following:

``` syntax
PWCHAR ldctl_oid = LDAP_CONTROL_VLVRESPONSE;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical = FALSE;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_CONTROL\_VLVRESPONSE defined as "2.16.840.1.113730.3.4.10".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Returns a **controlValue** that is an OCTET STRING whose value is the BER-encoded sequence of parameters that the application uses to specify the LDAP\_CONTROL\_VLVRESPONSE control. The [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure returns a pointer in **bv\_val** to the sequence that contains the virtual list view data, and sets **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Returned as **FALSE**.

</dd> </dl>

## Remarks

The **ldctl\_value** field is set to the following BER-encoded sequence.


```C++
Sequence {
  targetPosition         INTEGER (0 .. maxInt),
  contentCount           INTEGER (0 .. maxInt),
  virtualListViewResult  ENUMERATED {
    success (0),
    operationsError (1),
    unwillingToPerform (53),
    insufficientAccessRights (50),
    busy (51),
    timeLimitExceeded (3),
    adminLimitExceeded (11),
    sortControlMissing (60),
    offsetRangeError (61),
    other (80) },
  contextID              OCTET STRING OPTIONAL }
```



The following table lists the sequence fields.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Sequence data</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>targetPosition</strong><br/></td>
<td>Provides the list index position for the target entry.<br/></td>
</tr>
<tr class="even">
<td><strong>contentCount</strong><br/></td>
<td>Provides the server estimate of the current number of entries in the list. Together with the targetPosition field, there is sufficient data for the client to update a list box slider position to match the newly retrieved entries and identify the target entry.<br/> The value returned from this parameter should be used in a subsequent [LDAP_CONTROL_VLVREQUEST](ldap-control-vlvrequest.md) control.<br/></td>
</tr>
<tr class="odd">
<td><strong>virtualListViewResult</strong><br/></td>
<td>Provides the codes commonly returned by the LDAP searchResponse operation. These codes have the same meanings as defined in LDAP 3, but they pertain specifically to the VLV operation. The following codes are used:<br/>
<ul>
<li>success</li>
<li>operationsError</li>
<li>unwillingToPerform</li>
<li>insufficientAccessRights</li>
<li>busy</li>
<li>timeLimitExceeded</li>
<li>adminLimitExceeded</li>
<li>sortControlMissing</li>
<li>offsetRangeError</li>
<li>other</li>
</ul>
For example, the server could exceed an administration limit while processing a SearchRequest with a [LDAP_CONTROL_VLVREQUEST](ldap-control-vlvrequest.md) control. However, the same administration limit would not be exceeded if the same SearchRequest were submitted by the client without the LDAP_CONTROL_VLVREQUEST control. In this case, the client can determine that an administration limit has been exceeded while servicing the VLV request, and it can resubmit the SearchRequest without the LDAP_CONTROL_VLVREQUEST control.<br/> The insufficientAccessRights code means that the server denied the client permission to perform the VLV operation. If the server determines that the results of the search exceed the range provided by the 32-bit offset values, it must return offsetRangeError.<br/></td>
</tr>
<tr class="even">
<td><strong>contextID</strong><br/></td>
<td>Provides a server-defined octet string used to identify this search operation when sending additional requests to the server. If present, the contents of the contextID field should be returned to the server by a client in a subsequent [LDAP_CONTROL_VLVREQUEST](ldap-control-vlvrequest.md) control that pertains to the same list on the same server. Do not pass it back on just any future VLVREQUEST. If the client uses the contextID that the server passed back, it will improve the response time on the next query to the server.<br/></td>
</tr>
</tbody>
</table>



 

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

 

 





