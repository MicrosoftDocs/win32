---
title: Data Type Mapping between Active Directory and LDAP
description: The following table maps the friendly syntax name to the corresponding LDAP syntax OID and ADSTYPEENUM value.
ms.assetid: 07952de0-0389-473a-84ca-b5f35fdc5b1f
ms.tgt_platform: multiple
keywords:
- data type mapping between Active Directory and LDAP ADSI
- LDAP service provider ADSI , data type mapping between Active Directory and LDAP
ms.topic: article
ms.date: 05/31/2018
---

# Data Type Mapping between Active Directory and LDAP

The following table maps the friendly syntax name to the corresponding LDAP syntax OID and [**ADSTYPEENUM**](/windows/win32/api/iads/ne-iads-adstypeenum) value.



| Friendly syntax name              | LDAP syntax OID               | ADSTYPEENUM data type                 |
|-----------------------------------|-------------------------------|---------------------------------------|
| AccessPointDN                     | 1.3.6.1.4.1.1466.115.121.1.2  | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| AttributeTypeDescription          | 1.3.6.1.4.1.1466.115.121.1.3  | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| Audio                             | 1.3.6.1.4.1.1466.115.121.1.4  | **ADSTYPE\_OCTET\_STRING**            |
| Binary                            | 1.3.6.1.4.1.1466.115.121.1.5  | **ADSTYPE\_OCTET\_STRING**            |
| BitString                         | 1.3.6.1.4.1.1466.115.121.1.6  | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| Boolean                           | 1.3.6.1.4.1.1466.115.121.1.7  | **ADSTYPE\_BOOLEAN**                  |
| CaseExactString                   | 1.2.840.113556.1.4.1362       | **ADSTYPE\_CASE\_EXACT\_STRING**      |
| CaseIgnoreString                  | 1.2.840.113556.1.4.1221       | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| Certificate                       | 1.3.6.1.4.1.1466.115.121.1.8  | **ADSTYPE\_OCTET\_STRING**            |
| CertificateList                   | 1.3.6.1.4.1.1466.115.121.1.9  | **ADSTYPE\_OCTET\_STRING**            |
| CertificatePair                   | 1.3.6.1.4.1.1466.115.121.1.10 | **ADSTYPE\_OCTET\_STRING**            |
| Country/Region                    | 1.3.6.1.4.1.1466.115.121.1.11 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| DataQualitySyntax                 | 1.3.6.1.4.1.1466.115.121.1.13 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| DeliveryMethod                    | 1.3.6.1.4.1.1466.115.121.1.14 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| DirectoryString                   | 1.3.6.1.4.1.1466.115.121.1.15 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| DN                                | 1.3.6.1.4.1.1466.115.121.1.12 | **ADSTYPE\_DN\_STRING**               |
| DSAQualitySyntax                  | 1.3.6.1.4.1.1466.115.121.1.19 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| EnhancedGuide                     | 1.3.6.1.4.1.1466.115.121.1.21 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| FacsimileTelephoneNumber          | 1.3.6.1.4.1.1466.115.121.1.22 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| Fax                               | 1.3.6.1.4.1.1466.115.121.1.23 | **ADSTYPE\_OCTET\_STRING**            |
| GeneralizedTime                   | 1.3.6.1.4.1.1466.115.121.1.24 | **ADSTYPE\_UTC\_TIME**                |
| Time (only site server does this) | 1.3.6.1.4.1.1466.115.121.1.24 | **ADSTYPE\_UTC\_TIME**                |
| Guide                             | 1.3.6.1.4.1.1466.115.121.1.25 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| IA5String                         | 1.3.6.1.4.1.1466.115.121.1.26 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| INTEGER                           | 1.3.6.1.4.1.1466.115.121.1.27 | **ADSTYPE\_INTEGER**                  |
| INTEGER8 (not in LDAP, NTDS)      | 1.2.840.113556.1.4.906        | **ADSTYPE\_LARGE\_INTEGER**           |
| JPEG                              | 1.3.6.1.4.1.1466.115.121.1.28 | **ADSTYPE\_OCTET\_STRING**            |
| MailPreference                    | 1.3.6.1.4.1.1466.115.121.1.32 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| NameAndOptionalUID                | 1.3.6.1.4.1.1466.115.121.1.34 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| NumericString                     | 1.3.6.1.4.1.1466.115.121.1.36 | **ADSTYPE\_NUMERIC\_STRING**          |
| ObjectClassDescription            | 1.3.6.1.4.1.1466.115.121.1.37 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| OctetString (not in RFC)          | 1.3.6.1.4.1.1466.115.121.1.40 | **ADSTYPE\_OCTET\_STRING**            |
| OID                               | 1.3.6.1.4.1.1466.115.121.1.38 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| ORName                            | 1.2.840.113556.1.4.1221       | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| OtherMailbox                      | 1.3.6.1.4.1.1466.115.121.1.39 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| PostalAddress                     | 1.3.6.1.4.1.1466.115.121.1.41 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| PresentationAddress               | 1.3.6.1.4.1.1466.115.121.1.43 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| PrintableString                   | 1.3.6.1.4.1.1466.115.121.1.44 | **ADSTYPE\_PRINTABLE\_STRING**        |
| ObjectSecurityDescriptor          | 1.2.840.113556.1.4.907        | **ADSTYPE\_NT\_SECURITY\_DESCRIPTOR** |
| TelephoneNumber                   | 1.3.6.1.4.1.1466.115.121.1.50 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| TeletexTerminalIdentifier         | 1.3.6.1.4.1.1466.115.121.1.51 | **ADSTYPE\_OCTET\_STRING**            |
| TelexNumber                       | 1.3.6.1.4.1.1466.115.121.1.52 | **ADSTYPE\_CASE\_IGNORE\_STRING**     |
| UTCTime                           | 1.3.6.1.4.1.1466.115.121.1.53 | **ADSTYPE\_UTC\_TIME**                |



 

 

 




