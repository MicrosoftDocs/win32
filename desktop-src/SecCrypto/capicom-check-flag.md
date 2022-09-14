---
description: Defines the conditions for which a certificate chain is to be checked.
ms.assetid: 87df623c-5661-4325-8dd6-393ce2e44066
title: CAPICOM_CHECK_FLAG enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_CHECK_FLAG
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_CHECK\_FLAG enumeration

The **CAPICOM\_CHECK\_FLAG** enumeration type defines the conditions for which a certificate chain is to be checked.

## Members



| Member                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Value      |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **CAPICOM\_CHECK\_NONE**                        | No validity checking is done.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0x00000000 |
| **CAPICOM\_CHECK\_TRUSTED\_ROOT**               | Checks for a trusted root of the certificate chain.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 0x00000001 |
| **CAPICOM\_CHECK\_TIME\_VALIDITY**              | Checks the time validity of all certificates in the chain.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0x00000002 |
| **CAPICOM\_CHECK\_SIGNATURE\_VALIDITY**         | Checks for valid signatures on all certificates in the chain.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0x00000004 |
| **CAPICOM\_CHECK\_ONLINE\_REVOCATION\_STATUS**  | Checks the revocation status of all certificates in the chain using certificate revocation lists (CRLs) available online. CRLs are downloaded using the CRL distribution point (CDP) extension in the certificate. <br/> If the CRL has been downloaded and has not expired, CAPICOM uses it and does not go online. If a CRL has not been downloaded or is out of date, CAPICOM goes online to attempt to download the CRL.<br/> This flag is ignored if CAPICOM\_CHECK\_OFFLINE\_REVOCATION\_STATUS is also specified.<br/> | 0x00000008 |
| **CAPICOM\_CHECK\_OFFLINE\_REVOCATION\_STATUS** | Checks the revocation status of all certificates in the chain using only offline CRLs. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                              | 0x00000010 |
| **CAPICOM\_CHECK\_COMPLETE\_CHAIN**             | Checks the complete chain. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0x00000020 |
| **CAPICOM\_CHECK\_NAME\_CONSTRAINTS**           | Checks name constraints. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 0x00000040 |
| **CAPICOM\_CHECK\_BASIC\_CONSTRAINTS**          | Checks basic constraints. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 0x00000080 |
| **CAPICOM\_CHECK\_NESTED\_VALIDITY\_PERIOD**    | Checks nested validity. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 0x00000100 |
| **CAPICOM\_CHECK\_ONLINE\_ALL**                 | Checks all conditions except CAPICOM\_CHECK\_OFFLINE\_REVOCATION\_STATUS. Revocation checks are performed on all certificates in the chain except for the root certificate. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                               | 0x000001EF |
| **CAPICOM\_CHECK\_OFFLINE\_ALL**                | Checks all conditions except CAPICOM\_CHECK\_ONLINE\_REVOCATION\_STATUS. Revocation checks are performed on all certificates in the chain except for the root certificate. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                                                                                                                                                                | 0x000001F7 |



## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




