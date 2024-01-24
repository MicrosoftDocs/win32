---
description: Defines what information is to be queried from a certificate.
ms.assetid: b603c06b-e6d4-4d5d-92b2-3b4f5b93478a
title: CAPICOM_CERT_INFO_TYPE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_CERT_INFO_TYPE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_CERT\_INFO\_TYPE enumeration

The **CAPICOM\_CERT\_INFO\_TYPE** enumeration type defines what information is to be queried from a certificate.

## Members



| Member                                         | Description                                                                                  | Value |
|------------------------------------------------|----------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_CERT\_INFO\_SUBJECT\_SIMPLE\_NAME** | Returns the display name of the certificate subject.<br/>                              | 0     |
| **CAPICOM\_CERT\_INFO\_ISSUER\_SIMPLE\_NAME**  | Returns the display name of the issuer of the certificate.<br/>                        | 1     |
| **CAPICOM\_CERT\_INFO\_SUBJECT\_EMAIL\_NAME**  | Returns the email address of the certificate subject.<br/>                             | 2     |
| **CAPICOM\_CERT\_INFO\_ISSUER\_EMAIL\_NAME**   | Returns the email address of the issuer of the certificate.<br/>                       | 3     |
| **CAPICOM\_CERT\_INFO\_SUBJECT\_UPN**          | Returns the UPN of the certificate subject. Introduced in CAPICOM 2.0.<br/>            | 4     |
| **CAPICOM\_CERT\_INFO\_ISSUER\_UPN**           | Returns the UPN of the issuer of the certificate. Introduced in CAPICOM 2.0.<br/>      | 5     |
| **CAPICOM\_CERT\_INFO\_SUBJECT\_DNS\_NAME**    | Returns the DNS name of the certificate subject. Introduced in CAPICOM 2.0.<br/>       | 6     |
| **CAPICOM\_CERT\_INFO\_ISSUER\_DNS\_NAME**     | Returns the DNS name of the issuer of the certificate. Introduced in CAPICOM 2.0.<br/> | 7     |



## Remarks

The **CAPICOM\_CERT\_INFO\_TYPE** enumeration type is used by the [**Certificate.GetInfo**](certificate-getinfo.md) method.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




