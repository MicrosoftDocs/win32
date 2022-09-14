---
description: The CAPICOM\_CERTIFICATE\_FIND\_TYPE enumeration type defines the type of search criteria used to find specific certificates. This enumeration type was introduced in CAPICOM 2.0.
ms.assetid: d71436e5-d921-4b84-8028-301d8fc4aedb
title: CAPICOM_CERTIFICATE_FIND_TYPE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_CERTIFICATE_FIND_TYPE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_CERTIFICATE\_FIND\_TYPE enumeration

The **CAPICOM\_CERTIFICATE\_FIND\_TYPE** enumeration type defines the type of search criteria used to find specific certificates. This enumeration type was introduced in CAPICOM 2.0.

## Members



| Member                                                | Description                                                                                                                                 | Value |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_CERTIFICATE\_FIND\_SHA1\_HASH**            | Returns certificates matching a specified SHA1 hash.<br/>                                                                             | 0     |
| **CAPICOM\_CERTIFICATE\_FIND\_SUBJECT\_NAME**         | Returns certificates whose subject name exactly or partially matches a specified subject name.<br/>                                   | 1     |
| **CAPICOM\_CERTIFICATE\_FIND\_ISSUER\_NAME**          | Returns certificates whose issuer name exactly or partially matches a specified issuer name.<br/>                                     | 2     |
| **CAPICOM\_CERTIFICATE\_FIND\_ROOT\_NAME**            | Returns certificates whose root subject name exactly or partially matches a specified root subject name.<br/>                         | 3     |
| **CAPICOM\_CERTIFICATE\_FIND\_TEMPLATE\_NAME**        | Returns certificates whose template name matches a specified template name.<br/>                                                      | 4     |
| **CAPICOM\_CERTIFICATE\_FIND\_EXTENSION**             | Returns certificates that have an extension that matches a specified extension.<br/>                                                  | 5     |
| **CAPICOM\_CERTIFICATE\_FIND\_EXTENDED\_PROPERTY**    | Returns certificates that have an extended property whose property identifier matches a specified property identifier.<br/>           | 6     |
| **CAPICOM\_CERTIFICATE\_FIND\_APPLICATION\_POLICY**   | Returns certificates in the store that have either an enhanced key usage extension or property combined with a usage identifier.<br/> | 7     |
| **CAPICOM\_CERTIFICATE\_FIND\_CERTIFICATE\_POLICY**   | Returns certificates containing a specified policy OID.<br/>                                                                          | 8     |
| **CAPICOM\_CERTIFICATE\_FIND\_TIME\_VALID**           | Returns certificates whose time is valid.<br/>                                                                                        | 9     |
| **CAPICOM\_CERTIFICATE\_FIND\_TIME\_NOT\_YET\_VALID** | Returns certificates whose time is not yet valid.<br/>                                                                                | 10    |
| **CAPICOM\_CERTIFICATE\_FIND\_TIME\_EXPIRED**         | Returns certificates whose time has expired.<br/>                                                                                     | 11    |
| **CAPICOM\_CERTIFICATE\_FIND\_KEY\_USAGE**            | Returns certificates containing a key that can be used in the specified manner.<br/>                                                  | 12    |



## Remarks

The **CAPICOM\_CERTIFICATE\_FIND\_TYPE** enumeration type is used by the [**Certificates.Find**](certificates-find.md) method.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




